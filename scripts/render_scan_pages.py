#!/usr/bin/env python3
"""Render original scanned PDF pages into connector-friendly JPEG page tiles.

No OCR, no markdown conversion and no modifications to the original source PDFs.
Usage: python scripts/render_scan_pages.py --command '/render 001 1-3' --output /tmp/scan-output
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from dataclasses import dataclass
from pathlib import Path

import fitz
from PIL import Image

COMMAND = re.compile(r"^/render\s+(\d{3})\s+(\d{1,5})(?:-(\d{1,5}))?\s*$")
MAX_PAGES_PER_REQUEST = 8
MAX_JPEG_BYTES = 750_000
DPI = 200


@dataclass(frozen=True)
class RenderRequest:
    serial: str
    first_page: int
    last_page: int


def parse_command(value: str) -> RenderRequest:
    match = COMMAND.fullmatch(value.strip())
    if not match:
        raise ValueError("Expected /render 001 1-8 (document ID and page range)")
    serial, first, last = match.group(1), int(match.group(2)), int(match.group(3) or match.group(2))
    if first < 1 or last < first or last - first + 1 > MAX_PAGES_PER_REQUEST:
        raise ValueError(f"Choose 1-{MAX_PAGES_PER_REQUEST} consecutive pages in ascending order")
    return RenderRequest(serial, first, last)


def find_document(csv_file: Path, serial: str, root: Path) -> tuple[Path, dict]:
    with csv_file.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    matches = [r for r in rows if r.get("serial") == serial]
    if len(matches) != 1:
        raise ValueError(f"Document {serial} not found exactly once in the manifest")
    row = matches[0]
    relative_path = Path(row["repository_path"])
    if relative_path.is_absolute() or ".." in relative_path.parts or relative_path.suffix.lower() != ".pdf":
        raise ValueError("Unsafe PDF path in manifest")
    pdf = (root / relative_path).resolve()
    if not pdf.is_relative_to(root.resolve()) or not pdf.is_file():
        raise ValueError("PDF path escapes repository or is missing")
    declared_sha = row.get("sha256", "").strip().lower()
    if declared_sha:
        with pdf.open("rb") as f:
            actual_sha = hashlib.file_digest(f, "sha256").hexdigest()
        if actual_sha != declared_sha:
            raise ValueError("Source PDF SHA-256 does not match manifest")
    return pdf, row


def jpeg_bytes(im: Image.Image, quality: int = 83) -> bytes:
    file = io.BytesIO()
    im.save(file, format="JPEG", quality=quality, optimize=True)
    return file.getvalue()


def split_to_jpegs(im: Image.Image, max_bytes: int = MAX_JPEG_BYTES) -> list[tuple[tuple[int, int, int, int], bytes]]:
    """Recursively subdivide large raster pages, preserving 200-DPI legibility."""
    queue = [((0, 0, im.width, im.height), im)]
    result: list[tuple[tuple[int, int, int, int], bytes]] = []
    while queue:
        bbox, current = queue.pop(0)
        encoded = jpeg_bytes(current)
        if len(encoded) <= max_bytes:
            result.append((bbox, encoded))
            continue
        x0, y0, x1, y1 = bbox
        if current.height >= current.width and current.height > 700:
            mid = (y0 + y1) // 2
            top = current.crop((0, 0, current.width, mid - y0))
            bottom = current.crop((0, mid - y0, current.width, current.height))
            queue[:0] = [((x0, y0, x1, mid), top), ((x0, mid, x1, y1), bottom)]
        elif current.width > 700:
            mid = (x0 + x1) // 2
            left = current.crop((0, 0, mid-x0, current.height))
            right = current.crop((mid-x0, 0, current.width, current.height))
            queue[:0] = [((x0, y0, mid, y1), left), ((mid, y0, x1, y1), right)]
        else:
            reduced = jpeg_bytes(current, quality=65)
            if len(reduced) > max_bytes:
                raise ValueError("Cannot encode scan tile within GitHub file-size target")
            result.append((bbox, reduced))
    return result


def render(command: str, root: Path, csv_file: Path, output: Path) -> dict:
    req = parse_command(command)
    pdf_file, row = find_document(csv_file, req.serial, root)
    output.mkdir(parents=True, exist_ok=True)
    outputs = []
    with fitz.open(pdf_file) as document:
        if req.last_page > len(document):
            raise ValueError(f"Document {req.serial} has {len(document)} pages; requested {req.last_page}")
        for p in range(req.first_page, req.last_page + 1):
            page = document[p-1]
            pix = page.get_pixmap(matrix=fitz.Matrix(DPI/72,DPI/72), colorspace=fitz.csGRAY, alpha=False)
            img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
            tiles = split_to_jpegs(img)
            for tile_n, (bbox, content) in enumerate(tiles, 1):
                name = f"{req.serial}-page-{p:05d}-tile-{tile_n:02d}.jpg"
                (output / name).write_bytes(content)
                outputs.append({"page":p, "tile":tile_n, "tiles":len(tiles), "file":name, "pixels":list(bbox), "size_bytes":len(content)})
    result = {"serial":req.serial, "source":row["repository_path"], "pages":list(range(req.first_page,req.last_page+1)), "render_dpi":DPI, "images":outputs}
    (output / "manifest.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--command",required=True)
    parser.add_argument("--root",type=Path,default=Path("."))
    parser.add_argument("--csv",type=Path,default=Path("direct_pdf_links.csv"))
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=render(args.command,args.root,args.csv,args.output)
    print(json.dumps({"serial":result["serial"],"pages":result["pages"],"images":len(result["images"])}))

if __name__=="__main__":main()

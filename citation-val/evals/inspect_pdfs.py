#!/usr/bin/env python3
"""Inspect actual citation-val PDF bytes before authoring citation gold cases.

Produces a temporary page-level inspection report: extracted text, layout boxes,
page indexes, image counts, PDF fingerprints. Low-text pages are explicitly
flagged for visual review, not hallucinated into text.
"""
import hashlib
import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "PDFs"
OUT = Path(__file__).resolve().parent / "_inspection_report.json"
SELECTED = [
    "airo-lam-abridged-rhp-bid-application-form.pdf",
    "ecos-india-mobility-drhp-addendum-2024.pdf",
    "salvador-mica-ar-2022-23.pdf",
    "mapro_industries_reg29_share_sale_2026.pdf",
    "ieema_industry_apr-dec_2023.pdf",
    "tata-motors-q3-fy25-results.pdf",
    "google-seo-starter-guide.pdf",
    "rizq-trust-financials-2020.pdf",
]
KEYS = re.compile(
    r"(?i)revenue|total income|total assets|total liabilities|net profit|"
    r"current year|previous year|amount|turnover|quotation|offer|"
    r"date|regulation|registered|share|gross|total|year ended|"
    r"shareholder|board|issue|search engine|crawl|index"
)

def page_inspection(page, idx):
    # Keep raw ordering of extractable PDF text, not synthetic paraphrases.
    raw = page.get_text("text", sort=True)
    blocks = [
        {
            "bbox": [round(v, 2) for v in blk[:4]],
            "text": blk[4][:3500],
        }
        for blk in page.get_text("blocks", sort=True)
        if len(blk) >= 5 and isinstance(blk[4], str) and blk[4].strip()
    ]
    lines = raw.splitlines()
    hits = [i for i, line in enumerate(lines) if KEYS.search(line)]
    snippets = []
    for i in hits[:30]:
        snippets.append({"line": i + 1, "context": "\n".join(lines[max(0, i - 1):i + 3])[:700]})
    return {
        "page": idx + 1,
        "chars": len(raw),
        "images": len(page.get_images(full=False)),
        "requires_visual_review": len(raw.strip()) < 90,
        "keyword_lines": len(hits),
        "preview": raw[:360],
        "text": raw[:18000],
        "text_truncated": len(raw) > 18000,
        "snippets": snippets[:16],
        "blocks": blocks[:70],
    }

report = {"purpose": "TEMPORARY inspection only; not a verified gold set",
          "pages_are": "1-based physical PDF pages, not printed page labels",
          "documents": []}
for name in SELECTED:
    path = SOURCE / name
    if not path.is_file():
        report["documents"].append({"filename": name, "error": "file_missing"})
        continue
    try:
        doc = fitz.open(path)
        pages = [page_inspection(page, idx) for idx, page in enumerate(doc)]
        # Include every page summary, retain full text only for selected candidates.
        candidates = sorted(range(len(pages)),
            key=lambda i: (
                pages[i]["keyword_lines"] * 2 + min(10, pages[i]["chars"] // 350),
                -(i)
            ), reverse=True)
        kept = set(candidates[:10])
        kept.update(range(min(3, len(pages))))
        for i, entry in enumerate(pages):
            if i not in kept:
                entry.pop("text")
                entry.pop("blocks")
                entry.pop("snippets")
        report["documents"].append({
            "filename": name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "pages": len(doc),
            "full_text_pages_in_report": sorted(i+1 for i in kept),
            "page_details": pages
        })
        print(f"{name}: {len(doc)} pages, {sum(p['chars'] for p in pages)} chars, sample={sorted(i+1 for i in kept)}")
    except Exception as exc:
        report["documents"].append({"filename": name, "error": repr(exc)})
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False))
print(f"Report: {OUT} {OUT.stat().st_size} bytes")

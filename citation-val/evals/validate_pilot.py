#!/usr/bin/env python3
"""Validate citation pilot fields against original PDF bytes.

Only text-exact, visually-checked records count as strict gold.
Visual-transcription records are preserved as flagged candidates, not silently
passed as extraction-verified.
"""
import hashlib
import json
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "pilot_cases.json").read_text())
MANIFEST = json.loads((HERE / "pilot_selection_manifest.json").read_text())
REPO = HERE.parents[1]
SOURCE = REPO / "citation-val" / "sources" / "PDFs"

def check(cond, msg):
    if not cond:
        raise AssertionError(msg)

def run():
    check(len(DATA["cases"]) <= 12, "Pilot expanded too far")
    check(len(MANIFEST["selected_documents"]) < 20, "Pilot must remain a subset")
    filenames = {d["filename"] for d in MANIFEST["selected_documents"]}
    docs, strict, review = {}, 0, 0
    try:
        for d in MANIFEST["selected_documents"]:
            src = SOURCE / d["filename"]
            check(src.is_file(), f"Missing original PDF: {src}")
            fingerprint = hashlib.sha256(src.read_bytes()).hexdigest()
            check(fingerprint == d["sha256"], f"PDF changed: {src}")
            pdf = fitz.open(src)
            check(len(pdf) == d["pdf_pages"], f"Page count changed: {src}")
            docs[d["filename"]] = pdf
        for c in DATA["cases"]:
            key = c["id"]
            check(c["pdf_filename"] in filenames, f"{key}: not selected")
            check(c["source_path"] == "citation-val/sources/PDFs/" + c["pdf_filename"],
                  f"{key}: wrong source path")
            doc = docs[c["pdf_filename"]]
            check(c["sha256"] == MANIFEST["selected_documents"][
                next(i for i,d in enumerate(MANIFEST["selected_documents"]) if d["filename"] == c["pdf_filename"])
            ]["sha256"], f"{key}: wrong checksum")
            page_num = c["pdf_page_number_1_based"]
            check(1 <= page_num <= len(doc), f"{key}: invalid physical PDF page")
            loc = c["expected_citation_location"]
            check(loc["page"] == page_num and loc["region"], f"{key}: missing cite region")
            check(c["question"] and c["expected_answer_or_claim"], f"{key}: missing Q/A")
            check(c["exact_supporting_passage"], f"{key}: missing passage")
            page = doc[page_num - 1]
            extracted = page.get_text("text", sort=True)
            flag = c["verification"].get("visual_review_required", False)
            if flag:
                review += 1
                check(c["verification"]["status"] != "verified", f"{key}: review flagged as gold")
                check(c["verification"]["source"].startswith("rendered_scanned_page"),
                      f"{key}: missing visual-method marker")
                if extracted.strip():
                    check("extraction_observation_exact" in c,
                          f"{key}: OCR text present but observation not recorded")
                    check(c["extraction_observation_exact"] in extracted,
                          f"{key}: recorded OCR observation not found")
            else:
                strict += 1
                check(c["verification"].get("text_exact_match") is True,
                      f"{key}: must be text-exact")
                check(c["exact_supporting_passage"] in extracted,
                      f"{key}: exact passage not in original PDF page {page_num}")
                context = c.get("supporting_context_exact")
                if context:
                    check(context in extracted, f"{key}: context not in page")
            for field in ("plausible_incorrect_citation", "repeated_text_decoy",
                          "also_valid_citation"):
                item = c.get(field)
                if item:
                    target = docs[item["pdf_filename"]]
                    p = item["pdf_page_number_1_based"]
                    check(1 <= p <= len(target), f"{key}: wrong {field} page")
                    raw = target[p-1].get_text("text", sort=True)
                    for quote_field in ("exact_plausible_but_incorrect_passage",
                                        "incorrect_form_passage_exact",
                                        "shared_repeated_header_exact",
                                        "exact_supporting_passage",
                                        "context_exact"):
                        if quote_field in item:
                            check(item[quote_field] in raw,
                                  f"{key}: {field}.{quote_field} not found")
                    if field != "also_valid_citation":
                        check(item.get("why_it_does_not_support"),
                              f"{key}: no decoy justification")
            print(f"PASS {key}: {c['pdf_filename']} p{page_num} "
                  f"{'VISUAL REVIEW FLAG' if flag else 'EXACT QUOTE'}")
        all_types = {t for c in DATA["cases"] for t in c["case_types"]}
        for t in ("table_value", "ocr_scanned_text", "repeated_text_matches",
                  "valid_looking_but_non_supporting"):
            check(t in all_types, f"Missing required case type: {t}")
        print(f"RESULT: {strict} extractable, exact-match cases verified; "
              f"{review} visual/OCR cases flagged; {len(DATA['cases'])} total")
    finally:
        for pdf in docs.values():
            pdf.close()

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)

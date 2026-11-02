# Citation grounding pilot (8 cases, 6 source PDFs)

This **small pilot** evaluates whether a citation supports the *specific claim*, at the
correct physical PDF page and the right table row/column, person, form, and time period.
It does **not** assume one case per PDF or pretend all 20 source PDFs have been reviewed.

## Source reconciliation

- Requested path: `citation-evals/source-PDFs` (not present on `main`).
- Actual 20-PDF source path: `citation-val/sources/PDFs`.
- The repository's `main` tree has **no identifiable selection manifest** for this
  20-PDF collection. `pilot_selection_manifest.json` records the actual subset
  inspected and its source SHA-256 hashes; it is *not* claimed to be a pre-existing manifest.
- Eight PDF files were content-inspected; six supply the eight cases in
  `pilot_cases.json`. All files are original repository PDFs, not substitutes.

## Coverage and review status

| Case | Document | Physical PDF page | Stressor | Status |
|---|---|---:|---|---|
| CIT-001 | Tata Motors Q3 FY25 | 45 (bad: 46) | Table value; plausible wrong financial period | Extracted quote + image verified |
| CIT-002 | IEEMA Apr–Dec 2023 | 8 | Dual-column scanned-style table; adjacent row trap | Extracted quote + image verified |
| CIT-003 | ECOS India Mobility addendum | 5 | Wrong shareholder, same metric, same table | Extracted quote + image verified |
| CIT-004 | Airo Lam abridged RHP | 2 (bad: 11) | Repeated header; bid application vs revision form | Extracted quote + image verified |
| CIT-005 | Airo Lam abridged RHP | 7 | IPO use-of-proceeds table with unfilled percent cells | Extracted quote + image verified |
| CIT-006 | Salvador Mica annual report | 3 | Noisy OCR: scanned dividend statement | **Flagged for OCR/visual review** |
| CIT-007 | Mapro share sale disclosure | 1 | Image-only scanned text (no extracted text) | **Flagged for visual review** |
| CIT-008 | Tata Motors Q3 FY25 | 45 (also good: 23) | The same true metric supported in different places | Extracted quote + image verified |

**Important:** Strict extractable gold = 6 cases; visual/OCR-sensitive candidates = 2.
Both flagged cases have visually observed answers and transcribed passages, but
their text spans cannot be certified as exact by extraction. They must remain
flagged until a separate human visual/line-break check accepts them. Never
silently convert an OCR string with corrupted punctuation into an exact quote.

Page numbers are 1-based **physical PDF page indexes**. A document's printed
page label can differ: e.g., ECOS physical PDF page 5 is printed page 2;
Airo Lam physical PDF page 11 is printed page 9. The cases preserve both.

## Required fields in each case

`pdf_filename`, original `source_path`, file `sha256`,
`pdf_page_number_1_based`, `question`, `expected_answer_or_claim`,
`exact_supporting_passage`, `expected_citation_location` (page and region),
case types, and `verification` status. Negative examples carry the exact
`plausible_incorrect_citation` or `repeated_text_decoy` and an explanation
of why the passage fails the question. When multiple pages *really do*
support the same claim, `also_valid_citation` prevents false rejection.

## Validation

From repository root:

```bash
python -m pip install 'pymupdf>=1.24,<2'
python citation-val/evals/validate_pilot.py
```

The validator opens the actual PDF files, checks SHA-256, checks original PDF
page indexes, tests exact *verbatim* supporting and negative passages against
the named page, and ensures all required categories are present. It reports
visual-review candidates separately, rather than marking them as strict gold.

The `inspect_pdfs.py` utility can regenerate a transient extraction report for
further manual triage. It is not a gold set generator. The pilot should not be
expanded before the two flagged cases are visually signed off and citation
precision is measured on a real model run.

## Suggested rubric for citation evaluators

1. **Answer correctness**: exact entity, time period, unit, and number.
2. **Source correctness**: filename and SHA-256 match.
3. **Page correctness**: physical PDF page matches a supporting location.
4. **Passage support**: cited row, column, sentence, or form actually entails
   the claim (not just a shared heading or plausible number).
5. **False-positive-first**: an attractive but non-supporting quote is a fail.
6. **OCR uncertainty**: unresolved visual/text mismatch is review, not pass.
7. **Legitimate alternatives**: any independently supporting cited page is
   valid, even if it is not the primary expected page.

No evaluation-model outputs are claimed. This is a ground-truth fixture pilot.

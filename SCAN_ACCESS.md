# Scanned PDF access without OCR

## Goal

Read **any** of the 100 original scanned PDFs in this repository without relying on the GitHub Contents API's 1 MB Base64 response limitation. Originals are not modified; text extraction and Markdown files are not required.

## How it works

1. A repository owner comments `/render 001 1-4` on any **GitHub issue** (not a pull request).
2. GitHub Actions reads `direct_pdf_links.csv` and checks the source PDF's SHA-256.
3. The runner renders pages 1 through 4 at 200 DPI using PyMuPDF, converts them to grayscale JPEGs, and tiles oversized images so **each JPEG is below 750 KB**.
4. The run publishes only the requested page images and `manifest.json` to the **`scan-previews`** branch. The previous preview is replaced so the repository does not continuously grow with all 34,889 pages.
5. The issue receives a comment linking to that branch. Connected GitHub tools can fetch each JPEG using their Base64 content API, enabling direct visual inspection of scans and tables.

### Examples

- `/render 001 1-4`: First four pages of PDF 001
- `/render 098 11`: Page 11 of PDF 098
- `/render 100 1-7`: All seven pages of PDF 100

The command accepts only exactly three-digit document IDs, existing pages, and an ascending range of **at most 8 pages per request**. Only GitHub comments from `ayushcodes13` trigger the job. The script verifies source-file paths remain within the repository and matches each source SHA-256 against the CSV.

## Important constraints

- This is an **on-demand page-reading mechanism**, not a claim that a model can keep every scanned page in context simultaneously.
- The GitHub Actions workflow must be merged onto the default branch before `issue_comment` events will trigger it.
- It requires Actions enabled and a `GITHUB_TOKEN` allowed to write a separate `scan-previews` branch (permissions are requested in the workflow).
- Cache images are replaced by the next request; capture evidence/notes before rendering another batch.
- No content is sent to an external OCR or document conversion service. All rendering runs on GitHub's runner. GitHub and its Actions runner still process the scans, which is appropriate only if permitted for these documents.
- Some unusually dense pages may be split into multiple JPEG tiles, listed in `manifest.json`. Each tile retains its full-resolution position.
- Images are for visual document review, **not perfect text or number recognition**. Check ambiguous values against the scans.

## Developer verification

```bash
python -m pip install 'PyMuPDF==1.26.7' 'Pillow==12.0.0'
python -m unittest discover -s tests -v
python scripts/render_scan_pages.py --command '/render 001 1-3' --output /tmp/scan-output
```

The tests generate a synthetic 3-page image-only PDF with no text layer and confirm rendered page outputs remain under the byte limit. Integration with a live GitHub Actions runner still needs to be validated after merge. The workflow intentionally leaves `main` unchanged when publishing previews.

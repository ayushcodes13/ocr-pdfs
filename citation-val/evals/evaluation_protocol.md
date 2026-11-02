# Citation eval pilot: what it checks and how to score it

This is a small, source-grounded gold set, not a model benchmark result. It uses the 20 PDFs already in `citation-val/sources/PDFs`, but only the documents listed as inspected in `pilot_selection_manifest.json`. Do not expand the document sample until this pilot's case labels and scoring are reviewed.

## Required pieces of a citation test case

Each case needs:

1. **A question and expected answer claim**, small enough to check at claim level. Identify numbers, units, people/entities, date/period, and qualifications that matter.
2. **A stable source identity**: original PDF filename/path, SHA-256, and 1-based physical PDF page. Printed page labels are recorded separately because they can differ from PDF page indexes.
3. **Manually verified supporting evidence**: exact text where extractable, plus the surrounding table/form context and a concise description of the page region. For image/OCR text, record the human transcription, render/page reviewed, and OCR mismatch; do not call it an exact extraction match.
4. **Valid alternatives and deliberate decoys**: record every independently supporting location that should pass, and plausible wrong evidence that must fail (wrong period, person, row/column, form, or a repeated heading).
5. **Four independent result labels** for each run: citation presence, citation structure/resolution, claim support, and open/highlight behavior. Record green/orange separately from these labels.

The current eight cases use six of the 20 PDFs. The two scan cases have now been visually checked against rendered pages; their OCR extraction differences remain recorded. The 20-document corpus has not been broadened.

## Four checks

| Check | Unit | Pass rule | Fail examples |
|---|---|---|---|
| Citation presence | Each factual claim in the answer marked as requiring document evidence | At least one citation is attached to that claim | Correct answer but no citation; uncited table number |
| Citation structure | Every citation object emitted | Citation parses and resolves to the expected source/version and a valid physical page | Malformed payload, unknown handle, stale/deleted version, invalid page, unresolved source |
| Claim support | Every emitted citation-to-claim pair | The cited span and its context entail the specific claim | Wrong period/person, wrong table row or column, heading-only match, partial quote that omits a qualifier |
| Open/highlight | Every emitted citation | Opens the accepted document/page and highlights the supporting span or table cell | Opens wrong source/page, no highlight, misplaced highlight, highlight on decoy text |

If no citation is emitted, presence fails. Structure, support, and UI are recorded as `not_applicable` for the nonexistent citation, not as passes. If a malformed citation is emitted, structure fails; support and open/highlight are marked `not_evaluable` with the structural failure linked. This avoids disguising a broken reference as unsupported evidence or a UI defect. A citation that resolves and opens but points at a non-supporting passage is evaluable and fails support even if it is green.

## Green and orange

Only the two observed chip colors, **green** and **orange**, are recorded. Save the color as an observation next to the citation and separately record whether evidence supports the claim. Green is not a correctness verdict: a wrong-period or wrong-row quote can be present on the cited page and still be green. A `green_but_wrong` case is therefore a claim-support failure, regardless of chip color. The app's exact color transition should be captured during the later Bynd run rather than assumed from this PDF-only gold set.

## Candidate scoring report

Do not collapse these into one weighted percentage until the team agrees on weights. Report the following with numerator and denominator so a score change is interpretable:

- **Citation coverage** = factual claims with at least one emitted citation / all gold claims marked citation-required. Missing citations fail this metric.
- **Citation structure rate** = emitted citations that parse and resolve to an accepted source/version/page / all emitted citations. If none are emitted, report `N/A (0 citations)`, not 100%.
- **Claim-support rate** = emitted citation-to-claim pairs judged supporting / all emitted citation-to-claim pairs judged. Include wrong/unsupported but resolvable spans as failures. Keep structurally broken references in a separate count because no passage can be judged.
- **Open/highlight rate** = emitted citations that open the accepted source/page and highlight the supporting region / all emitted citations. A failed open or missing/misplaced highlight is a failure.

Also show raw counts for missing claims, malformed/unresolved citations, non-supporting citations, wrong-page opens, missing highlights, and misplaced highlights. Keep color counts (green/orange) cross-tabulated with claim-support labels so green false positives are visible. Do not use an aggregate pass threshold until one is explicitly agreed.

## Per-case result record for a later system run

Keep run output separate from gold truth. For each case and answer claim, store the question, raw answer, emitted citation payloads, resolver result, source/version/page opened, highlight geometry or a screenshot/reference, observed chip color, the four labels, reviewer/judge rationale, and run/build identifier. Use `pass`, `fail`, `not_applicable`, or `not_evaluable` for each check; an unresolved human judgment is `needs_review`. Never overwrite the expected evidence when recording a run.

## Current coverage and remaining boundary

The pilot has verified expected evidence for table values, wrong period, wrong entity, repeated headings/forms, a plausible adjacent table value, a scanned/OCR-sensitive sentence, and a legitimate alternative supporting page. Every case is a citation-required question, so an uncited answer is explicitly a presence failure. The later system run must observe actual citation payloads, page opens, highlights, and colors. This pilot does not itself prove the app emits or renders any particular citation, and it does not yet provide a runnable chat/evaluator integration.

# Financial OCR dataset: 100 PDFs

This repository contains exactly 100 deduplicated financial PDFs. Ranks 001–050 are the preserved full-page scanned set. Ranks 051–100 are mixed/partial PDFs; their exact OCR-needed page numbers are now classified with the page-level OCR detector from `bynd-chat-trunk/backend/src/core/ocr/ocrtriage` and stored in the manifest and page audit.

## Dataset counts

| Measure | Result |
|---|---:|
| PDFs | 100 |
| Fully scanned PDFs, every page verified | 50 |
| Mixed/partial PDFs with page-level OCR triage | 50 |
| Total PDF pages | 10,921 |
| Pages in preserved fully scanned PDFs | 2,743 |
| Pages classified as needing OCR in ranks 051–100 | 1,007 of 8,178 |
| Conservative time-limit pages included in OCR-needed lists | 12 |
| Total current PDF bytes | 696,752,833 (0.697 GB; 0.649 GiB) |

## Page verification method

For ranks 051–100, page numbers in `verified_page_numbers` are the pages returned with `needs_ocr=True` by the chat OCR classifier. Audit version: `2026-10-09.handover.chat1`; run settings: 4 workers, 1,000 ms per page, 90 seconds per document. All 50 documents completed in `classified` mode. The classifier reason counts across the added 50 are: bilevel_scan: 131, clearscan_text: 2, hidden_text_layer: 1, image_text: 290, image_text_lowres: 494, ocr_layer_over_image: 1, time_limit: 12, vector_text: 77.

12 pages were conservatively marked `needs_ocr` due to the per-page `time_limit`; their exact numbers are in `conservative_ocr_page_numbers` and their reason codes remain in the audit. These are flagged for OCR by the code, but are not claimed as visually confirmed scans. The first 50 retain their prior all-page image verification.

## Ranked document inventory

| Rank | PDF/document | Pages | Verified page count | Verified page numbers | Verification |
|---:|---|---:|---:|---|---|
| 001 | `annual_report_2023_24.pdf` | 680 | 680 | 1-680 | Full-page scan verified |
| 002 | `Nureca_Limited_Annual_Report_FY2025-26.pdf` | 181 | 181 | 1-181 | Full-page scan verified |
| 003 | `blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf` | 138 | 138 | 1-138 | Full-page scan verified |
| 004 | `blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf` | 138 | 138 | 1-138 | Full-page scan verified |
| 005 | `blob_185_185_automotive_component_manufacturers_association_of_india__acma__original_annual_report_2021_22.pdf` | 112 | 112 | 1-112 | Full-page scan verified |
| 006 | `Aastha_Spintex_Limited_Annual_Report_2024-25.pdf` | 95 | 95 | 1-95 | Full-page scan verified |
| 007 | `blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf` | 94 | 94 | 1-94 | Full-page scan verified |
| 008 | `20MICRONS_ar_2011.pdf` | 90 | 90 | 1-90 | Full-page scan verified |
| 009 | `blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf` | 88 | 88 | 1-88 | Full-page scan verified |
| 010 | `blob_050_050_indian_institute_of_packaging__iip___semi-private__original_annual_report_2022_23.pdf` | 72 | 72 | 1-72 | Full-page scan verified |
| 011 | `Nova_Iron_and_Steel_Limited_BSE_Regulation_30_Financial_Disclosure_2026.pdf` | 68 | 68 | 1-68 | Full-page scan verified |
| 012 | `shiv fabritex international pvt ltd.pdf` | 60 | 60 | 1-60 | Full-page scan verified |
| 013 | `Yugeri Marketing Private Limited.pdf` | 55 | 55 | 1-55 | Full-page scan verified |
| 014 | `Jolly_Plastic_Industries_Limited_Annual_Report_2025-26.pdf` | 50 | 50 | 1-50 | Full-page scan verified |
| 015 | `annual_report_2020_21_chapter_8_10.pdf` | 45 | 45 | 1-45 | Full-page scan verified |
| 016 | `Saffron_Industries_Limited_FY2025-26_Audited_Financial_Results.pdf` | 44 | 44 | 1-44 | Full-page scan verified |
| 017 | `FIDC_19th_Annual_Report_2022-23.pdf` | 40 | 40 | 1-40 | Full-page scan verified |
| 018 | `blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf` | 39 | 39 | 1-39 | Full-page scan verified |
| 019 | `blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf` | 36 | 36 | 1-36 | Full-page scan verified |
| 020 | `Edelweiss_Suraj_Estate_Company_Update_July_2024.pdf` | 35 | 35 | 1-35 | Full-page scan verified |
| 021 | `Wipro_Q4_FY25_Board_Outcome_Financial_Results.pdf` | 35 | 35 | 1-35 | Full-page scan verified |
| 022 | `Tata_Steel_FY25_Board_Outcome_Audited_Financial_Results.pdf` | 34 | 34 | 1-34 | Full-page scan verified |
| 023 | `Gianna Agro Pvt. Ltd.pdf` | 31 | 31 | 1-31 | Full-page scan verified |
| 024 | `Suruchi Dairy & Dairy Products.pdf` | 28 | 28 | 1-28 | Full-page scan verified |
| 025 | `Bank_of_Maharashtra_Q1_FY27_Financial_Results.pdf` | 27 | 27 | 1-27 | Full-page scan verified |
| 026 | `Tandhan_Industries_Monitoring_Agency_Report_Q4_FY26.pdf` | 27 | 27 | 1-27 | Full-page scan verified |
| 027 | `blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf` | 27 | 27 | 1-27 | Full-page scan verified |
| 028 | `blobextra_0e46676491d6_balance_sheet_2020_21.pdf` | 27 | 27 | 1-27 | Full-page scan verified |
| 029 | `blobextra_a79f601cfc45_audited_accounts_as_on_31st_march_2023.pdf` | 26 | 26 | 1-26 | Full-page scan verified |
| 030 | `PVP_Ventures_Limited_Debenture_and_Repayment_Schedule_Disclosure.pdf` | 26 | 26 | 1-26 | Full-page scan verified |
| 031 | `blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf` | 24 | 24 | 1-24 | Full-page scan verified |
| 032 | `Bharti_Airtel_Q4_FY25_Financial_Results.pdf` | 23 | 23 | 1-23 | Full-page scan verified |
| 033 | `Asian_Hotels_East_Audited_FY26_Financial_Results.pdf` | 22 | 22 | 1-22 | Full-page scan verified |
| 034 | `Bharti_Airtel_Q4_FY26_Financial_Results.pdf` | 21 | 21 | 1-21 | Full-page scan verified |
| 035 | `Prodocs_Solutions_Limited_Audited_Financial_Results_FY2025-26.pdf` | 20 | 20 | 1-20 | Full-page scan verified |
| 036 | `Meso Private Limited.pdf` | 19 | 19 | 1-19 | Full-page scan verified |
| 037 | `Primo_Chemicals_Limited_Postal_Ballot_Notice_Financial_Disclosure_2026.pdf` | 19 | 19 | 1-19 | Full-page scan verified |
| 038 | `Nirmal_Bang_Epigral_Monthly_Research_May_2024.pdf` | 18 | 18 | 1-18 | Full-page scan verified |
| 039 | `Havells_India_Q4_FY25_Board_Outcome_Audited_Results.pdf` | 17 | 17 | 1-17 | Full-page scan verified |
| 040 | `AXISCADES_Consolidated_Financial_Results_Q2_FY25.pdf` | 16 | 16 | 1-16 | Full-page scan verified |
| 041 | `CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf` | 16 | 16 | 1-16 | Full-page scan verified |
| 042 | `ICICI_Lombard_FY25_Board_Outcome_Audited_Results.pdf` | 15 | 15 | 1-15 | Full-page scan verified |
| 043 | `AXISCADES_Integrated_Filing_Q3_FY25_Financial_Results.pdf` | 11 | 11 | 1-11 | Full-page scan verified |
| 044 | `Nuvama_V2_Retail_Company_Update_October_2024.pdf` | 11 | 11 | 1-11 | Full-page scan verified |
| 045 | `Shardul_Securities_Limited_Q1_FY27_Financial_Results.pdf` | 11 | 11 | 1-11 | Full-page scan verified |
| 046 | `AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf` | 9 | 9 | 1-9 | Full-page scan verified |
| 047 | `21STCENMGM_qr_29_07_2025_171051.pdf` | 7 | 7 | 1-7 | Full-page scan verified |
| 048 | `Newtrac_Foods_and_Beverages_Q1_FY27_Financial_Results.pdf` | 7 | 7 | 1-7 | Full-page scan verified |
| 049 | `Nirmal_Bang_ITD_Cementation_Company_Update_April_2024.pdf` | 5 | 5 | 1-5 | Full-page scan verified |
| 050 | `blobextra_ce38744b83cf_blobextra_for_the_year_2024_2025.pdf` | 4 | 4 | 1-4 | Full-page scan verified |
| 051 | `IEEMA_Industry_Overview_Apr-Jun_FY2024.pdf` | 10 | 10 | 1,2,3,4,5,6,7,8,9,10 | Chat OCR classifier; needs_ocr |
| 052 | `IEEMA_Industry_Overview_Apr-Dec_FY2023.pdf` | 10 | 10 | 1,2,3,4,5,6,7,8,9,10 | Chat OCR classifier; needs_ocr |
| 053 | `IEEMA_Industry_Overview_FY2022-23.pdf` | 9 | 9 | 1,2,3,4,5,6,7,8,9 | Chat OCR classifier; needs_ocr |
| 054 | `Ministry_of_Education_Budgeted_Expenditure_Analysis_2020-2022.pdf` | 132 | 2 | 7,22 | Chat OCR classifier; needs_ocr |
| 055 | `FIDC_20th_Annual_Report_2023-24.pdf` | 35 | 19 | 1,3,4,5,6,16,23,24,25,26,27,28,29,30,31,32,33,34,35 | Chat OCR classifier; needs_ocr |
| 056 | `IBAI_21st_Annual_Report_2023.pdf` | 57 | 24 | 2,13,14,15,16,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56 | Chat OCR classifier; needs_ocr |
| 057 | `Sa-Dhan_Annual_Report_2020-21.pdf` | 56 | 13 | 1,2,3,28,43,44,47,48,49,51,53,55,56 | Chat OCR classifier; needs_ocr |
| 058 | `India_Tourism_Statistics_2021_Ministry_of_Tourism.pdf` | 248 | 24 | 1,3,5,15,23,27,28,32,34,81,89,101,105,145,156,169,179,185,193,213,214,233,239,248 | Chat OCR classifier; needs_ocr |
| 059 | `CropLife_India_Pesticide_Import_Position_Paper_2024.pdf` | 16 | 6 | 1,6,13,14,15,16 | Chat OCR classifier; needs_ocr |
| 060 | `Akshay_Urja_MNRE_Vol14_Issue1_2025.pdf` | 40 | 16 | 1,2,3,4,10,17,18,19,20,22,23,24,25,27,32,38 | Chat OCR classifier; needs_ocr |
| 061 | `Infomerics_Credit_Rating_Brochure_Nov2024.pdf` | 8 | 8 | 1,2,3,4,5,6,7,8 | Chat OCR classifier; needs_ocr |
| 062 | `IEEMA_Industry_Overview_Apr-Sep_FY2023-24.pdf` | 10 | 10 | 1,2,3,4,5,6,7,8,9,10 | Chat OCR classifier; needs_ocr |
| 063 | `Ministry_of_Power_Energy_Accounting_Guidelines_2025.pdf` | 23 | 15 | 1,2,9,10,13,14,15,16,17,18,19,20,21,22,23 | Chat OCR classifier; needs_ocr |
| 064 | `Steel_Exchange_India_Annual_Report_2019-20.pdf` | 118 | 14 | 1,2,3,43,66,67,81,90,97,109,113,114,117,118 | Chat OCR classifier; needs_ocr |
| 065 | `Steel_Exchange_India_Annual_Report_2025-26.pdf` | 165 | 24 | 1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,20,22,23,24,25,26,27,29,165 | Chat OCR classifier; needs_ocr |
| 066 | `ANKITA_KNIT_WEAR_LIMITED__DRHP__2009.pdf` | 209 | 7 | 22,23,24,31,45,76,81 | Chat OCR classifier; needs_ocr |
| 067 | `EQUITAS_SMALL_FINANCE_BANK_LIMITED__FOD__2020.pdf` | 411 | 20 | 1,99,101,102,103,104,105,106,107,109,110,113,114,115,116,117,118,119,120,139 | Chat OCR classifier; needs_ocr |
| 068 | `INDO_THAI_SECURITIES_LIMITED__DRHP__2011.pdf` | 327 | 10 | 1,75,76,77,78,79,81,82,83,84 | Chat OCR classifier; needs_ocr |
| 069 | `SIGACHI_INDUSTRIES_LIMITED__RHP__2021.pdf` | 392 | 12 | 1,137,138,140,142,143,146,147,150,152,161,248 | Chat OCR classifier; needs_ocr |
| 070 | `8b90b9f3-76d2-4d18-ad1c-21b6d11fb727.pdf` | 118 | 9 | 1,2,3,4,17,49,113,117,118 | Chat OCR classifier; needs_ocr |
| 071 | `caaa82f9-e0e9-47ff-b31f-33801b06ff9f.pdf` | 185 | 12 | 2,3,4,5,6,7,46,47,60,134,184,185 | Chat OCR classifier; needs_ocr |
| 072 | `056_ACROPETAL_TECHNOLOGIES_LIMITED_FOD.pdf` | 306 | 29 | 1,14,32,93,94,95,96,97,98,99,100,101,105,106,107,110,111,113,139,221,258,261,263,264,298,299,300,301,302 | Chat OCR classifier; needs_ocr |
| 073 | `509762__3ed5c6d6-7e32-4f58-ad46-b1e484bcbd0f.pdf` | 3 | 3 | 1,2,3 | Chat OCR classifier; needs_ocr |
| 074 | `532700__300778df-eff5-4a1e-b248-8fff79ce17c5.pdf` | 7 | 4 | 4,5,6,7 | Chat OCR classifier; needs_ocr |
| 075 | `533192__d47508d9-0361-4664-847b-7d99c83b5272.pdf` | 3 | 3 | 1,2,3 | Chat OCR classifier; needs_ocr |
| 076 | `541703__87a196e6-2d5e-4831-b4a7-c999ba8742ea.pdf` | 3 | 3 | 1,2,3 | Chat OCR classifier; needs_ocr |
| 077 | `543233__b25a8485-9ce9-4763-bdf9-f878ef454dad.pdf` | 4 | 4 | 1,2,3,4 | Chat OCR classifier; needs_ocr |
| 078 | `543540__8e5be6d6-a7c0-4586-8101-84a4a4671f78.pdf` | 3 | 2 | 2,3 | Chat OCR classifier; needs_ocr |
| 079 | `543621__dd9e16e8-0bc2-4d0f-8ee9-600df2bff2b5.pdf` | 3 | 3 | 1,2,3 | Chat OCR classifier; needs_ocr |
| 080 | `544626__3c75ff40-37f2-4dee-ac5f-29de11b4ecfd.pdf` | 3 | 3 | 1,2,3 | Chat OCR classifier; needs_ocr |
| 081 | `104e37c6-5f6a-4614-a80f-60301a139f9c.pdf` | 11 | 9 | 1,2,3,4,5,6,7,8,9 | Chat OCR classifier; needs_ocr |
| 082 | `5baa1b96-a282-436b-817a-c1d232464e0b.pdf` | 11 | 7 | 1,4,5,6,9,10,11 | Chat OCR classifier; needs_ocr |
| 083 | `4e0aa144-abe5-4666-bab2-7f4bca64d634.pdf` | 7 | 7 | 1,2,3,4,5,6,7 | Chat OCR classifier; needs_ocr |
| 084 | `038_VIBRANT_GLOBAL_CAPITAL_LIMITED._FOD.pdf` | 263 | 9 | 1,76,77,81,82,83,85,177,178 | Chat OCR classifier; needs_ocr |
| 085 | `060_COFFEE_DAY_ENTERPRISES_LIMITED_DRHP.pdf` | 920 | 52 | 1,65,66,68,69,70,73,145,147,148,150,151,152,153,155,157,158,160,161,162,163,165,166,168,171,175,186,254,280,281,282,283,284,285,286,287,288,289,295,429,430,431,442,505,506,507,508,509,785,788,789,799 | Chat OCR classifier; needs_ocr |
| 086 | `061_NUZIVEEDU_SEEDS_LIMITED_DRHP.pdf` | 878 | 111 | 1,88,90,158,160,161,164,166,171,172,173,174,175,178,179,181,183,186,196,198,204,207,262,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,738,741,742,752 | Chat OCR classifier; needs_ocr |
| 087 | `133_S_CHAND_AND_COMPANY_LIMITED_DRHP.pdf` | 597 | 21 | 1,49,50,51,53,121,122,127,137,144,151,403,404,405,406,407,408,409,509,510,519 | Chat OCR classifier; needs_ocr |
| 088 | `141_HPL_ELECTRIC___POWER_LIMITED_FOD.pdf` | 469 | 35 | 1,52,56,57,58,59,60,61,106,107,110,112,114,115,117,118,119,120,121,122,123,124,126,127,128,129,130,131,133,147,179,385,388,389,399 | Chat OCR classifier; needs_ocr |
| 089 | `192_MAHINDRA_LOGISTICS_LIMITED_DRHP.pdf` | 562 | 63 | 1,32,118,119,120,122,123,126,134,135,144,146,148,150,184,226,227,228,229,230,265,267,268,285,286,287,289,290,293,296,297,299,300,301,302,306,309,312,314,316,317,321,353,361,378,379,380,381,382,386,389,392,393,397,398,400,403,407,408,505,509,511,522 | Chat OCR classifier; needs_ocr |
| 090 | `bse-one-day__500188__2026__d413963a-1759-4baa-bc3b-e46241042372.pdf` | 4 | 4 | 1,2,3,4 | Chat OCR classifier; needs_ocr |
| 091 | `bse-one-day__500330__2026__1593a02f-7ce7-492b-af7b-f5b51603cb39.pdf` | 5 | 5 | 1,2,3,4,5 | Chat OCR classifier; needs_ocr |
| 092 | `bse-one-day__522241__2026__792f7779-cef8-49f1-a704-6b457cc81311.pdf` | 75 | 75 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75 | Chat OCR classifier; needs_ocr |
| 093 | `bse-one-day__539787__2026__1189a7e3-9a32-4ada-a96d-a74d5519adc7.pdf` | 14 | 8 | 7,8,9,10,11,12,13,14 | Chat OCR classifier; needs_ocr |
| 094 | `bse-one-day__539854__2026__1d8b905b-abc2-4527-ae0a-ac7b1a10fbeb.pdf` | 5 | 5 | 1,2,3,4,5 | Chat OCR classifier; needs_ocr |
| 095 | `bse-one-day__540726__2026__06d8fc46-4078-495c-939c-c0e8e022c016.pdf` | 8 | 7 | 1,2,3,4,5,7,8 | Chat OCR classifier; needs_ocr |
| 096 | `bse-one-day__543264__2026__6b26b4c1-d1b2-4efc-8619-ff640b03d708.pdf` | 47 | 38 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47 | Chat OCR classifier; needs_ocr |
| 097 | `bse-one-day__544338__2026__65c1203e-4148-41e9-ba8f-499af4dbc0f3.pdf` | 19 | 9 | 2,3,4,5,6,7,8,9,10 | Chat OCR classifier; needs_ocr |
| 098 | `119_MANORAMA_INDUSTRIES_LIMITED_FOD.pdf` | 447 | 89 | 1,50,53,54,55,56,127,130,131,132,133,136,139,141,142,146,147,151,152,153,154,155,156,157,159,160,173,176,210,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,317,318,365,366,375,376 | Chat OCR classifier; needs_ocr |
| 099 | `184_SOFTTECH_ENGINEERS_LIMITED_FOD.pdf` | 418 | 67 | 1,49,51,52,53,56,57,60,61,62,140,142,143,144,146,148,150,153,157,158,160,161,162,169,170,204,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,284,285,332,335,336,346 | Chat OCR classifier; needs_ocr |
| 100 | `136_ROUTE_MOBILE_LIMITED_DRHP.pdf` | 504 | 58 | 1,116,118,125,130,169,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,387,434,436,437,446 | Chat OCR classifier; needs_ocr |

## Source and audit files

- `ranked_100_manifest.csv` records source metadata and verified page numbers for each PDF.
- `top_50_manifest.csv` indexes the preserved full-page scans.
- `inventory.csv` summarizes verified page numbers/counts for all 100 PDFs.
- `direct_pdf_links.csv` contains raw GitHub download links and page results.
- `ocr_classifier_document_audit_2026-10-27.csv` records one classifier summary per added PDF, including fallback pages, reason codes, classifier version, and processing time.
- `ocr_classifier_page_audit_2026-10-27.csv` records the classifier decision and reason code for every page in ranks 051–100.
- `replacement_log_2026-10-27.csv` records the 50 replaced paths and their verified replacement page lists.
- `OCR triage implementation`: `Bynd-ai/chat` `backend/src/core/ocr/ocrtriage`; this repository stores the generated page-level results.

Pages not flagged by `needs_ocr` are simply not flagged by this classifier run.

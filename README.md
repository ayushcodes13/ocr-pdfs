# Financial OCR dataset: 100 PDFs

This repository contains exactly 100 deduplicated financial PDFs. Ranks 001–050 are the original verified full-page scanned set and are preserved unchanged. Ranks 051–100 replace the previous mixed/partial group whose scan/OCR page counts had not been audited. The replacement PDFs come from the local Azure Blob candidate set; their OCR-relevant pages are recorded individually in the manifest.

## Dataset counts

| Measure | Result |
|---|---:|
| PDFs in current default-branch dataset | 100 |
| Fully scanned PDFs with every page image-backed and verified | 50 |
| Mixed/partial OCR-candidate PDFs added | 50 |
| Total PDF pages | 10,921 |
| Pages in preserved fully scanned PDFs | 2,743 |
| Selectable-text layer pages among preserved full scans | 790 |
| Visually reviewed OCR-candidate pages in added 50 | 512 of 8,178 |
| Added PDFs with every page flagged as OCR-relevant candidate | 6 |
| Total current PDF bytes | 696,752,833 (0.697 GB; 0.649 GiB) |

**Interpretation:** “Fully scanned” is reserved for the 50 preserved PDFs with every page verified as image-backed. The added 50 have known, visually reviewed OCR-relevant page numbers and counts. Six have every page marked as an OCR candidate, but they remain in the mixed/partial group because this audit did not certify full-page image coverage for the entire document. The remaining pages are not marked as OCR candidates; that does **not** prove they are non-OCRable or text-selectable. No OCR engine was run as part of this repository update.

## Ranked document inventory

| Rank | PDF/document | Pages | Fully scanned pages verified | OCR-candidate pages | OCR text-layer pages | Type |
|---:|---|---:|---:|---:|---:|---|
| 001 | `annual_report_2023_24.pdf` | 680 | 680 | 680 | 0 | Full-page scan |
| 002 | `Nureca_Limited_Annual_Report_FY2025-26.pdf` | 181 | 181 | 181 | 180 | Full-page scan |
| 003 | `blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf` | 138 | 138 | 138 | 0 | Full-page scan |
| 004 | `blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf` | 138 | 138 | 138 | 0 | Full-page scan |
| 005 | `blob_185_185_automotive_component_manufacturers_association_of_india__acma__original_annual_report_2021_22.pdf` | 112 | 112 | 112 | 0 | Full-page scan |
| 006 | `Aastha_Spintex_Limited_Annual_Report_2024-25.pdf` | 95 | 95 | 95 | 0 | Full-page scan |
| 007 | `blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf` | 94 | 94 | 94 | 0 | Full-page scan |
| 008 | `20MICRONS_ar_2011.pdf` | 90 | 90 | 90 | 0 | Full-page scan |
| 009 | `blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf` | 88 | 88 | 88 | 0 | Full-page scan |
| 010 | `blob_050_050_indian_institute_of_packaging__iip___semi-private__original_annual_report_2022_23.pdf` | 72 | 72 | 72 | 0 | Full-page scan |
| 011 | `Nova_Iron_and_Steel_Limited_BSE_Regulation_30_Financial_Disclosure_2026.pdf` | 68 | 68 | 68 | 68 | Full-page scan |
| 012 | `shiv fabritex international pvt ltd.pdf` | 60 | 60 | 60 | 0 | Full-page scan |
| 013 | `Yugeri Marketing Private Limited.pdf` | 55 | 55 | 55 | 0 | Full-page scan |
| 014 | `Jolly_Plastic_Industries_Limited_Annual_Report_2025-26.pdf` | 50 | 50 | 50 | 50 | Full-page scan |
| 015 | `annual_report_2020_21_chapter_8_10.pdf` | 45 | 45 | 45 | 0 | Full-page scan |
| 016 | `Saffron_Industries_Limited_FY2025-26_Audited_Financial_Results.pdf` | 44 | 44 | 44 | 44 | Full-page scan |
| 017 | `FIDC_19th_Annual_Report_2022-23.pdf` | 40 | 40 | 40 | 36 | Full-page scan |
| 018 | `blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf` | 39 | 39 | 39 | 0 | Full-page scan |
| 019 | `blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf` | 36 | 36 | 36 | 0 | Full-page scan |
| 020 | `Edelweiss_Suraj_Estate_Company_Update_July_2024.pdf` | 35 | 35 | 35 | 34 | Full-page scan |
| 021 | `Wipro_Q4_FY25_Board_Outcome_Financial_Results.pdf` | 35 | 35 | 35 | 35 | Full-page scan |
| 022 | `Tata_Steel_FY25_Board_Outcome_Audited_Financial_Results.pdf` | 34 | 34 | 34 | 34 | Full-page scan |
| 023 | `Gianna Agro Pvt. Ltd.pdf` | 31 | 31 | 31 | 0 | Full-page scan |
| 024 | `Suruchi Dairy & Dairy Products.pdf` | 28 | 28 | 28 | 0 | Full-page scan |
| 025 | `Bank_of_Maharashtra_Q1_FY27_Financial_Results.pdf` | 27 | 27 | 27 | 27 | Full-page scan |
| 026 | `Tandhan_Industries_Monitoring_Agency_Report_Q4_FY26.pdf` | 27 | 27 | 27 | 26 | Full-page scan |
| 027 | `blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf` | 27 | 27 | 27 | 0 | Full-page scan |
| 028 | `blobextra_0e46676491d6_balance_sheet_2020_21.pdf` | 27 | 27 | 27 | 0 | Full-page scan |
| 029 | `blobextra_a79f601cfc45_audited_accounts_as_on_31st_march_2023.pdf` | 26 | 26 | 26 | 0 | Full-page scan |
| 030 | `PVP_Ventures_Limited_Debenture_and_Repayment_Schedule_Disclosure.pdf` | 26 | 26 | 26 | 26 | Full-page scan |
| 031 | `blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf` | 24 | 24 | 24 | 0 | Full-page scan |
| 032 | `Bharti_Airtel_Q4_FY25_Financial_Results.pdf` | 23 | 23 | 23 | 23 | Full-page scan |
| 033 | `Asian_Hotels_East_Audited_FY26_Financial_Results.pdf` | 22 | 22 | 22 | 22 | Full-page scan |
| 034 | `Bharti_Airtel_Q4_FY26_Financial_Results.pdf` | 21 | 21 | 21 | 21 | Full-page scan |
| 035 | `Prodocs_Solutions_Limited_Audited_Financial_Results_FY2025-26.pdf` | 20 | 20 | 20 | 20 | Full-page scan |
| 036 | `Meso Private Limited.pdf` | 19 | 19 | 19 | 0 | Full-page scan |
| 037 | `Primo_Chemicals_Limited_Postal_Ballot_Notice_Financial_Disclosure_2026.pdf` | 19 | 19 | 19 | 19 | Full-page scan |
| 038 | `Nirmal_Bang_Epigral_Monthly_Research_May_2024.pdf` | 18 | 18 | 18 | 17 | Full-page scan |
| 039 | `Havells_India_Q4_FY25_Board_Outcome_Audited_Results.pdf` | 17 | 17 | 17 | 17 | Full-page scan |
| 040 | `AXISCADES_Consolidated_Financial_Results_Q2_FY25.pdf` | 16 | 16 | 16 | 16 | Full-page scan |
| 041 | `CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf` | 16 | 16 | 16 | 0 | Full-page scan |
| 042 | `ICICI_Lombard_FY25_Board_Outcome_Audited_Results.pdf` | 15 | 15 | 15 | 15 | Full-page scan |
| 043 | `AXISCADES_Integrated_Filing_Q3_FY25_Financial_Results.pdf` | 11 | 11 | 11 | 8 | Full-page scan |
| 044 | `Nuvama_V2_Retail_Company_Update_October_2024.pdf` | 11 | 11 | 11 | 10 | Full-page scan |
| 045 | `Shardul_Securities_Limited_Q1_FY27_Financial_Results.pdf` | 11 | 11 | 11 | 11 | Full-page scan |
| 046 | `AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf` | 9 | 9 | 9 | 9 | Full-page scan |
| 047 | `21STCENMGM_qr_29_07_2025_171051.pdf` | 7 | 7 | 7 | 7 | Full-page scan |
| 048 | `Newtrac_Foods_and_Beverages_Q1_FY27_Financial_Results.pdf` | 7 | 7 | 7 | 7 | Full-page scan |
| 049 | `Nirmal_Bang_ITD_Cementation_Company_Update_April_2024.pdf` | 5 | 5 | 5 | 4 | Full-page scan |
| 050 | `blobextra_ce38744b83cf_blobextra_for_the_year_2024_2025.pdf` | 4 | 4 | 4 | 4 | Full-page scan |
| 051 | `IEEMA_Industry_Overview_Apr-Jun_FY2024.pdf` | 10 | — | 8 | not counted | Mixed/partial candidate |
| 052 | `IEEMA_Industry_Overview_Apr-Dec_FY2023.pdf` | 10 | — | 8 | not counted | Mixed/partial candidate |
| 053 | `IEEMA_Industry_Overview_FY2022-23.pdf` | 9 | — | 7 | not counted | Mixed/partial candidate |
| 054 | `Ministry_of_Education_Budgeted_Expenditure_Analysis_2020-2022.pdf` | 132 | — | 1 | not counted | Mixed/partial candidate |
| 055 | `FIDC_20th_Annual_Report_2023-24.pdf` | 35 | — | 12 | not counted | Mixed/partial candidate |
| 056 | `IBAI_21st_Annual_Report_2023.pdf` | 57 | — | 22 | not counted | Mixed/partial candidate |
| 057 | `Sa-Dhan_Annual_Report_2020-21.pdf` | 56 | — | 2 | not counted | Mixed/partial candidate |
| 058 | `India_Tourism_Statistics_2021_Ministry_of_Tourism.pdf` | 248 | — | 1 | not counted | Mixed/partial candidate |
| 059 | `CropLife_India_Pesticide_Import_Position_Paper_2024.pdf` | 16 | — | 1 | not counted | Mixed/partial candidate |
| 060 | `Akshay_Urja_MNRE_Vol14_Issue1_2025.pdf` | 40 | — | 1 | not counted | Mixed/partial candidate |
| 061 | `Infomerics_Credit_Rating_Brochure_Nov2024.pdf` | 8 | — | 8 | not counted | Mixed/partial; all pages candidates |
| 062 | `IEEMA_Industry_Overview_Apr-Sep_FY2023-24.pdf` | 10 | — | 2 | not counted | Mixed/partial candidate |
| 063 | `Ministry_of_Power_Energy_Accounting_Guidelines_2025.pdf` | 23 | — | 7 | not counted | Mixed/partial candidate |
| 064 | `Steel_Exchange_India_Annual_Report_2019-20.pdf` | 118 | — | 4 | not counted | Mixed/partial candidate |
| 065 | `Steel_Exchange_India_Annual_Report_2025-26.pdf` | 165 | — | 1 | not counted | Mixed/partial candidate |
| 066 | `ANKITA_KNIT_WEAR_LIMITED__DRHP__2009.pdf` | 209 | — | 2 | not counted | Mixed/partial candidate |
| 067 | `EQUITAS_SMALL_FINANCE_BANK_LIMITED__FOD__2020.pdf` | 411 | — | 2 | not counted | Mixed/partial candidate |
| 068 | `INDO_THAI_SECURITIES_LIMITED__DRHP__2011.pdf` | 327 | — | 1 | not counted | Mixed/partial candidate |
| 069 | `SIGACHI_INDUSTRIES_LIMITED__RHP__2021.pdf` | 392 | — | 1 | not counted | Mixed/partial candidate |
| 070 | `8b90b9f3-76d2-4d18-ad1c-21b6d11fb727.pdf` | 118 | — | 1 | not counted | Mixed/partial candidate |
| 071 | `caaa82f9-e0e9-47ff-b31f-33801b06ff9f.pdf` | 185 | — | 3 | not counted | Mixed/partial candidate |
| 072 | `056_ACROPETAL_TECHNOLOGIES_LIMITED_FOD.pdf` | 306 | — | 2 | not counted | Mixed/partial candidate |
| 073 | `509762__3ed5c6d6-7e32-4f58-ad46-b1e484bcbd0f.pdf` | 3 | — | 3 | not counted | Mixed/partial; all pages candidates |
| 074 | `532700__300778df-eff5-4a1e-b248-8fff79ce17c5.pdf` | 7 | — | 4 | not counted | Mixed/partial candidate |
| 075 | `533192__d47508d9-0361-4664-847b-7d99c83b5272.pdf` | 3 | — | 2 | not counted | Mixed/partial candidate |
| 076 | `541703__87a196e6-2d5e-4831-b4a7-c999ba8742ea.pdf` | 3 | — | 3 | not counted | Mixed/partial; all pages candidates |
| 077 | `543233__b25a8485-9ce9-4763-bdf9-f878ef454dad.pdf` | 4 | — | 3 | not counted | Mixed/partial candidate |
| 078 | `543540__8e5be6d6-a7c0-4586-8101-84a4a4671f78.pdf` | 3 | — | 2 | not counted | Mixed/partial candidate |
| 079 | `543621__dd9e16e8-0bc2-4d0f-8ee9-600df2bff2b5.pdf` | 3 | — | 3 | not counted | Mixed/partial; all pages candidates |
| 080 | `544626__3c75ff40-37f2-4dee-ac5f-29de11b4ecfd.pdf` | 3 | — | 3 | not counted | Mixed/partial; all pages candidates |
| 081 | `104e37c6-5f6a-4614-a80f-60301a139f9c.pdf` | 11 | — | 1 | not counted | Mixed/partial candidate |
| 082 | `5baa1b96-a282-436b-817a-c1d232464e0b.pdf` | 11 | — | 2 | not counted | Mixed/partial candidate |
| 083 | `4e0aa144-abe5-4666-bab2-7f4bca64d634.pdf` | 7 | — | 1 | not counted | Mixed/partial candidate |
| 084 | `038_VIBRANT_GLOBAL_CAPITAL_LIMITED._FOD.pdf` | 263 | — | 1 | not counted | Mixed/partial candidate |
| 085 | `060_COFFEE_DAY_ENTERPRISES_LIMITED_DRHP.pdf` | 920 | — | 18 | not counted | Mixed/partial candidate |
| 086 | `061_NUZIVEEDU_SEEDS_LIMITED_DRHP.pdf` | 878 | — | 84 | not counted | Mixed/partial candidate |
| 087 | `133_S_CHAND_AND_COMPANY_LIMITED_DRHP.pdf` | 597 | — | 7 | not counted | Mixed/partial candidate |
| 088 | `141_HPL_ELECTRIC___POWER_LIMITED_FOD.pdf` | 469 | — | 1 | not counted | Mixed/partial candidate |
| 089 | `192_MAHINDRA_LOGISTICS_LIMITED_DRHP.pdf` | 562 | — | 4 | not counted | Mixed/partial candidate |
| 090 | `bse-one-day__500188__2026__d413963a-1759-4baa-bc3b-e46241042372.pdf` | 4 | — | 4 | not counted | Mixed/partial; all pages candidates |
| 091 | `bse-one-day__500330__2026__1593a02f-7ce7-492b-af7b-f5b51603cb39.pdf` | 5 | — | 2 | not counted | Mixed/partial candidate |
| 092 | `bse-one-day__522241__2026__792f7779-cef8-49f1-a704-6b457cc81311.pdf` | 75 | — | 74 | not counted | Mixed/partial candidate |
| 093 | `bse-one-day__539787__2026__1189a7e3-9a32-4ada-a96d-a74d5519adc7.pdf` | 14 | — | 8 | not counted | Mixed/partial candidate |
| 094 | `bse-one-day__539854__2026__1d8b905b-abc2-4527-ae0a-ac7b1a10fbeb.pdf` | 5 | — | 2 | not counted | Mixed/partial candidate |
| 095 | `bse-one-day__540726__2026__06d8fc46-4078-495c-939c-c0e8e022c016.pdf` | 8 | — | 1 | not counted | Mixed/partial candidate |
| 096 | `bse-one-day__543264__2026__6b26b4c1-d1b2-4efc-8619-ff640b03d708.pdf` | 47 | — | 38 | not counted | Mixed/partial candidate |
| 097 | `bse-one-day__544338__2026__65c1203e-4148-41e9-ba8f-499af4dbc0f3.pdf` | 19 | — | 8 | not counted | Mixed/partial candidate |
| 098 | `119_MANORAMA_INDUSTRIES_LIMITED_FOD.pdf` | 447 | — | 51 | not counted | Mixed/partial candidate |
| 099 | `184_SOFTTECH_ENGINEERS_LIMITED_FOD.pdf` | 418 | — | 38 | not counted | Mixed/partial candidate |
| 100 | `136_ROUTE_MOBILE_LIMITED_DRHP.pdf` | 504 | — | 47 | not counted | Mixed/partial candidate |

## Source and audit files

- `ranked_100_manifest.csv` records hashes, page counts, Blob locations, scan classification, and page-level OCR candidate counts and page numbers.
- `top_50_manifest.csv` remains the index for the preserved 50 fully scanned PDFs.
- `inventory.csv` summarizes page counts and OCR-candidate counts for all 100 current PDFs.
- `direct_pdf_links.csv` contains GitHub raw download links for all 100 current PDFs.
- The candidate PDFs were copied from `OCR/sources/industry_reports_additional_50`; its per-page source manifest and local visual review evidence remain in the parent workspace.
- The replaced ranks 051–100 remain recoverable from Git history before this update.

Only the 50 unverified mixed/partial folders were replaced. The original 50 fully scanned PDFs and their top-50 manifest were preserved.

# Financial OCR dataset: 100 ranked PDFs

This folder contains exactly 100 deduplicated financial PDFs. Entries 001-025 are verified full-page scanned PDFs; each page was checked for raster image coverage. Remaining entries are mixed/partial candidates. The weakest mixed files have been replaced with stronger full-page scans; the eight approved company PDFs remain included. The full-page scan threshold is at least 68% image-bounding-box coverage on every page, allowing white margins and OCR text overlays. Selectable OCR text is counted separately and does not disqualify an image-scanned page.

## Current dataset totals

| Measure | Result |
|---|---:|
| PDFs | 100 |
| Full-page scanned PDFs verified | 25 |
| Mixed/partial PDFs | 75 |
| Total PDF pages | 32,870 |
| Pages in full-page scanned PDFs | 1,933 |
| Candidate pages in mixed PDFs (prior heuristic) | 1,231 |
| Total file size | 857,801,357 bytes (0.858 GB; 0.799 GiB) |
| Full-scan target | 50 PDFs; current verified count 25 |

Mixed-document candidate counts are an earlier page-level image/sparse-text heuristic, not ground truth. Pages not flagged are not proven non-OCRable. For full-page scans, every page is image-backed; `ocr_text_layer_pages` records pages with selectable text so existing OCR layers are visible. No OCR engine was run as part of this dataset curation.

## Ranked document table

| Rank | PDF/document | Pages | Verified scanned pages | Mixed candidate pages (heuristic) | OCR text-layer pages | Type |
|---:|---|---:|---:|---:|---:|---|
| 001 | `Ministry of Petroleum and Natural Gas Annual Report 2023-24.pdf` | 680 | 680 | — | 0 | Full-page scan |
| 002 | `blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf` | 138 | 138 | — | 0 | Full-page scan |
| 003 | `blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf` | 138 | 138 | — | 0 | Full-page scan |
| 004 | `Automotive Component Manufacturers Association of India Annual Report 2021-22.pdf` | 112 | 112 | — | 0 | Full-page scan |
| 005 | `blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf` | 94 | 94 | — | 0 | Full-page scan |
| 006 | `20MICRONS_ar_2011.pdf` | 90 | 90 | — | 0 | Full-page scan |
| 007 | `blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf` | 88 | 88 | — | 0 | Full-page scan |
| 008 | `Indian Institute of Packaging Annual Report 2022-23.pdf` | 72 | 72 | — | 0 | Full-page scan |
| 009 | `Nova Iron & Steel Limited BSE Regulation 30 Financial Disclosure 2026.pdf` | 68 | 68 | — | 68 | Full-page scan |
| 010 | `shiv fabritex international pvt ltd.pdf` | 60 | 60 | — | 0 | Full-page scan |
| 011 | `Yugeri Marketing Private Limited.pdf` | 55 | 55 | — | 0 | Full-page scan |
| 012 | `Ministry of New and Renewable Energy Annual Report 2020-21 Chapters 8-10.pdf` | 45 | 45 | — | 0 | Full-page scan |
| 013 | `blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf` | 39 | 39 | — | 0 | Full-page scan |
| 014 | `blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf` | 36 | 36 | — | 0 | Full-page scan |
| 015 | `Gianna Agro Pvt. Ltd.pdf` | 31 | 31 | — | 0 | Full-page scan |
| 016 | `Suruchi Dairy & Dairy Products.pdf` | 28 | 28 | — | 0 | Full-page scan |
| 017 | `blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf` | 27 | 27 | — | 0 | Full-page scan |
| 018 | `blobextra_0e46676491d6_balance_sheet_2020_21.pdf` | 27 | 27 | — | 0 | Full-page scan |
| 019 | `Indian Tea Association Audited Accounts 2023.pdf` | 26 | 26 | — | 0 | Full-page scan |
| 020 | `blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf` | 24 | 24 | — | 0 | Full-page scan |
| 021 | `Meso Private Limited.pdf` | 19 | 19 | — | 0 | Full-page scan |
| 022 | `CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf` | 16 | 16 | — | 0 | Full-page scan |
| 023 | `AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf` | 9 | 9 | — | 9 | Full-page scan |
| 024 | `21STCENMGM_qr_29_07_2025_171051.pdf` | 7 | 7 | — | 7 | Full-page scan |
| 025 | `blobextra_ce38744b83cf_blobextra_for_the_year_2024_2025.pdf` | 4 | 4 | — | 4 | Full-page scan |
| 026 | `sebi_207_INTERGLOBE_AVIATION_LIMITED_RHP.pdf` | 519 | not fully verified | 274 | not audited | Mixed/partial |
| 027 | `sebi_210_INTERGLOBE_AVIATION_LIMITED_FOD.pdf` | 519 | not fully verified | 274 | not audited | Mixed/partial |
| 028 | `blob_008_008_tea_board_of_india__original_annual_accounts_2020_21.pdf` | 251 | not fully verified | 118 | not audited | Mixed/partial |
| 029 | `blobextra_f0d2442a79e3_IRIS_BUSINESS_SERVICES_LIMITED_FOD.pdf` | 384 | not fully verified | 89 | not audited | Mixed/partial |
| 030 | `blobextra_88844af589af_MAHINDRA_LOGISTICS_LIMITED_FOD.pdf` | 573 | not fully verified | 22 | not audited | Mixed/partial |
| 031 | `blobextra_d9f47ed8de3f_BSE_LIMITED_FOD.pdf` | 667 | not fully verified | 19 | not audited | Mixed/partial |
| 032 | `blobextra_d20cb6a9bf63_BSE_LIMITED_RHP.pdf` | 659 | not fully verified | 19 | not audited | Mixed/partial |
| 033 | `BANDHAN_BANK_LIMITED_DRHP.pdf` | 482 | not fully verified | 17 | not audited | Mixed/partial |
| 034 | `BANDHAN_BANK_LIMITED_RHP.pdf` | 559 | not fully verified | 15 | not audited | Mixed/partial |
| 035 | `blobextra_09824b16d8fb_BANDHAN_BANK_LIMITED_FOD.pdf` | 559 | not fully verified | 15 | not audited | Mixed/partial |
| 036 | `blobextra_d9fa75cc7ef7_ENDURANCE_TECHNOLOGIES_LIMITED_RHP.pdf` | 637 | not fully verified | 15 | not audited | Mixed/partial |
| 037 | `sebi_098_V-MART_RETAIL_LIMITED_FOD.pdf` | 437 | not fully verified | 14 | not audited | Mixed/partial |
| 038 | `sebi_156_TIJARIA_POLYPIPES_LIMITED_FOD.pdf` | 341 | not fully verified | 13 | not audited | Mixed/partial |
| 039 | `blobextra_bd2e3115cf0e_THETA_PHARMACEUTICALS_LIMITED_RHP.pdf` | 247 | not fully verified | 13 | not audited | Mixed/partial |
| 040 | `sebi_111_KRIDHAN_INFRA_LIMITED_RHP.pdf` | 314 | not fully verified | 11 | not audited | Mixed/partial |
| 041 | `sebi_110_KRIDHAN_INFRA_LIMITED_FOD.pdf` | 312 | not fully verified | 11 | not audited | Mixed/partial |
| 042 | `sebi_065_FINEOTEX_CHEMICAL_LIMITED_FOD.pdf` | 256 | not fully verified | 11 | not audited | Mixed/partial |
| 043 | `sebi_070_FINEOTEX_CHEMICAL_LIMITED_RHP.pdf` | 256 | not fully verified | 11 | not audited | Mixed/partial |
| 044 | `blob_051_051_sa-dhan__original_annual_report_2021_22.pdf` | 69 | not fully verified | 11 | not audited | Mixed/partial |
| 045 | `sebi_134_SETUBANDHAN_INFRASTRUCTURE_LIMITED_FOD.pdf` | 359 | not fully verified | 10 | not audited | Mixed/partial |
| 046 | `blob_053_053_sa-dhan__original_annual_report_2023_24.pdf` | 65 | not fully verified | 10 | not audited | Mixed/partial |
| 047 | `blob_052_052_sa-dhan__original_annual_report_2022_23.pdf` | 58 | not fully verified | 10 | not audited | Mixed/partial |
| 048 | `blobextra_df1e1e16046d_BF_INDUSTRIAL_TECHNOLOGY___SOLUTIONS_LIMITED_FOD.pdf` | 367 | not fully verified | 9 | not audited | Mixed/partial |
| 049 | `sebi_151_SETUBANDHAN_INFRASTRUCTURE_LIMITED_RHP.pdf` | 359 | not fully verified | 9 | not audited | Mixed/partial |
| 050 | `blob_043_043_department_of_revenue__original_statistical_report_on_7_years_of_gst.pdf` | 65 | not fully verified | 9 | not audited | Mixed/partial |
| 051 | `BENARA_BEARINGS_AND_PISTONS_LIMITED_FOD.pdf` | 481 | not fully verified | 8 | not audited | Mixed/partial |
| 052 | `blobextra_fe66f1c6bfb0_BENARA_BEARINGS_AND_PISTONS_LIMITED_RHP.pdf` | 481 | not fully verified | 8 | not audited | Mixed/partial |
| 053 | `CAPRICORN_FOOD_PRODUCTS_INDIA_LIMITED_DRHP.pdf` | 446 | not fully verified | 8 | not audited | Mixed/partial |
| 054 | `sebi_053_GB_GLOBAL_LIMITED_FOD.pdf` | 383 | not fully verified | 8 | not audited | Mixed/partial |
| 055 | `sebi_059_GB_GLOBAL_LIMITED_RHP.pdf` | 382 | not fully verified | 8 | not audited | Mixed/partial |
| 056 | `blob_030_030_niti_aayog__original_aim__niti_ipe_white_paper_on_blended_financing.pdf` | 48 | not fully verified | 7 | not audited | Mixed/partial |
| 057 | `blobextra_313b997b13a8_BOMBAY_SUPER_HYBRID_SEEDS_LIMITED_FOD.pdf` | 408 | not fully verified | 6 | not audited | Mixed/partial |
| 058 | `ZOTA_HEALTH_CARE_LIMITED_FOD.pdf` | 461 | not fully verified | 5 | not audited | Mixed/partial |
| 059 | `ZOTA_HEALTH_CARE_LIMITED_RHP.pdf` | 461 | not fully verified | 5 | not audited | Mixed/partial |
| 060 | `BOHRA_INDUSTRIES_LIMITED_RHP.pdf` | 435 | not fully verified | 5 | not audited | Mixed/partial |
| 061 | `BOHRA_INDUSTRIES_LIMITED_FOD.pdf` | 434 | not fully verified | 5 | not audited | Mixed/partial |
| 062 | `blobextra_499fc5d1931e_KHADIM_INDIA_LIMITED_FOD.pdf` | 409 | not fully verified | 5 | not audited | Mixed/partial |
| 063 | `blobextra_fbdca9d53696_KHADIM_INDIA_LIMITED_RHP.pdf` | 409 | not fully verified | 5 | not audited | Mixed/partial |
| 064 | `blob_112_112_life_insurance_council__original_annual_report_2021_2022.pdf` | 740 | not fully verified | 5 | not audited | Mixed/partial |
| 065 | `blobextra_f102514d4612_INVENTURE_GROWTH_AND_SECURITIES_LIMITED_RHP.pdf` | 397 | not fully verified | 5 | not audited | Mixed/partial |
| 066 | `blobextra_c80e0dc1cf2c_ACROPETAL_TECHNOLOGIES_LIMITED_RHP.pdf` | 306 | not fully verified | 5 | not audited | Mixed/partial |
| 067 | `blobextra_7e12da3324c4_GENERAL_INSURANCE_CORPORATION_OF_INDIA_FOD.pdf` | 570 | not fully verified | 4 | not audited | Mixed/partial |
| 068 | `blobextra_77ca65ea5335_MAHINDRA_LOGISTICS_LIMITED_DRHP.pdf` | 562 | not fully verified | 4 | not audited | Mixed/partial |
| 069 | `blobextra_a83b3bdbf259_BHARAT_WIRE_ROPES_LIMITED_DRHP.pdf` | 437 | not fully verified | 4 | not audited | Mixed/partial |
| 070 | `blobextra_490216b1e744_DEEP_POLYMERS_LIMITED_FOD.pdf` | 418 | not fully verified | 4 | not audited | Mixed/partial |
| 071 | `INNOVATIVE_TYRES_&_TUBES_LIMITED_FOD.pdf` | 416 | not fully verified | 4 | not audited | Mixed/partial |
| 072 | `INNOVATIVE_TYRES_&_TUBES_LIMITED_RHP.pdf` | 416 | not fully verified | 4 | not audited | Mixed/partial |
| 073 | `blobextra_d6150fcf3b8f_HPL_ELECTRIC___POWER_LIMITED_RHP.pdf` | 469 | not fully verified | 4 | not audited | Mixed/partial |
| 074 | `sebi_081_MOMAI_APPARELS_LIMITED_FOD.pdf` | 421 | not fully verified | 4 | not audited | Mixed/partial |
| 075 | `blobextra_f0d370970dcc_UJJIVAN_FINANCIAL_SERVICES_LIMITED_DRHP.pdf` | 391 | not fully verified | 4 | not audited | Mixed/partial |
| 076 | `AU_SMALL_FINANCE_BANK_LIMITED_FOD.pdf` | 515 | not fully verified | 3 | not audited | Mixed/partial |
| 077 | `GARDEN_REACH_SHIPBUILDERS_&_ENGINEERS_LIMITED_RHP.pdf` | 515 | not fully verified | 3 | not audited | Mixed/partial |
| 078 | `blobextra_2ecb0157f400_GARDEN_REACH_SHIPBUILDERS_&_ENGINEERS_LIMITED_FOD.pdf` | 513 | not fully verified | 3 | not audited | Mixed/partial |
| 079 | `blobextra_e2f9f54a5521_AU_SMALL_FINANCE_BANK_LIMITED_RHP.pdf` | 511 | not fully verified | 3 | not audited | Mixed/partial |
| 080 | `blobextra_78f1a0016f85_ANGEL_ONE_LIMITED_DRHP.pdf` | 470 | not fully verified | 3 | not audited | Mixed/partial |
| 081 | `ASTRON_PAPER_&_BOARD_MILL_LIMITED_FOD.pdf` | 469 | not fully verified | 3 | not audited | Mixed/partial |
| 082 | `ASTRON_PAPER_&_BOARD_MILL_LIMITED_RHP.pdf` | 468 | not fully verified | 3 | not audited | Mixed/partial |
| 083 | `blobextra_d2e1e549bbe4_SREI_EQUIPMENT_FINANCE_LIMITED_DRHP.pdf` | 465 | not fully verified | 3 | not audited | Mixed/partial |
| 084 | `AAVAS_FINANCIERS_LIMITED_DRHP.pdf` | 458 | not fully verified | 3 | not audited | Mixed/partial |
| 085 | `CAPACIT'E_INFRAPROJECTS_LIMITED_FOD.pdf` | 456 | not fully verified | 3 | not audited | Mixed/partial |
| 086 | `blobextra_c38f7d5bc70e_CAPACIT_E_INFRAPROJECTS_LIMITED_RHP.pdf` | 455 | not fully verified | 3 | not audited | Mixed/partial |
| 087 | `CAPACIT'E_INFRAPROJECTS_LIMITED_DRHP.pdf` | 454 | not fully verified | 3 | not audited | Mixed/partial |
| 088 | `FUTURE_SUPPLY_CHAIN_SOLUTIONS_LIMITED_RHP.pdf` | 428 | not fully verified | 3 | not audited | Mixed/partial |
| 089 | `SIDDHARTH_EDUCATION_SERVICES_LIMITED_RHP.pdf` | 409 | not fully verified | 3 | not audited | Mixed/partial |
| 090 | `blobextra_ff2fa3432967_KHADIM_INDIA_LIMITED_DRHP.pdf` | 399 | not fully verified | 3 | not audited | Mixed/partial |
| 091 | `blobextra_d461d0d867e9_AKASH_INFRA-PROJECTS_LIMITED_FOD.pdf` | 322 | not fully verified | 3 | not audited | Mixed/partial |
| 092 | `blob_006_006_tea_board_of_india__original_annual_accounts_2021_22.pdf` | 252 | not fully verified | 3 | not audited | Mixed/partial |
| 093 | `blob_017_017_department_of_financial_services__original_annual_report_2022_23.pdf` | 39 | not fully verified | 3 | not audited | Mixed/partial |
| 094 | `blobextra_79cb0aa7c9fa_PSP_PROJECTS_LIMITED_FOD.pdf` | 487 | not fully verified | 2 | not audited | Mixed/partial |
| 095 | `blobextra_653619a90ef7_AMBER_ENTERPRISES_INDIA_LIMITED_DRHP.pdf` | 483 | not fully verified | 2 | not audited | Mixed/partial |
| 096 | `COCHIN_SHIPYARD_LIMITED_FOD.pdf` | 483 | not fully verified | 2 | not audited | Mixed/partial |
| 097 | `ICICI_SECURITIES_LIMITED_DRHP.pdf` | 460 | not fully verified | 2 | not audited | Mixed/partial |
| 098 | `blobextra_d77802b199ca_GALAXY_SURFACTANTS_LTD_FOD.pdf` | 447 | not fully verified | 2 | not audited | Mixed/partial |
| 099 | `GALAXY_SURFACTANTS_LTD_RHP.pdf` | 445 | not fully verified | 2 | not audited | Mixed/partial |
| 100 | `blobextra_627d6b00b51d_AVANA_LOGISTEK_LIMITED_DRHP.pdf` | 439 | not fully verified | 2 | not audited | Mixed/partial |

## Source and audit files

- `ranked_100_manifest.csv` records hashes, page counts, source Blob paths where available, and page-level scan evidence for full-scan entries.
- `top_50_manifest.csv` indexes the first 50 ranked PDFs without duplicating the files.
- Blob search logs and candidate evidence are retained under the local `OCR/sources/blob_search_agent_*` folders.

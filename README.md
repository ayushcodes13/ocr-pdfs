# Financial OCR dataset: 100 ranked PDFs

This folder contains exactly 100 deduplicated financial PDFs. Entries 001-040 are verified full-page scanned PDFs; every page was checked for raster image coverage. Remaining entries are mixed/partial candidates. The eight approved company PDFs remain included. Full-page scan coverage is at least 68% of the page bounding box on every page; selectable OCR text is counted separately.

## Current dataset totals

| Measure | Result |
|---|---:|
| PDFs | 100 |
| Full-page scanned PDFs verified | 40 |
| Mixed/partial PDFs | 60 |
| Total PDF pages | 26,207 |
| Pages in full-page scanned PDFs | 2,440 |
| Candidate pages in mixed PDFs (prior heuristic) | 1,193 |
| Total file size | 885,353,428 bytes (0.885 GB; 0.825 GiB) |
| Full-scan target | 50 PDFs; current verified count 40 |

Mixed-document candidate counts are an earlier image/sparse-text heuristic, not ground truth; pages not flagged are not proven non-OCRable. For full-page scans, every page is image-backed; `ocr_text_layer_pages` records pages with selectable text. No OCR engine was run as part of curation. Tandhan p13 is sideways and may stress OCR orientation handling; p27 is nearly blank.

## Ranked document table

| Rank | PDF/document | Pages | Verified scanned pages | Mixed candidate pages (heuristic) | OCR text-layer pages | Type |
|---:|---|---:|---:|---:|---:|---|
| 001 | `annual_report_2023_24.pdf` | 680 | 680 | — | 0 | Full-page scan |
| 002 | `Nureca_Limited_Annual_Report_FY2025-26.pdf` | 181 | 181 | — | 180 | Full-page scan |
| 003 | `blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf` | 138 | 138 | — | 0 | Full-page scan |
| 004 | `blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf` | 138 | 138 | — | 0 | Full-page scan |
| 005 | `blob_185_185_automotive_component_manufacturers_association_of_india__acma__original_annual_report_2021_22.pdf` | 112 | 112 | — | 0 | Full-page scan |
| 006 | `blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf` | 94 | 94 | — | 0 | Full-page scan |
| 007 | `20MICRONS_ar_2011.pdf` | 90 | 90 | — | 0 | Full-page scan |
| 008 | `blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf` | 88 | 88 | — | 0 | Full-page scan |
| 009 | `blob_050_050_indian_institute_of_packaging__iip___semi-private__original_annual_report_2022_23.pdf` | 72 | 72 | — | 0 | Full-page scan |
| 010 | `Nova_Iron_and_Steel_Limited_BSE_Regulation_30_Financial_Disclosure_2026.pdf` | 68 | 68 | — | 68 | Full-page scan |
| 011 | `shiv fabritex international pvt ltd.pdf` | 60 | 60 | — | 0 | Full-page scan |
| 012 | `Yugeri Marketing Private Limited.pdf` | 55 | 55 | — | 0 | Full-page scan |
| 013 | `annual_report_2020_21_chapter_8_10.pdf` | 45 | 45 | — | 0 | Full-page scan |
| 014 | `FIDC_19th_Annual_Report_2022-23.pdf` | 40 | 40 | — | 36 | Full-page scan |
| 015 | `blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf` | 39 | 39 | — | 0 | Full-page scan |
| 016 | `blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf` | 36 | 36 | — | 0 | Full-page scan |
| 017 | `Edelweiss_Suraj_Estate_Company_Update_July_2024.pdf` | 35 | 35 | — | 34 | Full-page scan |
| 018 | `Wipro_Q4_FY25_Board_Outcome_Financial_Results.pdf` | 35 | 35 | — | 35 | Full-page scan |
| 019 | `Tata_Steel_FY25_Board_Outcome_Audited_Financial_Results.pdf` | 34 | 34 | — | 34 | Full-page scan |
| 020 | `Gianna Agro Pvt. Ltd.pdf` | 31 | 31 | — | 0 | Full-page scan |
| 021 | `Suruchi Dairy & Dairy Products.pdf` | 28 | 28 | — | 0 | Full-page scan |
| 022 | `Tandhan_Industries_Monitoring_Agency_Report_Q4_FY26.pdf` | 27 | 27 | — | 26 | Full-page scan |
| 023 | `blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf` | 27 | 27 | — | 0 | Full-page scan |
| 024 | `blobextra_0e46676491d6_balance_sheet_2020_21.pdf` | 27 | 27 | — | 0 | Full-page scan |
| 025 | `blobextra_a79f601cfc45_audited_accounts_as_on_31st_march_2023.pdf` | 26 | 26 | — | 0 | Full-page scan |
| 026 | `PVP_Ventures_Limited_Debenture_and_Repayment_Schedule_Disclosure.pdf` | 26 | 26 | — | 26 | Full-page scan |
| 027 | `blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf` | 24 | 24 | — | 0 | Full-page scan |
| 028 | `Bharti_Airtel_Q4_FY25_Financial_Results.pdf` | 23 | 23 | — | 23 | Full-page scan |
| 029 | `Bharti_Airtel_Q4_FY26_Financial_Results.pdf` | 21 | 21 | — | 21 | Full-page scan |
| 030 | `Meso Private Limited.pdf` | 19 | 19 | — | 0 | Full-page scan |
| 031 | `Primo_Chemicals_Limited_Postal_Ballot_Notice_Financial_Disclosure_2026.pdf` | 19 | 19 | — | 19 | Full-page scan |
| 032 | `Nirmal_Bang_Epigral_Monthly_Research_May_2024.pdf` | 18 | 18 | — | 17 | Full-page scan |
| 033 | `Havells_India_Q4_FY25_Board_Outcome_Audited_Results.pdf` | 17 | 17 | — | 17 | Full-page scan |
| 034 | `CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf` | 16 | 16 | — | 0 | Full-page scan |
| 035 | `ICICI_Lombard_FY25_Board_Outcome_Audited_Results.pdf` | 15 | 15 | — | 15 | Full-page scan |
| 036 | `Nuvama_V2_Retail_Company_Update_October_2024.pdf` | 11 | 11 | — | 10 | Full-page scan |
| 037 | `AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf` | 9 | 9 | — | 9 | Full-page scan |
| 038 | `21STCENMGM_qr_29_07_2025_171051.pdf` | 7 | 7 | — | 7 | Full-page scan |
| 039 | `Nirmal_Bang_ITD_Cementation_Company_Update_April_2024.pdf` | 5 | 5 | — | 4 | Full-page scan |
| 040 | `blobextra_ce38744b83cf_blobextra_for_the_year_2024_2025.pdf` | 4 | 4 | — | 4 | Full-page scan |
| 041 | `sebi_207_INTERGLOBE_AVIATION_LIMITED_RHP.pdf` | 519 | not fully verified | 274 | not audited | Mixed/partial |
| 042 | `sebi_210_INTERGLOBE_AVIATION_LIMITED_FOD.pdf` | 519 | not fully verified | 274 | not audited | Mixed/partial |
| 043 | `blob_008_008_tea_board_of_india__original_annual_accounts_2020_21.pdf` | 251 | not fully verified | 118 | not audited | Mixed/partial |
| 044 | `blobextra_f0d2442a79e3_IRIS_BUSINESS_SERVICES_LIMITED_FOD.pdf` | 384 | not fully verified | 89 | not audited | Mixed/partial |
| 045 | `blobextra_88844af589af_MAHINDRA_LOGISTICS_LIMITED_FOD.pdf` | 573 | not fully verified | 22 | not audited | Mixed/partial |
| 046 | `blobextra_d9f47ed8de3f_BSE_LIMITED_FOD.pdf` | 667 | not fully verified | 19 | not audited | Mixed/partial |
| 047 | `blobextra_d20cb6a9bf63_BSE_LIMITED_RHP.pdf` | 659 | not fully verified | 19 | not audited | Mixed/partial |
| 048 | `BANDHAN_BANK_LIMITED_DRHP.pdf` | 482 | not fully verified | 17 | not audited | Mixed/partial |
| 049 | `BANDHAN_BANK_LIMITED_RHP.pdf` | 559 | not fully verified | 15 | not audited | Mixed/partial |
| 050 | `blobextra_09824b16d8fb_BANDHAN_BANK_LIMITED_FOD.pdf` | 559 | not fully verified | 15 | not audited | Mixed/partial |
| 051 | `blobextra_d9fa75cc7ef7_ENDURANCE_TECHNOLOGIES_LIMITED_RHP.pdf` | 637 | not fully verified | 15 | not audited | Mixed/partial |
| 052 | `sebi_098_V-MART_RETAIL_LIMITED_FOD.pdf` | 437 | not fully verified | 14 | not audited | Mixed/partial |
| 053 | `sebi_156_TIJARIA_POLYPIPES_LIMITED_FOD.pdf` | 341 | not fully verified | 13 | not audited | Mixed/partial |
| 054 | `blobextra_bd2e3115cf0e_THETA_PHARMACEUTICALS_LIMITED_RHP.pdf` | 247 | not fully verified | 13 | not audited | Mixed/partial |
| 055 | `sebi_111_KRIDHAN_INFRA_LIMITED_RHP.pdf` | 314 | not fully verified | 11 | not audited | Mixed/partial |
| 056 | `sebi_110_KRIDHAN_INFRA_LIMITED_FOD.pdf` | 312 | not fully verified | 11 | not audited | Mixed/partial |
| 057 | `sebi_065_FINEOTEX_CHEMICAL_LIMITED_FOD.pdf` | 256 | not fully verified | 11 | not audited | Mixed/partial |
| 058 | `sebi_070_FINEOTEX_CHEMICAL_LIMITED_RHP.pdf` | 256 | not fully verified | 11 | not audited | Mixed/partial |
| 059 | `blob_051_051_sa-dhan__original_annual_report_2021_22.pdf` | 69 | not fully verified | 11 | not audited | Mixed/partial |
| 060 | `sebi_134_SETUBANDHAN_INFRASTRUCTURE_LIMITED_FOD.pdf` | 359 | not fully verified | 10 | not audited | Mixed/partial |
| 061 | `blob_053_053_sa-dhan__original_annual_report_2023_24.pdf` | 65 | not fully verified | 10 | not audited | Mixed/partial |
| 062 | `blob_052_052_sa-dhan__original_annual_report_2022_23.pdf` | 58 | not fully verified | 10 | not audited | Mixed/partial |
| 063 | `blobextra_df1e1e16046d_BF_INDUSTRIAL_TECHNOLOGY___SOLUTIONS_LIMITED_FOD.pdf` | 367 | not fully verified | 9 | not audited | Mixed/partial |
| 064 | `sebi_151_SETUBANDHAN_INFRASTRUCTURE_LIMITED_RHP.pdf` | 359 | not fully verified | 9 | not audited | Mixed/partial |
| 065 | `blob_043_043_department_of_revenue__original_statistical_report_on_7_years_of_gst.pdf` | 65 | not fully verified | 9 | not audited | Mixed/partial |
| 066 | `BENARA_BEARINGS_AND_PISTONS_LIMITED_FOD.pdf` | 481 | not fully verified | 8 | not audited | Mixed/partial |
| 067 | `blobextra_fe66f1c6bfb0_BENARA_BEARINGS_AND_PISTONS_LIMITED_RHP.pdf` | 481 | not fully verified | 8 | not audited | Mixed/partial |
| 068 | `CAPRICORN_FOOD_PRODUCTS_INDIA_LIMITED_DRHP.pdf` | 446 | not fully verified | 8 | not audited | Mixed/partial |
| 069 | `sebi_053_GB_GLOBAL_LIMITED_FOD.pdf` | 383 | not fully verified | 8 | not audited | Mixed/partial |
| 070 | `sebi_059_GB_GLOBAL_LIMITED_RHP.pdf` | 382 | not fully verified | 8 | not audited | Mixed/partial |
| 071 | `blob_030_030_niti_aayog__original_aim__niti_ipe_white_paper_on_blended_financing.pdf` | 48 | not fully verified | 7 | not audited | Mixed/partial |
| 072 | `blobextra_313b997b13a8_BOMBAY_SUPER_HYBRID_SEEDS_LIMITED_FOD.pdf` | 408 | not fully verified | 6 | not audited | Mixed/partial |
| 073 | `ZOTA_HEALTH_CARE_LIMITED_FOD.pdf` | 461 | not fully verified | 5 | not audited | Mixed/partial |
| 074 | `ZOTA_HEALTH_CARE_LIMITED_RHP.pdf` | 461 | not fully verified | 5 | not audited | Mixed/partial |
| 075 | `BOHRA_INDUSTRIES_LIMITED_RHP.pdf` | 435 | not fully verified | 5 | not audited | Mixed/partial |
| 076 | `BOHRA_INDUSTRIES_LIMITED_FOD.pdf` | 434 | not fully verified | 5 | not audited | Mixed/partial |
| 077 | `blobextra_499fc5d1931e_KHADIM_INDIA_LIMITED_FOD.pdf` | 409 | not fully verified | 5 | not audited | Mixed/partial |
| 078 | `blobextra_fbdca9d53696_KHADIM_INDIA_LIMITED_RHP.pdf` | 409 | not fully verified | 5 | not audited | Mixed/partial |
| 079 | `blob_112_112_life_insurance_council__original_annual_report_2021_2022.pdf` | 740 | not fully verified | 5 | not audited | Mixed/partial |
| 080 | `blobextra_f102514d4612_INVENTURE_GROWTH_AND_SECURITIES_LIMITED_RHP.pdf` | 397 | not fully verified | 5 | not audited | Mixed/partial |
| 081 | `blobextra_c80e0dc1cf2c_ACROPETAL_TECHNOLOGIES_LIMITED_RHP.pdf` | 306 | not fully verified | 5 | not audited | Mixed/partial |
| 082 | `blobextra_7e12da3324c4_GENERAL_INSURANCE_CORPORATION_OF_INDIA_FOD.pdf` | 570 | not fully verified | 4 | not audited | Mixed/partial |
| 083 | `blobextra_77ca65ea5335_MAHINDRA_LOGISTICS_LIMITED_DRHP.pdf` | 562 | not fully verified | 4 | not audited | Mixed/partial |
| 084 | `blobextra_a83b3bdbf259_BHARAT_WIRE_ROPES_LIMITED_DRHP.pdf` | 437 | not fully verified | 4 | not audited | Mixed/partial |
| 085 | `blobextra_490216b1e744_DEEP_POLYMERS_LIMITED_FOD.pdf` | 418 | not fully verified | 4 | not audited | Mixed/partial |
| 086 | `INNOVATIVE_TYRES_&_TUBES_LIMITED_FOD.pdf` | 416 | not fully verified | 4 | not audited | Mixed/partial |
| 087 | `INNOVATIVE_TYRES_&_TUBES_LIMITED_RHP.pdf` | 416 | not fully verified | 4 | not audited | Mixed/partial |
| 088 | `blobextra_d6150fcf3b8f_HPL_ELECTRIC___POWER_LIMITED_RHP.pdf` | 469 | not fully verified | 4 | not audited | Mixed/partial |
| 089 | `sebi_081_MOMAI_APPARELS_LIMITED_FOD.pdf` | 421 | not fully verified | 4 | not audited | Mixed/partial |
| 090 | `blobextra_f0d370970dcc_UJJIVAN_FINANCIAL_SERVICES_LIMITED_DRHP.pdf` | 391 | not fully verified | 4 | not audited | Mixed/partial |
| 091 | `AAVAS_FINANCIERS_LIMITED_DRHP.pdf` | 458 | not fully verified | 3 | not audited | Mixed/partial |
| 092 | `CAPACIT'E_INFRAPROJECTS_LIMITED_FOD.pdf` | 456 | not fully verified | 3 | not audited | Mixed/partial |
| 093 | `blobextra_c38f7d5bc70e_CAPACIT_E_INFRAPROJECTS_LIMITED_RHP.pdf` | 455 | not fully verified | 3 | not audited | Mixed/partial |
| 094 | `CAPACIT'E_INFRAPROJECTS_LIMITED_DRHP.pdf` | 454 | not fully verified | 3 | not audited | Mixed/partial |
| 095 | `FUTURE_SUPPLY_CHAIN_SOLUTIONS_LIMITED_RHP.pdf` | 428 | not fully verified | 3 | not audited | Mixed/partial |
| 096 | `SIDDHARTH_EDUCATION_SERVICES_LIMITED_RHP.pdf` | 409 | not fully verified | 3 | not audited | Mixed/partial |
| 097 | `blobextra_ff2fa3432967_KHADIM_INDIA_LIMITED_DRHP.pdf` | 399 | not fully verified | 3 | not audited | Mixed/partial |
| 098 | `blobextra_d461d0d867e9_AKASH_INFRA-PROJECTS_LIMITED_FOD.pdf` | 322 | not fully verified | 3 | not audited | Mixed/partial |
| 099 | `blob_006_006_tea_board_of_india__original_annual_accounts_2021_22.pdf` | 252 | not fully verified | 3 | not audited | Mixed/partial |
| 100 | `blob_017_017_department_of_financial_services__original_annual_report_2022_23.pdf` | 39 | not fully verified | 3 | not audited | Mixed/partial |

## Source and audit files

- `ranked_100_manifest.csv` records hashes, page counts, Blob locations, source URLs where verified, provenance notes, and scan coverage.
- `top_50_manifest.csv` indexes the first 50 ranked PDFs without duplicating files.
- `direct_pdf_links.csv` contains raw GitHub download URLs.
- Blob search reports and candidate evidence are retained in the local `OCR/sources/blob_search_agent_*` folders.

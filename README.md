# Financial OCR candidate dataset: ranked 100 PDFs

This repository contains one PDF in each serial-numbered folder (`001__...` through `100__...`). Ranking and page counts are verified against the canonical dataset used for the Bynd Chat OCR stress-test preparation. The first 50 documents are the top-50 subset of this same ranked list. See [`top_50_inventory.csv`](top_50_inventory.csv) for that subset and [`inventory.csv`](inventory.csv) for all 100 PDFs.

## Dataset totals

| Measure | Result |
|---|---:|
| PDFs | 100 |
| Total PDF pages | 37,600 |
| Likely OCR-candidate pages | 1,962 |
| Pages not flagged as OCR candidates | 35,638 |
| PDFs with candidate signal on every page | 12 |
| PDFs with mixed/partial candidate signal | 88 |
| Total file size | 827,591,961 bytes (0.828 GB; 0.771 GiB) |
| Top 50 subset | 50 PDFs; 16,390 pages; 1,823 likely OCR-candidate pages |

### How to read the OCR page counts

“Likely OCR-candidate” means the existing page-level audit found image-backed page content with sparse selectable text, a signal that OCR may be useful. It does not prove a physical scan, OCR failure, or that fresh OCR is required. “Pages not flagged as OCR candidates” is the remaining page count; those pages may be native text or already have a text layer. The available audit cannot establish that any page is impossible to OCR, so the 35,638 pages not flagged should not be interpreted as truly non-OCRable.

The rank order uses likely OCR-candidate page count (more candidate pages ranks higher), with the finance-only relevance review used to keep the dataset financially focused. The score is test-set suitability, not a quality score for OCR output. `inventory.csv` contains the serial, folder, original PDF name, page counts, candidate counts, candidate fraction, page-mix label, SHA-256, byte size, and repository path for each document.

## Per-PDF inventory

| Rank | Folder / PDF name | Total pages | Likely OCR-candidate pages | Not flagged as candidates | Candidate mix |
|---:|---|---:|---:|---:|---|
| 001 | `001__sebi_207_INTERGLOBE_AVIATION_LIMITED_RHP` / `sebi_207_INTERGLOBE_AVIATION_LIMITED_RHP.pdf` | 519 | 274 | 245 | Mixed/partial |
| 002 | `002__sebi_210_INTERGLOBE_AVIATION_LIMITED_FOD` / `sebi_210_INTERGLOBE_AVIATION_LIMITED_FOD.pdf` | 519 | 274 | 245 | Mixed/partial |
| 003 | `003__blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23` / `blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf` | 138 | 138 | 0 | All pages |
| 004 | `004__blob_029_029_department_of_science_and_technology__original_budget_2021_22` / `blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf` | 138 | 138 | 0 | All pages |
| 005 | `005__blob_008_008_tea_board_of_india__original_annual_accounts_2020_21` / `blob_008_008_tea_board_of_india__original_annual_accounts_2020_21.pdf` | 251 | 118 | 133 | Mixed/partial |
| 006 | `006__blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25` / `blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf` | 94 | 94 | 0 | All pages |
| 007 | `007__20MICRONS_ar_2011` / `20MICRONS_ar_2011.pdf` | 90 | 90 | 0 | All pages |
| 008 | `008__blobextra_f0d2442a79e3_IRIS_BUSINESS_SERVICES_LIMITED_FOD` / `blobextra_f0d2442a79e3_IRIS_BUSINESS_SERVICES_LIMITED_FOD.pdf` | 384 | 89 | 295 | Mixed/partial |
| 009 | `009__blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23` / `blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf` | 88 | 88 | 0 | All pages |
| 010 | `010__blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22` / `blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf` | 39 | 39 | 0 | All pages |
| 011 | `011__blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case` / `blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf` | 36 | 36 | 0 | All pages |
| 012 | `012__blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24` / `blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf` | 27 | 27 | 0 | All pages |
| 013 | `013__blobextra_0e46676491d6_balance_sheet_2020_21` / `blobextra_0e46676491d6_balance_sheet_2020_21.pdf` | 27 | 27 | 0 | All pages |
| 014 | `014__blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021` / `blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf` | 24 | 24 | 0 | All pages |
| 015 | `015__blobextra_88844af589af_MAHINDRA_LOGISTICS_LIMITED_FOD` / `blobextra_88844af589af_MAHINDRA_LOGISTICS_LIMITED_FOD.pdf` | 573 | 22 | 551 | Mixed/partial |
| 016 | `016__blobextra_d9f47ed8de3f_BSE_LIMITED_FOD` / `blobextra_d9f47ed8de3f_BSE_LIMITED_FOD.pdf` | 667 | 19 | 648 | Mixed/partial |
| 017 | `017__blobextra_d20cb6a9bf63_BSE_LIMITED_RHP` / `blobextra_d20cb6a9bf63_BSE_LIMITED_RHP.pdf` | 659 | 19 | 640 | Mixed/partial |
| 018 | `018__BANDHAN_BANK_LIMITED_DRHP` / `BANDHAN_BANK_LIMITED_DRHP.pdf` | 482 | 17 | 465 | Mixed/partial |
| 019 | `019__BANDHAN_BANK_LIMITED_RHP` / `BANDHAN_BANK_LIMITED_RHP.pdf` | 559 | 15 | 544 | Mixed/partial |
| 020 | `020__blobextra_09824b16d8fb_BANDHAN_BANK_LIMITED_FOD` / `blobextra_09824b16d8fb_BANDHAN_BANK_LIMITED_FOD.pdf` | 559 | 15 | 544 | Mixed/partial |
| 021 | `021__blobextra_d9fa75cc7ef7_ENDURANCE_TECHNOLOGIES_LIMITED_RHP` / `blobextra_d9fa75cc7ef7_ENDURANCE_TECHNOLOGIES_LIMITED_RHP.pdf` | 637 | 15 | 622 | Mixed/partial |
| 022 | `022__sebi_098_V-MART_RETAIL_LIMITED_FOD` / `sebi_098_V-MART_RETAIL_LIMITED_FOD.pdf` | 437 | 14 | 423 | Mixed/partial |
| 023 | `023__sebi_156_TIJARIA_POLYPIPES_LIMITED_FOD` / `sebi_156_TIJARIA_POLYPIPES_LIMITED_FOD.pdf` | 341 | 13 | 328 | Mixed/partial |
| 024 | `024__blobextra_bd2e3115cf0e_THETA_PHARMACEUTICALS_LIMITED_RHP` / `blobextra_bd2e3115cf0e_THETA_PHARMACEUTICALS_LIMITED_RHP.pdf` | 247 | 13 | 234 | Mixed/partial |
| 025 | `025__sebi_111_KRIDHAN_INFRA_LIMITED_RHP` / `sebi_111_KRIDHAN_INFRA_LIMITED_RHP.pdf` | 314 | 11 | 303 | Mixed/partial |
| 026 | `026__sebi_110_KRIDHAN_INFRA_LIMITED_FOD` / `sebi_110_KRIDHAN_INFRA_LIMITED_FOD.pdf` | 312 | 11 | 301 | Mixed/partial |
| 027 | `027__sebi_065_FINEOTEX_CHEMICAL_LIMITED_FOD` / `sebi_065_FINEOTEX_CHEMICAL_LIMITED_FOD.pdf` | 256 | 11 | 245 | Mixed/partial |
| 028 | `028__sebi_070_FINEOTEX_CHEMICAL_LIMITED_RHP` / `sebi_070_FINEOTEX_CHEMICAL_LIMITED_RHP.pdf` | 256 | 11 | 245 | Mixed/partial |
| 029 | `029__blob_051_051_sa-dhan__original_annual_report_2021_22` / `blob_051_051_sa-dhan__original_annual_report_2021_22.pdf` | 69 | 11 | 58 | Mixed/partial |
| 030 | `030__sebi_134_SETUBANDHAN_INFRASTRUCTURE_LIMITED_FOD` / `sebi_134_SETUBANDHAN_INFRASTRUCTURE_LIMITED_FOD.pdf` | 359 | 10 | 349 | Mixed/partial |
| 031 | `031__blob_053_053_sa-dhan__original_annual_report_2023_24` / `blob_053_053_sa-dhan__original_annual_report_2023_24.pdf` | 65 | 10 | 55 | Mixed/partial |
| 032 | `032__blob_052_052_sa-dhan__original_annual_report_2022_23` / `blob_052_052_sa-dhan__original_annual_report_2022_23.pdf` | 58 | 10 | 48 | Mixed/partial |
| 033 | `033__blobextra_df1e1e16046d_BF_INDUSTRIAL_TECHNOLOGY___SOLUTIONS_LIMITED_FOD` / `blobextra_df1e1e16046d_BF_INDUSTRIAL_TECHNOLOGY___SOLUTIONS_LIMITED_FOD.pdf` | 367 | 9 | 358 | Mixed/partial |
| 034 | `034__sebi_151_SETUBANDHAN_INFRASTRUCTURE_LIMITED_RHP` / `sebi_151_SETUBANDHAN_INFRASTRUCTURE_LIMITED_RHP.pdf` | 359 | 9 | 350 | Mixed/partial |
| 035 | `035__blob_043_043_department_of_revenue__original_statistical_report_on_7_years_of_gst` / `blob_043_043_department_of_revenue__original_statistical_report_on_7_years_of_gst.pdf` | 65 | 9 | 56 | Mixed/partial |
| 036 | `036__BENARA_BEARINGS_AND_PISTONS_LIMITED_FOD` / `BENARA_BEARINGS_AND_PISTONS_LIMITED_FOD.pdf` | 481 | 8 | 473 | Mixed/partial |
| 037 | `037__blobextra_fe66f1c6bfb0_BENARA_BEARINGS_AND_PISTONS_LIMITED_RHP` / `blobextra_fe66f1c6bfb0_BENARA_BEARINGS_AND_PISTONS_LIMITED_RHP.pdf` | 481 | 8 | 473 | Mixed/partial |
| 038 | `038__CAPRICORN_FOOD_PRODUCTS_INDIA_LIMITED_DRHP` / `CAPRICORN_FOOD_PRODUCTS_INDIA_LIMITED_DRHP.pdf` | 446 | 8 | 438 | Mixed/partial |
| 039 | `039__sebi_053_GB_GLOBAL_LIMITED_FOD` / `sebi_053_GB_GLOBAL_LIMITED_FOD.pdf` | 383 | 8 | 375 | Mixed/partial |
| 040 | `040__sebi_059_GB_GLOBAL_LIMITED_RHP` / `sebi_059_GB_GLOBAL_LIMITED_RHP.pdf` | 382 | 8 | 374 | Mixed/partial |
| 041 | `041__blob_030_030_niti_aayog__original_aim__niti_ipe_white_paper_on_blended_financing` / `blob_030_030_niti_aayog__original_aim__niti_ipe_white_paper_on_blended_financing.pdf` | 48 | 7 | 41 | Mixed/partial |
| 042 | `042__blobextra_313b997b13a8_BOMBAY_SUPER_HYBRID_SEEDS_LIMITED_FOD` / `blobextra_313b997b13a8_BOMBAY_SUPER_HYBRID_SEEDS_LIMITED_FOD.pdf` | 408 | 6 | 402 | Mixed/partial |
| 043 | `043__ZOTA_HEALTH_CARE_LIMITED_FOD` / `ZOTA_HEALTH_CARE_LIMITED_FOD.pdf` | 461 | 5 | 456 | Mixed/partial |
| 044 | `044__ZOTA_HEALTH_CARE_LIMITED_RHP` / `ZOTA_HEALTH_CARE_LIMITED_RHP.pdf` | 461 | 5 | 456 | Mixed/partial |
| 045 | `045__BOHRA_INDUSTRIES_LIMITED_RHP` / `BOHRA_INDUSTRIES_LIMITED_RHP.pdf` | 435 | 5 | 430 | Mixed/partial |
| 046 | `046__BOHRA_INDUSTRIES_LIMITED_FOD` / `BOHRA_INDUSTRIES_LIMITED_FOD.pdf` | 434 | 5 | 429 | Mixed/partial |
| 047 | `047__blobextra_499fc5d1931e_KHADIM_INDIA_LIMITED_FOD` / `blobextra_499fc5d1931e_KHADIM_INDIA_LIMITED_FOD.pdf` | 409 | 5 | 404 | Mixed/partial |
| 048 | `048__blobextra_fbdca9d53696_KHADIM_INDIA_LIMITED_RHP` / `blobextra_fbdca9d53696_KHADIM_INDIA_LIMITED_RHP.pdf` | 409 | 5 | 404 | Mixed/partial |
| 049 | `049__blob_112_112_life_insurance_council__original_annual_report_2021_2022` / `blob_112_112_life_insurance_council__original_annual_report_2021_2022.pdf` | 740 | 5 | 735 | Mixed/partial |
| 050 | `050__blobextra_f102514d4612_INVENTURE_GROWTH_AND_SECURITIES_LIMITED_RHP` / `blobextra_f102514d4612_INVENTURE_GROWTH_AND_SECURITIES_LIMITED_RHP.pdf` | 397 | 5 | 392 | Mixed/partial |
| 051 | `051__blobextra_c80e0dc1cf2c_ACROPETAL_TECHNOLOGIES_LIMITED_RHP` / `blobextra_c80e0dc1cf2c_ACROPETAL_TECHNOLOGIES_LIMITED_RHP.pdf` | 306 | 5 | 301 | Mixed/partial |
| 052 | `052__blobextra_7e12da3324c4_GENERAL_INSURANCE_CORPORATION_OF_INDIA_FOD` / `blobextra_7e12da3324c4_GENERAL_INSURANCE_CORPORATION_OF_INDIA_FOD.pdf` | 570 | 4 | 566 | Mixed/partial |
| 053 | `053__blobextra_77ca65ea5335_MAHINDRA_LOGISTICS_LIMITED_DRHP` / `blobextra_77ca65ea5335_MAHINDRA_LOGISTICS_LIMITED_DRHP.pdf` | 562 | 4 | 558 | Mixed/partial |
| 054 | `054__blobextra_a83b3bdbf259_BHARAT_WIRE_ROPES_LIMITED_DRHP` / `blobextra_a83b3bdbf259_BHARAT_WIRE_ROPES_LIMITED_DRHP.pdf` | 437 | 4 | 433 | Mixed/partial |
| 055 | `055__blobextra_490216b1e744_DEEP_POLYMERS_LIMITED_FOD` / `blobextra_490216b1e744_DEEP_POLYMERS_LIMITED_FOD.pdf` | 418 | 4 | 414 | Mixed/partial |
| 056 | `056__INNOVATIVE_TYRES_&_TUBES_LIMITED_FOD` / `INNOVATIVE_TYRES_&_TUBES_LIMITED_FOD.pdf` | 416 | 4 | 412 | Mixed/partial |
| 057 | `057__INNOVATIVE_TYRES_&_TUBES_LIMITED_RHP` / `INNOVATIVE_TYRES_&_TUBES_LIMITED_RHP.pdf` | 416 | 4 | 412 | Mixed/partial |
| 058 | `058__blobextra_d6150fcf3b8f_HPL_ELECTRIC___POWER_LIMITED_RHP` / `blobextra_d6150fcf3b8f_HPL_ELECTRIC___POWER_LIMITED_RHP.pdf` | 469 | 4 | 465 | Mixed/partial |
| 059 | `059__sebi_081_MOMAI_APPARELS_LIMITED_FOD` / `sebi_081_MOMAI_APPARELS_LIMITED_FOD.pdf` | 421 | 4 | 417 | Mixed/partial |
| 060 | `060__blobextra_f0d370970dcc_UJJIVAN_FINANCIAL_SERVICES_LIMITED_DRHP` / `blobextra_f0d370970dcc_UJJIVAN_FINANCIAL_SERVICES_LIMITED_DRHP.pdf` | 391 | 4 | 387 | Mixed/partial |
| 061 | `061__blobextra_ce38744b83cf_blobextra_for_the_year_2024_2025` / `blobextra_ce38744b83cf_blobextra_for_the_year_2024_2025.pdf` | 4 | 4 | 0 | All pages |
| 062 | `062__AU_SMALL_FINANCE_BANK_LIMITED_FOD` / `AU_SMALL_FINANCE_BANK_LIMITED_FOD.pdf` | 515 | 3 | 512 | Mixed/partial |
| 063 | `063__GARDEN_REACH_SHIPBUILDERS_&_ENGINEERS_LIMITED_RHP` / `GARDEN_REACH_SHIPBUILDERS_&_ENGINEERS_LIMITED_RHP.pdf` | 515 | 3 | 512 | Mixed/partial |
| 064 | `064__blobextra_2ecb0157f400_GARDEN_REACH_SHIPBUILDERS_&_ENGINEERS_LIMITED_FOD` / `blobextra_2ecb0157f400_GARDEN_REACH_SHIPBUILDERS_&_ENGINEERS_LIMITED_FOD.pdf` | 513 | 3 | 510 | Mixed/partial |
| 065 | `065__blobextra_e2f9f54a5521_AU_SMALL_FINANCE_BANK_LIMITED_RHP` / `blobextra_e2f9f54a5521_AU_SMALL_FINANCE_BANK_LIMITED_RHP.pdf` | 511 | 3 | 508 | Mixed/partial |
| 066 | `066__blobextra_78f1a0016f85_ANGEL_ONE_LIMITED_DRHP` / `blobextra_78f1a0016f85_ANGEL_ONE_LIMITED_DRHP.pdf` | 470 | 3 | 467 | Mixed/partial |
| 067 | `067__ASTRON_PAPER_&_BOARD_MILL_LIMITED_FOD` / `ASTRON_PAPER_&_BOARD_MILL_LIMITED_FOD.pdf` | 469 | 3 | 466 | Mixed/partial |
| 068 | `068__ASTRON_PAPER_&_BOARD_MILL_LIMITED_RHP` / `ASTRON_PAPER_&_BOARD_MILL_LIMITED_RHP.pdf` | 468 | 3 | 465 | Mixed/partial |
| 069 | `069__blobextra_d2e1e549bbe4_SREI_EQUIPMENT_FINANCE_LIMITED_DRHP` / `blobextra_d2e1e549bbe4_SREI_EQUIPMENT_FINANCE_LIMITED_DRHP.pdf` | 465 | 3 | 462 | Mixed/partial |
| 070 | `070__AAVAS_FINANCIERS_LIMITED_DRHP` / `AAVAS_FINANCIERS_LIMITED_DRHP.pdf` | 458 | 3 | 455 | Mixed/partial |
| 071 | `071__CAPACIT'E_INFRAPROJECTS_LIMITED_FOD` / `CAPACIT'E_INFRAPROJECTS_LIMITED_FOD.pdf` | 456 | 3 | 453 | Mixed/partial |
| 072 | `072__blobextra_c38f7d5bc70e_CAPACIT_E_INFRAPROJECTS_LIMITED_RHP` / `blobextra_c38f7d5bc70e_CAPACIT_E_INFRAPROJECTS_LIMITED_RHP.pdf` | 455 | 3 | 452 | Mixed/partial |
| 073 | `073__CAPACIT'E_INFRAPROJECTS_LIMITED_DRHP` / `CAPACIT'E_INFRAPROJECTS_LIMITED_DRHP.pdf` | 454 | 3 | 451 | Mixed/partial |
| 074 | `074__FUTURE_SUPPLY_CHAIN_SOLUTIONS_LIMITED_RHP` / `FUTURE_SUPPLY_CHAIN_SOLUTIONS_LIMITED_RHP.pdf` | 428 | 3 | 425 | Mixed/partial |
| 075 | `075__SIDDHARTH_EDUCATION_SERVICES_LIMITED_RHP` / `SIDDHARTH_EDUCATION_SERVICES_LIMITED_RHP.pdf` | 409 | 3 | 406 | Mixed/partial |
| 076 | `076__blobextra_ff2fa3432967_KHADIM_INDIA_LIMITED_DRHP` / `blobextra_ff2fa3432967_KHADIM_INDIA_LIMITED_DRHP.pdf` | 399 | 3 | 396 | Mixed/partial |
| 077 | `077__blobextra_d461d0d867e9_AKASH_INFRA-PROJECTS_LIMITED_FOD` / `blobextra_d461d0d867e9_AKASH_INFRA-PROJECTS_LIMITED_FOD.pdf` | 322 | 3 | 319 | Mixed/partial |
| 078 | `078__blob_006_006_tea_board_of_india__original_annual_accounts_2021_22` / `blob_006_006_tea_board_of_india__original_annual_accounts_2021_22.pdf` | 252 | 3 | 249 | Mixed/partial |
| 079 | `079__blob_017_017_department_of_financial_services__original_annual_report_2022_23` / `blob_017_017_department_of_financial_services__original_annual_report_2022_23.pdf` | 39 | 3 | 36 | Mixed/partial |
| 080 | `080__BARBEQUE-NATION_HOSPITALITY_LIMITED_DRHP` / `BARBEQUE-NATION_HOSPITALITY_LIMITED_DRHP.pdf` | 515 | 2 | 513 | Mixed/partial |
| 081 | `081__SHALBY_LIMITED_FOD` / `SHALBY_LIMITED_FOD.pdf` | 513 | 2 | 511 | Mixed/partial |
| 082 | `082__SHALBY_LIMITED_RHP` / `SHALBY_LIMITED_RHP.pdf` | 513 | 2 | 511 | Mixed/partial |
| 083 | `083__SHALBY_LIMITED_DRHP` / `SHALBY_LIMITED_DRHP.pdf` | 499 | 2 | 497 | Mixed/partial |
| 084 | `084__blobextra_4a3fc692c0c7_INOX_WIND_LIMITED_RHP` / `blobextra_4a3fc692c0c7_INOX_WIND_LIMITED_RHP.pdf` | 491 | 2 | 489 | Mixed/partial |
| 085 | `085__blobextra_aa1b2adb29e1_INOX_WIND_LIMITED_FOD` / `blobextra_aa1b2adb29e1_INOX_WIND_LIMITED_FOD.pdf` | 491 | 2 | 489 | Mixed/partial |
| 086 | `086__blobextra_79cb0aa7c9fa_PSP_PROJECTS_LIMITED_FOD` / `blobextra_79cb0aa7c9fa_PSP_PROJECTS_LIMITED_FOD.pdf` | 487 | 2 | 485 | Mixed/partial |
| 087 | `087__blobextra_653619a90ef7_AMBER_ENTERPRISES_INDIA_LIMITED_DRHP` / `blobextra_653619a90ef7_AMBER_ENTERPRISES_INDIA_LIMITED_DRHP.pdf` | 483 | 2 | 481 | Mixed/partial |
| 088 | `088__COCHIN_SHIPYARD_LIMITED_FOD` / `COCHIN_SHIPYARD_LIMITED_FOD.pdf` | 483 | 2 | 481 | Mixed/partial |
| 089 | `089__ICICI_SECURITIES_LIMITED_DRHP` / `ICICI_SECURITIES_LIMITED_DRHP.pdf` | 460 | 2 | 458 | Mixed/partial |
| 090 | `090__blobextra_d77802b199ca_GALAXY_SURFACTANTS_LTD_FOD` / `blobextra_d77802b199ca_GALAXY_SURFACTANTS_LTD_FOD.pdf` | 447 | 2 | 445 | Mixed/partial |
| 091 | `091__GALAXY_SURFACTANTS_LTD_RHP` / `GALAXY_SURFACTANTS_LTD_RHP.pdf` | 445 | 2 | 443 | Mixed/partial |
| 092 | `092__blobextra_627d6b00b51d_AVANA_LOGISTEK_LIMITED_DRHP` / `blobextra_627d6b00b51d_AVANA_LOGISTEK_LIMITED_DRHP.pdf` | 439 | 2 | 437 | Mixed/partial |
| 093 | `093__GALAXY_SURFACTANTS_LTD_DRHP` / `GALAXY_SURFACTANTS_LTD_DRHP.pdf` | 433 | 2 | 431 | Mixed/partial |
| 094 | `094__FUTURE_SUPPLY_CHAIN_SOLUTIONS_LIMITED_FOD` / `FUTURE_SUPPLY_CHAIN_SOLUTIONS_LIMITED_FOD.pdf` | 428 | 2 | 426 | Mixed/partial |
| 095 | `095__INDIAN_ENERGY_EXCHANGE_LIMITED_FOD` / `INDIAN_ENERGY_EXCHANGE_LIMITED_FOD.pdf` | 414 | 2 | 412 | Mixed/partial |
| 096 | `096__blobextra_4ea93e06aa2f_INDIAN_ENERGY_EXCHANGE_LIMITED_RHP` / `blobextra_4ea93e06aa2f_INDIAN_ENERGY_EXCHANGE_LIMITED_RHP.pdf` | 413 | 2 | 411 | Mixed/partial |
| 097 | `097__blobextra_05a1609c50c2_ANMOL_INDUSTRIES_LIMITED_DRHP` / `blobextra_05a1609c50c2_ANMOL_INDUSTRIES_LIMITED_DRHP.pdf` | 411 | 2 | 409 | Mixed/partial |
| 098 | `098__3MINDIA_ar_2021` / `3MINDIA_ar_2021.pdf` | 264 | 2 | 262 | Mixed/partial |
| 099 | `099__LEMON_TREE_HOTELS_LIMITED_DRHP` / `LEMON_TREE_HOTELS_LIMITED_DRHP.pdf` | 572 | 1 | 571 | Mixed/partial |
| 100 | `100__20MICRONS_ar_2013` / `20MICRONS_ar_2013.pdf` | 1 | 1 | 0 | All pages |

## Verification

- Copied and verified 100/100 PDFs; every repository copy matches its expected SHA-256 hash.
- Page counts were checked from each PDF with PDFium: 37,600 pages total.
- The selection is SHA-256 deduplicated; all 100 hashes are unique.
- The full row-level inventory and top-50 subset inventory are included in the repository root.

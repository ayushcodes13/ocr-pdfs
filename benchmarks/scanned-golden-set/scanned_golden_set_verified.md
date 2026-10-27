# Golden Set: Scanned Financial and Administrative Documents

**Dataset:** OCR_Scanned_Documents_093-100_then_003-014.pdf
**Sessions:** 20 | **QA turns:** 60 | **Original source PDFs:** 18

> **Coverage note:** This is an evidence-checked first-pass benchmark across the 18 sources, not an exhaustive human visual reading of all 927 pages. Individual gold answers have page-level evidence in the source scans; additional material may exist on unsampled pages.

---

## scanned_session_01: Shiv Fibretex (filename says Fabritex): audited results and board-report tie-out

### Turn 1 — Summarization / Overview

**Question:** For the company named Shiv Fibretex in the scanned pages, what financial period and audit materials are in the scanned record?

**Golden answer:** The record includes the independent auditor’s report and financial statements for Shiv Fibretex International Private Limited as at/for the year ended 31 March 2023, along with comparative figures for the year ended 31 March 2022 and a board report.

**Citation source:** shiv fabritex international pvt ltd.pdf [source #093], original p. 1, merged PDF p. 2; upper half, independent auditor report and period description | shiv fabritex international pvt ltd.pdf [source #093], original p. 28, merged PDF p. 29; statement of profit and loss, table heading | shiv fabritex international pvt ltd.pdf [source #093], original p. 47, merged PDF p. 48; board report, introductory paragraph

### Turn 2 — High-Precision Extraction

**Question:** In that 2022–23 profit-and-loss statement, what are revenue from operations, other income, and profit after tax? Preserve the unit.

**Golden answer:** Revenue from operations: ₹4,68,548.65 thousand; other income: ₹79.72 thousand; and profit after tax: ₹2,877.92 thousand. The scanned statement labels the amounts “Rupees in Thousands.”

**Citation source:** shiv fabritex international pvt ltd.pdf [source #093], original p. 28, merged PDF p. 29; profit-and-loss table, current-period column, Revenue from operations and Other Income rows | shiv fabritex international pvt ltd.pdf [source #093], original p. 29, merged PDF p. 30; top half, Profit/(Loss) for the Period row

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Can you corroborate those profit figures elsewhere in the scans, and how is the statement authenticated?

**Golden answer:** Yes. The board report repeats current-year net profit after tax of ₹2,877.92 thousand versus ₹2,735.19 thousand for the previous year. The adjacent signed continuation of the profit-and-loss statement shows the auditor’s circular seal/signature on the lower left and director signature blocks for Amit Garg and Mohit Garg on the lower right.

**Citation source:** shiv fabritex international pvt ltd.pdf [source #093], original p. 47, merged PDF p. 48; Financial Results table, Net Profit After Tax row | shiv fabritex international pvt ltd.pdf [source #093], original p. 29, merged PDF p. 30; lower half, auditor seal and director-signature blocks

---

## scanned_session_02: Yugveri Marketing (file labeled Yugeri): directors report, meeting count and reserves

### Turn 1 — Summarization / Overview

**Question:** What financial year does the Yugveri Marketing directors’ report cover and what does it say about business operations?

**Golden answer:** The 29th Annual Report of Yugveri Marketing Private Limited addresses the year ended 31 March 2023. The directors report revenue from operations of ₹3,16,52,154 and net profit after tax of ₹72,402 for that year.

**Citation source:** Yugeri Marketing Private Limited.pdf [source #094], original p. 1, merged PDF p. 62; top half, Directors’ Report and State of Company Affairs paragraph

### Turn 2 — High-Precision Extraction

**Question:** How many board meetings were held during that year, and what are their dates?

**Golden answer:** Six board meetings are listed: 05/04/2022, 16/06/2022, 25/08/2022, 03/09/2022, 06/12/2022 and 08/03/2023. The attendance column shows two directors present at each meeting.

**Citation source:** Yugeri Marketing Private Limited.pdf [source #094], original p. 2, merged PDF p. 63; upper-middle, Meetings of the Board table, six date rows

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** How did the directors handle dividend and reserves despite the reported profit?

**Golden answer:** They did not recommend a dividend for the year, citing growth plans, and stated that ₹14,480 had been transferred to the Special Reserve Account. Both disclosures appear in the same directors’ report that gives the ₹72,402 net profit figure, so they should not be confused with a shareholder dividend payment.

**Citation source:** Yugeri Marketing Private Limited.pdf [source #094], original p. 1, merged PDF p. 62; State of Company Affairs, Dividend and Transfer to Reserves paragraphs

---

## scanned_session_03: Gianna Agro: profit, ownership and signatory cross-check

### Turn 1 — Summarization / Overview

**Question:** What statements and reporting date are shown for Gianna Agro?

**Golden answer:** Gianna Agro Private Limited provides a balance sheet as at 31 March 2023 and a statement of profit and loss for the year ended on that date, each comparing 31 March 2023 with 31 March 2022. The financial amounts are expressed in INR lakhs unless otherwise specified.

**Citation source:** Gianna Agro Pvt. Ltd.pdf [source #095], original p. 1, merged PDF p. 117; balance-sheet header and two date columns | Gianna Agro Pvt. Ltd.pdf [source #095], original p. 2, merged PDF p. 118; profit-and-loss header and unit note

### Turn 2 — High-Precision Extraction

**Question:** What were total income and profit for the year in the newer financial year, compared with the prior one?

**Golden answer:** Total income was ₹4,809.19 lakh in FY2022–23 versus ₹65.95 lakh in FY2021–22. Profit for the period was ₹18.63 lakh versus ₹3.36 lakh, respectively.

**Citation source:** Gianna Agro Pvt. Ltd.pdf [source #095], original p. 2, merged PDF p. 118; upper table, Total Income row and lower table, Profit/(Loss) for the Period row

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Do the equity shareholders listed in the notes have the same names as the two people signing the profit-and-loss statement?

**Golden answer:** No. The shareholding table names Rakhi Gupta and Swapnil Gupta, each holding 5,000 shares (50.00% each), while the profit-and-loss signature blocks name Ravi Navratn Jain and Abhinav Vinod Gupta as directors. They are distinct name lists and should not be conflated.

**Citation source:** Gianna Agro Pvt. Ltd.pdf [source #095], original p. 4, merged PDF p. 120; bottom third, shareholder table, Name/No. of Shares/% of Holding columns | Gianna Agro Pvt. Ltd.pdf [source #095], original p. 2, merged PDF p. 118; bottom, signed director blocks

---

## scanned_session_04: Suruchi Dairy: liquidity and recoverability emphasis against balance-sheet evidence

### Turn 1 — Summarization / Overview

**Question:** What issue did the auditor actually highlight under “Emphasis of Matter” in Suruchi Dairy’s report?

**Golden answer:** The auditor’s report for the year ended 31 March 2023 includes an “Emphasis of Matter” about the company’s liquidity assessment for the coming year and recoverability of assets. It references inventories and payment of statutory dues in the CARO annexure and says management expects to recover the assets’ carrying amounts. The auditor expressly states that the opinion is not modified in respect of that matter.

**Citation source:** Suruchi Dairy & Dairy Products.pdf [source #096], original p. 1, merged PDF p. 148; lower third, Emphasis of Matter paragraph, closing opinion sentence

### Turn 2 — High-Precision Extraction

**Question:** Which exact negative equity figure appears in the corresponding balance sheet, and in what unit?

**Golden answer:** Reserves and surplus at 31 March 2023 are shown as negative ₹300.38 lakh, in a balance-sheet table labelled “Rupees in Lakhs.” The total balance sheet at that date is ₹543.16 lakh.

**Citation source:** Suruchi Dairy & Dairy Products.pdf [source #096], original p. 7, merged PDF p. 154; top-left balance sheet, Reserves and Surplus and TOTAL rows

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** How do the numbers and the signatures support the audit narrative, without treating the emphasis paragraph as a qualified opinion?

**Golden answer:** The negative reserves in the balance sheet are a relevant financial-stress indicator consistent with the auditor’s liquidity/recoverability emphasis; they do not by themselves establish insolvency. The balance sheet bears the auditor’s stamped/signature area at the lower left (M. No. 44878) and multiple director signature blocks to the lower right, dated 27 September 2023. The auditor explicitly says the opinion is not modified.

**Citation source:** Suruchi Dairy & Dairy Products.pdf [source #096], original p. 1, merged PDF p. 148; Emphasis of Matter, final line | Suruchi Dairy & Dairy Products.pdf [source #096], original p. 7, merged PDF p. 154; top table, negative reserves; lower portion, auditor seal, board signatures and date

---

## scanned_session_05: Meso: scan-color financials and two-year profitability

### Turn 1 — Summarization / Overview

**Question:** Which period is covered by the yellow scanned Meso statements, and what three primary statements are shown?

**Golden answer:** Meso Private Limited has an audited balance sheet as at 31 March 2024, audited profit-and-loss statement for the period ended 31 March 2024, and cash-flow statement for the year ended 31 March 2024. The tables compare against the previous year and use rupees in lakhs.

**Citation source:** Meso Private Limited.pdf [source #097], original p. 1, merged PDF p. 176; balance-sheet title and date/units columns | Meso Private Limited.pdf [source #097], original p. 2, merged PDF p. 177; P&L title and date columns | Meso Private Limited.pdf [source #097], original p. 3, merged PDF p. 178; cash-flow heading

### Turn 2 — High-Precision Extraction

**Question:** What changed in revenue from operations and profit for the year from 2023 to 2024?

**Golden answer:** Revenue from operations increased from ₹10,409 lakh (2023) to ₹11,359 lakh (2024), and profit for the year increased from ₹1,450 lakh to ₹2,386 lakh.

**Citation source:** Meso Private Limited.pdf [source #097], original p. 2, merged PDF p. 177; upper half, Revenue from Operations and Profit for the Year rows, 2024 and 2023 columns

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Where is the auditor evidence located on the same profit statement, and whose director signatures appear?

**Golden answer:** The lower-left audit section names Kamdar Desai & Patel LLP and contains a circular seal beside partner Urmil Shah’s signature. The lower right contains signatures labelled Ketan K. Sheth and Hemant T. Vashi, directors, with a round Meso company stamp below. The page is dated 05/09/2024 in Mumbai.

**Citation source:** Meso Private Limited.pdf [source #097], original p. 2, merged PDF p. 177; bottom left auditor signature and stamp; bottom right directors and company stamp

---

## scanned_session_06: Chandra Narain Machinery Stores: balance-sheet and auditor sign-off

### Turn 1 — Summarization / Overview

**Question:** Which company and dates are covered by the scanned independent auditor report and balance sheet?

**Golden answer:** S.K.M. & Co. issues the independent auditor’s report for Chandra Narain Machinery Stores Private Limited; the accompanying balance sheet is as at 31 March 2023, with comparative amounts as at 31 March 2022.

**Citation source:** CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf [source #098], original p. 1, merged PDF p. 195; upper auditor-report heading and first opinion paragraph | CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf [source #098], original p. 6, merged PDF p. 200; balance sheet title and column headings

### Turn 2 — High-Precision Extraction

**Question:** Give the exact balance-sheet totals for 2023 and 2022, including the displayed unit.

**Golden answer:** Total assets and total equity/liabilities both equal ₹5,69,842.15 thousand at 31 March 2023 and ₹7,42,611.14 thousand at 31 March 2022. The scan specifies that all amounts are in ₹’000 unless otherwise stated.

**Citation source:** CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf [source #098], original p. 6, merged PDF p. 200; balance sheet top-right date columns and two Total rows

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Who signed the 2023 balance sheet and what authentication evidence is visible?

**Golden answer:** At the bottom, auditor Amit Bansal signs for S.K.M. & Co., beside the circular red firm stamp; Narendra Kumar Jain and Sunita Jain sign for the board. The block records Agra, 16 August 2023. The signatures sit immediately beneath the balancing totals, helping establish that the table is the signed financial statement.

**Citation source:** CHANDRA NARAIN MACHINERY STORES PRIVATE LIMITED-(MCA).pdf [source #098], original p. 6, merged PDF p. 200; bottom-left auditor stamp, bottom-centre and bottom-right director signatures and date

---

## scanned_session_07: AAQUARIES: provisional results and equity-note linkage

### Turn 1 — Summarization / Overview

**Question:** Are AAQUARIES’ results presented as audited annual statements or another type of financial record?

**Golden answer:** The scanned section labels the 31 March 2023 balance sheet and profit-and-loss account as “Provisional Standalone,” and it also includes a standalone cash-flow statement and notes to accounts. It should not be described as a completed statutory audit solely on the strength of these pages.

**Citation source:** AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 1, merged PDF p. 211; balance-sheet heading | AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 2, merged PDF p. 212; cash-flow statement heading | AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 3, merged PDF p. 213; P&L heading

### Turn 2 — High-Precision Extraction

**Question:** Read the 2023 profit after tax and earnings per share from the scanned P&L, not the balance-sheet assets.

**Golden answer:** For the period ended 31 March 2023, profit after tax is ₹13,78,71,511.03 and EPS is 265.14. The corresponding 2022 entries are ₹11,44,46,544.37 and 220.09.

**Citation source:** AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 3, merged PDF p. 213; lower P&L table, Profit (Loss) After Tax and EPS rows, both date columns

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** How do the notes and stamped P&L distinguish share rights from the financial performance figures?

**Golden answer:** The share-capital note says equity shares have a par value of ₹10 and one vote per share; that is ownership-rights information, not the EPS of 265.14 reported on the P&L. The P&L footer has a blue AAQUARIES company seal and a “01 APR 2023” date stamp near Dr Sameer Talim’s whole-time director sign-off.

**Citation source:** AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 4, merged PDF p. 214; middle paragraph, Terms/Rights attached to equity shares | AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 3, merged PDF p. 213; EPS row and bottom blue seal/date/signatory

---

## scanned_session_08: Twentyfirst Century Management Services: standalone versus consolidated quarter

### Turn 1 — Summarization / Overview

**Question:** What quarter is being reported, and what does the exchange submission say about audit status?

**Golden answer:** The exchange communication dated 29 July 2025 concerns the unaudited results for the quarter ended 30 June 2025. It says the audit committee reviewed and the board approved the results; the accompanying independent auditor reports are limited reviews rather than full audit opinions.

**Citation source:** 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 1, merged PDF p. 220; subject and first numbered board-resolution paragraph | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 2, merged PDF p. 221; independent auditors’ review report, conclusion about scope

### Turn 2 — High-Precision Extraction

**Question:** What are the standalone and consolidated total revenue and profit after tax for that quarter?

**Golden answer:** For the quarter ended 30 June 2025, the standalone statement shows total revenue ₹289.57 lakh and profit ₹238.47 lakh. The consolidated statement shows total revenue ₹334.07 lakh and profit ₹231.48 lakh.

**Citation source:** 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 4, merged PDF p. 223; standalone quarterly table, 30-06-2025 column, Total Revenue and Profit/(Loss) for the period rows | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 7, merged PDF p. 226; consolidated quarterly table, 30-06-2025 column, same rows

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Why must we not report the consolidated figures as a second standalone quarter, and what is the named subsidiary?

**Golden answer:** The later statement is explicitly headed “CONSOLIDATED UNAUDITED FINANCIAL RESULTS” and its note states that it includes the wholly owned subsidiary Twentyfirst Century Shares & Securities Limited. The earlier statement is explicitly “STANDALONE.” Both refer to the same quarter, so the revenue figures are different reporting scopes, not separate quarters.

**Citation source:** 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 4, merged PDF p. 223; statement title, STANDALONE | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 7, merged PDF p. 226; statement title, CONSOLIDATED, and Note 2 below the table

---

## scanned_session_09: Tea Board of India: annual-accounts structure and rotated schedules

### Turn 1 — Summarization / Overview

**Question:** What entity and fiscal period does the illustrated tea-kettle cover identify?

**Golden answer:** It is the Tea Board of India’s 69th Annual Accounts for 2022–23. The cover presents the English and Hindi title alongside a Tea Board logo and a kettle pouring tea.

**Citation source:** blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf [source #003], original p. 1, merged PDF p. 227; full-page front cover, logo and title

### Turn 2 — High-Precision Extraction

**Question:** Where does its table of contents place the consolidated receipt-and-payment, income-and-expenditure, and balance-sheet sections?

**Golden answer:** The table of contents assigns consolidated Receipt & Payment Account to pages 1–5, consolidated Income & Expenditure Account to page 6, and consolidated Balance Sheet to page 7 of the original printed publication (these are publication page numbers, not the merged-PDF numbers).

**Citation source:** blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf [source #003], original p. 4, merged PDF p. 230; top table of contents, first three rows and Page No. column

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Does the sideways grid later in the file represent a new document or a schedule within the Tea Board accounts?

**Golden answer:** It is a rotated in-document table headed “Assets Physical Verification Report 2022–23,” with an “Annexure-II” heading and many fine grid columns. It falls within the bookmarked Tea Board source section; the sideways orientation is a page-layout issue, not a new PDF boundary.

**Citation source:** blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf [source #003], original p. 16, merged PDF p. 242; landscape/90-degree printed table, title and Annexure-II marker | blob_007_007_tea_board_of_india__original_69th_annual_accounts_of_tea_board_india_2022_23.pdf [source #003], original p. 1, merged PDF p. 227; Tea Board source cover

---

## scanned_session_10: Ministry of Science and Technology: demand-number and table hierarchy

### Turn 1 — Summarization / Overview

**Question:** What ministry, fiscal year and document type are given on the cover?

**Golden answer:** The title page states “Detailed Demands for Grants” of the Ministry of Science and Technology for 2021–2022. The number 45 is printed prominently at the top left of the cover.

**Citation source:** blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf [source #004], original p. 1, merged PDF p. 365; central bilingual title block and upper-left cover number

### Turn 2 — High-Precision Extraction

**Question:** In the departmental budget table, which demand number and department appear?

**Golden answer:** The tabular heading is “Demand No. 88 – Department of Science & Technology” (also displayed bilingually). The table uses a “Rupees in Thousands” amount notation.

**Citation source:** blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf [source #004], original p. 4, merged PDF p. 368; table header, Demand No. 88 and top-right units label

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** How is the departmental table structured across the adjacent pages?

**Golden answer:** The Department of Science & Technology demand continues across successive tabular pages. The earlier page includes salaries, wages, overtime allowance, domestic and foreign travel, office expenses and other object heads, while the following page continues with the same accounting-code/estimate column structure. They should be read as one continuing grant schedule rather than unrelated charts.

**Citation source:** blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf [source #004], original p. 4, merged PDF p. 368; body of tabular expenditure object heads | blob_029_029_department_of_science_and_technology__original_budget_2021_22.pdf [source #004], original p. 5, merged PDF p. 369; same demand title and matching budget estimate columns

---

## scanned_session_11: FIPI pre-budget memorandum: tax-policy section mapping

### Turn 1 — Summarization / Overview

**Question:** Who prepared the petroleum-industry memorandum, and for which Union Budget?

**Golden answer:** The cover identifies the Federation of Indian Petroleum Industry (FIPI) and labels the document “Pre-Budget Memorandum, Union Budget 2024–25.” It is a set of industry policy proposals, not an enacted budget statement.

**Citation source:** blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 1, merged PDF p. 503; front cover, FIPI mark and title

### Turn 2 — High-Precision Extraction

**Question:** What broad tax headings can you distinguish in the contents, and where is income tax placed?

**Golden answer:** The contents starts with “A. DIRECT TAX,” then an “INCOME TAX” subsection, followed by headings for upstream, downstream, natural gas and general topics. Later contents pages list GST and indirect-tax/excise/customs matters. The initial contents page places the income-tax material at printed page 7.

**Citation source:** blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 2, merged PDF p. 504; top and middle, contents hierarchy and “Income Tax ... 7” | blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 4, merged PDF p. 506; contents continuation, GST and natural gas categories | blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 5, merged PDF p. 507; contents continuation, Excise Duty and Customs Duty

### Turn 3 — Multi-Hop Synthesis / Compliance Scope

**Question:** If a reviewer asks whether GST and excise recommendations are part of the same direct-tax section, how should you resolve that from the scanned contents?

**Golden answer:** They should be categorized separately. The first contents page begins with direct tax/income tax, while the continuation pages enumerate GST, excise duty and customs duty in their own later headings. All remain within the one FIPI memorandum but are not the same tax category.

**Citation source:** blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 2, merged PDF p. 504; top, A. DIRECT TAX and income-tax heading | blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 4, merged PDF p. 506; middle-to-lower, GST entries | blob_146_146_federation_of_indian_petroleum_industry__original_pre_budget_memorandum_for_union_budget_2024_25.pdf [source #006], original p. 5, merged PDF p. 507; middle, II EXCISE DUTY and III CUSTOMS DUTY

---

## scanned_session_12: 20 Microns: director-report reconciliation with prior year

### Turn 1 — Summarization / Overview

**Question:** Which annual report is shown and what fiscal-year result does it cover?

**Golden answer:** This is the 24th Annual Report of 20 Microns Limited for 2010–11. Its board-of-directors report presents the audited accounts for the year ended 31 March 2011, including comparative results for 31 March 2010.

**Citation source:** 20MICRONS_ar_2011.pdf [source #007], original p. 1, merged PDF p. 597; annual-report cover, 24th Annual Report 2010–11 | 20MICRONS_ar_2011.pdf [source #007], original p. 7, merged PDF p. 603; Directors’ Report opening and result-column headings

### Turn 2 — High-Precision Extraction

**Question:** What gross sales and PBDITA were reported for 2011 versus 2010?

**Golden answer:** All figures are in ₹ lakhs. Sales (gross): ₹24,072.38 lakh at 31 March 2011 versus ₹17,999.13 lakh at 31 March 2010. Profit before depreciation, interest and tax (PBDITA): ₹2,555.41 lakh versus ₹2,300.13 lakh.

**Citation source:** 20MICRONS_ar_2011.pdf [source #007], original p. 7, merged PDF p. 603; Results of Operations table, first two rows, 2011 and 2010 columns

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Did higher sales also mean higher net profit? Cross-check the lower rows and the performance commentary.

**Golden answer:** No. The same table reports net profit of ₹550.19 lakh for 2011 versus ₹729.74 lakh for 2010, despite higher sales and PBDITA. The performance review below the table explicitly highlights the sales increase, so a correct answer must distinguish top-line growth from net-profit performance.

**Citation source:** 20MICRONS_ar_2011.pdf [source #007], original p. 7, merged PDF p. 603; lower Results of Operations table, Net Profit/(loss) row; bottom Performance Review paragraph

---

## scanned_session_13: Chemicals and Fertilizers: cover-to-demand drill-down

### Turn 1 — Summarization / Overview

**Question:** What government budget document and year does the pink cover identify?

**Golden answer:** The pink title page is the Government of India’s Detailed Demands for Grants of the Ministry of Chemicals and Fertilizers for 2022–23. A large “4” is printed in the upper-left corner.

**Citation source:** blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf [source #009], original p. 1, merged PDF p. 687; pink cover, government crest, ministry, year and numeral 4

### Turn 2 — High-Precision Extraction

**Question:** What is the department and demand number on the next colored divider?

**Golden answer:** The green divider reads “Demand No. 5 – Department of Chemicals & Petrochemicals,” with corresponding Hindi text.

**Citation source:** blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf [source #009], original p. 2, merged PDF p. 688; central framed bilingual heading on green page

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Which source pages establish that the following rupee columns belong to that same demand?

**Golden answer:** The next detailed table continues with “Demand No. 5 – Department of Chemicals & Petrochemicals” across the top and uses the Actuals, Budget Estimates and Revised Estimates column headers. The adjacent continuation page retains the same departmental context. Thus the estimate columns on these pages belong to Demand No. 5, not an unrelated Department of Fertilizers table.

**Citation source:** blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf [source #009], original p. 2, merged PDF p. 688; green demand-divider title | blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf [source #009], original p. 4, merged PDF p. 690; table header, Demand No. 5 and Actuals/B.E./R.E. columns | blob_035_035_department_of_fertilizers__original_detailed_demand_for_grants_2022_23.pdf [source #009], original p. 5, merged PDF p. 691; continuation grid with matching B.E./R.E. heading

---

## scanned_session_14: FIDC: council governance and financial-result arithmetic

### Turn 1 — Summarization / Overview

**Question:** Which organization and reporting year are shown on the cover and directors’ report?

**Golden answer:** The Finance Industry Development Council (FIDC) presents its 18th Annual Report for 2021–22, with audited accounts for the year ended 31 March 2022.

**Citation source:** blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf [source #010], original p. 1, merged PDF p. 775; cover title, 18th Annual Report 2021–22 | blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf [source #010], original p. 5, merged PDF p. 779; Directors’ Report first paragraph

### Turn 2 — High-Precision Extraction

**Question:** What are FIDC’s gross income, expenses/transfers, and year surplus for 2022?

**Golden answer:** In rupees, gross income is ₹42,47,881; expenses/transfers are ₹36,74,888; and the surplus for the year is ₹4,25,454. The table also shows a tax provision of ₹1,50,000 and an excess/short tax-provision adjustment of (₹2,461), so the surplus is not simply gross income minus expenses.

**Citation source:** blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf [source #010], original p. 5, merged PDF p. 779; FINANCIAL RESULTS table, 31.03.2022 column, first five financial rows

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Where would you verify the auditor and registered-office details instead of treating them as income rows?

**Golden answer:** The separate contents-and-contact page identifies the auditors as Bhuwania & Agrawal Associates, the banker as HDFC Bank Ltd., and the registered/administrative office at 101/103 Sunflower, 1st Floor, Rajawadi Road No. 2, Ghatkopar (East), Mumbai 400 077. These are governance/contact blocks, not entries in the directors’ financial-results table.

**Citation source:** blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf [source #010], original p. 4, merged PDF p. 778; right-hand AUDITORS/BANKER boxes and lower-left registered-office box | blob_054_054_finance_industry_development_council__fidc__original_fidc_18th_annual_report_2021_22.pdf [source #010], original p. 5, merged PDF p. 779; financial-results table

---

## scanned_session_15: FACE/D91 Labs: credit-scoring ranges and evidence distinction

### Turn 1 — Summarization / Overview

**Question:** Who is behind the alternative-data report and what lending question does it address?

**Golden answer:** The cover carries D91 Labs and FACE branding, with the title “State of alternative data in India – The lending use-case.” The report examines alternative data in credit assessment and the underwriting gap for thin-file/no-credit-history consumers.

**Citation source:** blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf [source #011], original p. 1, merged PDF p. 814; cover logos and title | blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf [source #011], original p. 4, merged PDF p. 817; Overcoming data gaps in credit underwriting heading and discussion

### Turn 2 — High-Precision Extraction

**Question:** What six CIBIL credit-score tiers appear in the boxed chart?

**Golden answer:** The score legend lists: No Score (NTC), Subprime 300–680, Near Prime 681–730, Prime 731–770, Prime Plus 771–790, and Super Prime 790+. Preserve the report’s printed labels and ranges as displayed.

**Citation source:** blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf [source #011], original p. 4, merged PDF p. 817; middle, colored Credit tiers based in CIBIL score range strip

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** How does the report connect the score-gap discussion with its depicted borrower example?

**Golden answer:** The preceding page explains that thin-file or no-credit-history consumers may be difficult to assess using conventional credit-bureau scores. The next page uses “Mr. Vinay Kumar” as an illustrated example of a gig worker with income and transactions but no formal loan history, motivating alternative-data assessment. The illustration is an explanatory scenario, not proof that the depicted person is an actual borrower in the study.

**Citation source:** blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf [source #011], original p. 4, merged PDF p. 817; first paragraphs and colored credit-score tier strip | blob_048_048_fintech_association_for_consumer_empowerment__face__original_state_of_alternative_data_in_india_a_lending_use_case.pdf [source #011], original p. 5, merged PDF p. 818; right narrative and left illustrated Mr. Vinay Kumar profile

---

## scanned_session_16: Indian Tea Association FY2024: auditor scope and signed balance sheet

### Turn 1 — Summarization / Overview

**Question:** What reporting period and assurance context does the Indian Tea Association financial report present?

**Golden answer:** The Indian Tea Association’s financial statements are as at 31 March 2024, prepared by SBA Associates. The audit report addresses the association’s balance sheet and income/expenditure statement and explains that several branch accounts were audited by other auditors, whose reports informed the consolidated/merged presentation.

**Citation source:** blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 1, merged PDF p. 850; cover, FY2024 and preparer | blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 2, merged PDF p. 851; audit report, first paragraph and branches-other-auditors scope

### Turn 2 — High-Precision Extraction

**Question:** What is the total Sources of Funds/Application of Funds for 2024 and the prior year?

**Golden answer:** The balance-sheet total is ₹10,86,43,595 as at 31 March 2024 and ₹11,68,45,110 as at 31 March 2023, displayed on both the Sources of Funds and Application of Funds sides.

**Citation source:** blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 5, merged PDF p. 854; balance-sheet table, bold Total rows in both date columns

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Where can a reviewer confirm that this balance sheet is signed rather than an unsigned table?

**Golden answer:** Below the balance-sheet totals, the scan shows the SBA Associates auditor signature/seal and two association signature blocks labelled Chairman and Secretary General. The date “01.08.2024” is printed in the lower portion. The separate audit-report page also contains the auditor seal, partner signature and the Kolkata date.

**Citation source:** blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 5, merged PDF p. 854; lower margin, signatures, circular seal and date | blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 4, merged PDF p. 853; bottom-right auditor sign-off and Kolkata date

---

## scanned_session_17: Indian Jute Mills Association: alternate audit-method explanation

### Turn 1 — Summarization / Overview

**Question:** What is the association and financial year printed on this black-and-white cover?

**Golden answer:** It is the Indian Jute Mills Association auditor’s report, balance sheet and profit-and-loss statement for the year ended 31 March 2021. The cover names Jain & Co. as the chartered-accountant firm and gives Kolkata addresses.

**Citation source:** blobextra_0e46676491d6_balance_sheet_2020_21.pdf [source #013], original p. 1, merged PDF p. 877; framed cover title and lower “FROM: JAIN & CO.” block

### Turn 2 — High-Precision Extraction

**Question:** What unusual audit-procedure limitation is specifically stated under Key Audit Matters?

**Golden answer:** The auditor says regular audit/quality-control procedures were impacted; earlier in-person procedures could not be performed, and alternate procedures were used, including enquiries via phone/video/e-mail and review of scanned documents sent by e-mail, with original documents sighted afterward.

**Citation source:** blobextra_0e46676491d6_balance_sheet_2020_21.pdf [source #013], original p. 2, merged PDF p. 878; bottom “KEY AUDIT MATTERS” paragraph

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Does the scanned limitation paragraph itself say the financial statements received an adverse opinion?

**Golden answer:** No. The “OPINION” passage states the financial statements give the information required and a true and fair view for the year ended 31 March 2021, while “KEY AUDIT MATTERS” separately explains altered procedures. It is incorrect to treat that procedural disclosure alone as an adverse opinion.

**Citation source:** blobextra_0e46676491d6_balance_sheet_2020_21.pdf [source #013], original p. 2, merged PDF p. 878; upper OPINION paragraph and lower KEY AUDIT MATTERS paragraph

---

## scanned_session_18: Indian Tea Association FY2021: cash-basis reporting and signature layout

### Turn 1 — Summarization / Overview

**Question:** What reporting period and preparer are identified by the 2021 Indian Tea Association section?

**Golden answer:** The section is the Indian Tea Association Statement of Accounts for the year ended 31 March 2021. The following cover page names SBA Associates, Chartered Accountants, as the preparer.

**Citation source:** blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 1, merged PDF p. 904; title cover with fiscal year | blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 2, merged PDF p. 905; preparer box

### Turn 2 — High-Precision Extraction

**Question:** What balance-sheet totals are printed for 2021 and 2020?

**Golden answer:** The total Sources of Funds and Application of Funds are ₹13,06,78,345 as at 31 March 2021 and ₹12,19,82,697 as at 31 March 2020. Both sides are balanced to these same totals.

**Citation source:** blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 5, merged PDF p. 908; balance-sheet Total rows, 2021 and 2020 columns

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** Who signs this balance sheet, and where are their signatures compared with the auditor’s seal?

**Golden answer:** The bottom of the balance sheet has the SBA Associates auditor signature and round seal toward the left; to the right are association signature blocks for Vivek Goenka (Chairman) and Arijit Raha (Secretary General). The date appears by the auditor details at the lower-left region.

**Citation source:** blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 5, merged PDF p. 908; balance-sheet lower portion beneath Total rows, signatures, stamp and date

---

## scanned_session_19: Cross-document: Indian Tea Association reporting-period separation

### Turn 1 — Cross-Document Summarization

**Question:** Are the two Indian Tea Association PDFs duplicate copies of the same year’s accounts?

**Golden answer:** No. Source #014 is the Statement of Accounts for the year ended 31 March 2021, whereas source #012 is the financial statements as at 31 March 2024. The reporting years and their balance-sheet comparators differ.

**Citation source:** blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 1, merged PDF p. 904; FY2021 cover | blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 1, merged PDF p. 850; FY2024 cover

### Turn 2 — Cross-Document High-Precision Extraction

**Question:** What are the reported balance-sheet totals for those two distinct year-end dates?

**Golden answer:** For 31 March 2021 (#014): ₹13,06,78,345; for 31 March 2024 (#012): ₹10,86,43,595. These are the totals printed on the respective balance sheets. No claim about a continuous three-year trend can be established from just these two numbers.

**Citation source:** blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 5, merged PDF p. 908; 2021 balance sheet, Total rows | blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 5, merged PDF p. 854; 2024 balance sheet, Total rows

### Turn 3 — Visual & Multi-Hop Synthesis

**Question:** What visual details help keep the 2021 and 2024 sign-off pages from being mixed up?

**Golden answer:** Both have SBA Associates authentication, but the FY2021 page shows Vivek Goenka and Arijit Raha as chairman and secretary general, whereas the FY2024 page has its own later-year signatures and an auditor sign-off dated 01.08.2024. The correct page must be selected by reporting date and table header, not by the common auditor’s circular seal.

**Citation source:** blob_049_049_indian_tea_association__ita__original_ita_statement_of_accounts_for_the_year_ended_31st_march__2021.pdf [source #014], original p. 5, merged PDF p. 908; signature and 2021 date area | blob_123_123_indian_tea_association__ita__original_audited_accounts_for_fy_2023_24.pdf [source #012], original p. 5, merged PDF p. 854; date and signed blocks beneath FY2024 balance sheet

---

## scanned_session_20: Cross-document: audit scope versus management reporting scope

### Turn 1 — Cross-Document Summarization

**Question:** Do the AAQUARIES, Meso, and Twentyfirst Century scans all represent the same kind of audit assurance?

**Golden answer:** No. AAQUARIES labels its results provisional standalone; Meso labels its financial statements audited; Twentyfirst Century presents unaudited quarterly results with independent limited-review reports. Their titles and assurance descriptions must be preserved distinctly.

**Citation source:** AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 3, merged PDF p. 213; Provisional Standalone P&L title | Meso Private Limited.pdf [source #097], original p. 2, merged PDF p. 177; Audited Statement of Profit and Loss title | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 2, merged PDF p. 221; independent limited-review report | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 4, merged PDF p. 223; standalone unaudited quarter heading

### Turn 2 — Cross-Document High-Precision Extraction

**Question:** What are the respective financial reporting dates or periods in those three examples?

**Golden answer:** AAQUARIES is for the period ended 31 March 2023; Meso is for the period ended 31 March 2024; Twentyfirst Century’s quarterly results are for the quarter ended 30 June 2025.

**Citation source:** AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 3, merged PDF p. 213; P&L reporting-period heading | Meso Private Limited.pdf [source #097], original p. 2, merged PDF p. 177; P&L reporting-period heading | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 4, merged PDF p. 223; quarterly reporting-period table header

### Turn 3 — Cross-Document / Visual Reasoning

**Question:** What specific layout or document title clues would prevent an AI system from merging these figures into a single time series?

**Golden answer:** AAQUARIES uses a “Provisional Standalone” title and a blue company stamp; Meso uses yellow scanned paper, an “Audited” title and auditor/director seal blocks; Twentyfirst Century has company disclosure letters, independent review reports and separate standalone/consolidated quarterly tables. Those provenance and reporting-scope differences make a combined company time series invalid.

**Citation source:** AAQUARIES GLOABAL INDUSTRIES LIMITED.pdf [source #099], original p. 3, merged PDF p. 213; provisional title and blue seal | Meso Private Limited.pdf [source #097], original p. 2, merged PDF p. 177; yellow background and audited title, bottom stamps | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 1, merged PDF p. 220; submission letter | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 4, merged PDF p. 223; standalone result | 21STCENMGM_qr_29_07_2025_171051.pdf [source #100], original p. 7, merged PDF p. 226; consolidated result


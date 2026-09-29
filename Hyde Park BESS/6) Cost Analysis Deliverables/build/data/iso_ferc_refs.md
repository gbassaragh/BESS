# ISO / FERC / State-Regulatory Reference Data for Benchmarking a 10 MW / 20 MWh Utility-Owned, Distribution-Connected BESS (Boston, MA; Eversource; ISO-NE; COD Dec 2028)

Prepared 2026-09-29. Research constraint: the sandbox egress proxy blocked direct fetches of every primary host tried (lbl.gov, osti.gov, escholarship.org, ferc.gov, federalregister.gov, mass.gov, nyserda.ny.gov, dps.ny.gov, cpuc.ca.gov, pnnl.gov, nrel.gov/nlr.gov, eia.gov, lazard.com, brattle.com, masscec.com, iso-ne.com, aacei.org, sec.gov, catalyst.coop, plus trade press). All figures below therefore come from search-engine excerpts of those documents. Confidence tags reflect that: **High** = figure appeared verbatim in two or more independent excerpts or in the publisher's own abstract; **Medium** = single excerpt, or period/dollar-year ambiguous; **Low** = secondary-source paraphrase or derived by me. "NOT RETRIEVED" = the document exists and the URL is given, but the number could not be extracted this session. Dollar years are stated where the source stated them; otherwise marked "nominal/unstated".

Derived unit costs (marked "derived") are my arithmetic on the sourced totals and carry the lower of the inputs' confidence.

---

## Summary table (one page)

| # | Reference | Key figure(s) | $ year | Conf. |
|---|-----------|---------------|--------|-------|
| 1 | LBNL ISO-NE interconnection brief (Jun 2023; 194 projects, studies 2010–2021) | All resources: mean $225 → $422/kW, median $124 → $224/kW (2010-17 vs 2018-21). Withdrawn: mean $270 → $613, median $198 → $455. Complete: mean $134 → $114, median $58 → $104. **Storage median $3/kW (2010-17) → $148/kW (2018-21)**; storage all-status mean ≈ $230/kW; storage 85–200 MW median $148/kW. Network share: complete 31% (2010-17) / 3% (2018+), active 58%. | LBNL briefs report real $ (2022$ likely) – unstated in excerpts | High (medians), Medium ($ yr) |
| 1 | LBNL PJM brief (Jan 2023) | Storage mean, all statuses **$335/kW**; storage median across sample $63/kW; complete storage ≈ $4/kW; active+withdrawn storage/hybrids $337/kW. All-resource 2020-22: complete mean $84 / median $30; active mean $240 / median $85; withdrawn mean $599 / median $156. Network-upgrade means since 2019: complete $71, active $227, withdrawn $563/kW. | as above | High |
| 1 | LBNL MISO brief (Oct 2022) | Storage potential cost **$248/kW** (2018-21); gas $108, solar $209, wind $399. All-resource active $156/kW, withdrawn $452/kW. | as above | High |
| 1 | LBNL NYISO brief (Mar 2023) | All-resource mean $86 → $167/kW, median $66 → $115 (2006-16 vs 2017-21); complete mean $83 → $234; withdrawn mean $87 → $241. **Storage by size: 1–50 MW $76/kW; 50–100 MW $64; 100–250 MW $73; 250+ MW $32/kW.** | as above | High |
| 1 | LBNL SPP brief (Apr 2023; 845 projects) | Complete 2020-23 mean $106/kW, median $66; withdrawn $304/kW (2020s); **active storage $95/kW**; withdrawn network upgrades $388/kW = 85% of total. | as above | High |
| 1 | LBNL non-ISO BA brief (Feb 2026) | Complete 2018-24 mean $194/kW; storage active $57/kW, withdrawn $91/kW. | unstated | Medium |
| 1 | LBNL CAISO; ERCOT | CAISO data (2010–2023) exists in LBNL dataset; storage $/kW NOT RETRIEVED. ERCOT: no LBNL brief (connect-and-manage). | – | – |
| 1 | ISO-NE Transitional Cluster Study interim (Jun 2026) | 23 projects, ~4.8 GW, **~$3.2 B total interconnection cost; ~$2.5 B System Network Upgrades** (≈$1.8 B deliverability thermal, ≈$0.5 B energy); avg ≈ $664 k/MW (= **$664/kW**); WCMA ≈ 2,000 MW/8 projects > $1,000/kW; SEMA ≈ 1,460 MW/5 projects ≈ $177/kW. 21 of 26 qualified requests are BESS. Allocation: pro-rata MW share (Summer NRC). | nominal (2026) | High (totals), Medium (zonal) |
| 2 | FERC Order 898 (RM21-11; FR 88 FR 68,946, Oct 5 2023) | New USofA plant accounts **348 (production), 351 (transmission), 363 (distribution)** "Energy Storage Equipment"; O&M 548.1/553.1, 562.1/570.1, 582.1/592.2; mandatory from **Jan 1 2025** → first Form 1 with separated storage plant = FY2025 filings (Apr 2026). | – | High |
| 2 | MISO SATOA, Waupaca (MTEP20, ATC) | $8.1 M for 2.5 MW / 5 MWh Li-ion + 14 MVAR caps vs $11.3 M 115 kV rebuild → derived ≈ $3,240/kW, $1,620/kWh (hybrid, includes caps). FERC accepted MISO SATOA tariff ER20-588 (170 FERC ¶ 61,186, 2020). | nominal 2020 | High ($), Low (derived) |
| 2 | Other FERC | Western Grid 130 FERC ¶ 61,056 (2010) – storage as transmission; PL17-2 Policy Statement (2017) dual cost/market recovery; SPP SATOA accepted May 2023. FERC-approved rate-base storage projects with public $ and MW/MWh beyond Waupaca: NOT RETRIEVED. | – | Medium |
| 3 | MA DPU 17-05 – Eversource Outer Cape/Provincetown | 24.9 MW / 38 MWh, **≈ $40 M**, in service Dec 2022 → derived ≈ $1,606/kW, $1,053/kWh. | nominal 2019–22 | High ($40 M), Low (derived) |
| 3 | MA DPU 17-13 – National Grid Nantucket | 6 MW / 48 MWh Tesla, **≈ $81 M** (2019) → derived $13,500/kW, $1,688/kWh (8-h, island, plus site works). | nominal 2019 | Medium |
| 3 | MA ESMP D.P.U. 24-10/24-11 | Eversource proposed 1 MW / 2 MWh mobile BESS (Springfield); NG spending cap $569.96 M; storage line-item $ NOT RETRIEVED. | – | Medium |
| 3 | MA §83E Round I (2025-26) | 1,268 MW selected; 1,068 MW filed at DPU Jul 2 2026 (Trimount 700 MW, Energizar 250, Salt Cod 168); River Mill 500 MW/2,000 MWh withdrew citing TCS upgrade costs; bid cap 97.75% of Clean Peak ACP; claimed $516 M ratepayer savings; contract prices confidential – NOT RETRIEVED. Round II (D.P.U. 26-75): 1,000 MW incl. distribution-connected carve-out. | – | Medium |
| 3 | NY PSC 18-E-0130 / NYSERDA | Bulk incentive schedule **$110/kWh (2019) → $50/kWh (2025)** stepping $10/yr; 2024 Roadmap incentive NPV bulk $701.5 M–$1.42 B; **State of Storage (Dec 2025): bulk (>5 MW) avg installed $524/kWh; retail FTM standalone $666/kWh**; Con Ed dispatch-rights contracts ≥300 MW, up to 15 yr, prices confidential – NOT RETRIEVED. | nominal | High ($524/$666, schedule) |
| 3 | CPUC utility-owned | SCE/Ameresco EPC+maintenance **$1.226 B for 537.5 MW / 2,150 MWh** (2021) → derived $2,281/kW, $570/kWh; SDG&E Westside Canal 2a $267.9 M / 119 MW → $2,251/kW (MWh n/r); PG&E Elkhorn 182.5 MW/730 MWh cost confidential; 2021-22 revenue requirement $80.248 M (Res. E-4949). | nominal 2021 | High (SCE), Medium (others) |
| 3 | HI PUC Docket 2020-0132 – HECO Waena | 40 MW / 160 MWh self-build; est. $60 M; **PUC-approved cap $82 M** (Dec 2023); increase requested for tariffs → derived $1,500–2,050/kW, $375–513/kWh. | nominal | High |
| 3 | CT PURA 17-12-03RE03 | 2021 decision: residential upfront ≈ $250/kWh (cap $7,500); C&I upfront capped at 50% of cost. 2025 commercial upfront $280–450/kWh (per CT Green Bank). From Apr 1 2026: performance $325/kW yrs 1-5, $175/kW yrs 6-10 (small/med C&I); $275 / $175 (large C&I). | nominal | Medium |
| 3 | NJ BPU GSESP Tranche 1 (Mar 4 2026) | 355 MW awarded; **$413.6 M over 15 yr**: Woods Landing 200 MW $15 M/yr (= $75/kW-yr), Two Rivers 150 MW $12.28 M/yr (= $82/kW-yr), NAES 5 MW $0.3 M/yr (= $60/kW-yr). | nominal | High |
| 4 | NREL Cost Projections 2023 Update (4-h, 2022$) | 2030: $245 / $326 / $403 per kWh (low/mid/high); 2050: $159 / $226 / $348; 2028 mid ≈ $351/kWh. | 2022$ | High |
| 4 | NREL Cost Projections 2025 Update (4-h) | 2035: $152 / $247 / $349 per kWh; 2050: $111 / $184 / $333. | 2023$ (likely) | Medium |
| 4 | NREL ATB 2024 | 60 MW reference; durations 2/4/6/8/10 h; CAPEX($/kW) = pack($/kWh)×h + BOS($/kW); 2022→2035 CAPEX −18% / −37% / −52% (Cons/Mod/Adv). Base-year $/kW NOT RETRIEVED. | 2022$ | High (method) |
| 4 | Modo Energy global capex survey (Sep 2026) | Median 2-h **$325/kWh**, 4-h **$201/kWh**; "doubling duration cuts 38% per MWh". | 2026 nominal | Medium |
| 4 | Lazard LCOE+ Jun 2025 | 100 MW 4-h LCOS $115–254/MWh (no ITC), $83–192 (ITC); 2-h $129–277/MWh. Capital-cost $/kWh NOT RETRIEVED. | 2025 nominal | Medium |
| 4 | EIA AEO2025 (S&L capital-cost study, Case 19: 150 MW / 600 MWh) | Overnight $/kW and New England regional multiplier NOT RETRIEVED (URL given). | 2024$ | – |
| 4 | Brattle NE Duration Study (Feb 2024); E3 Charging Forward (Dec 2023) | Cost assumptions NOT RETRIEVED (URLs given). | – | – |
| 5 | Scale/duration | LBNL NYISO storage $/kW by size (above); LBNL ISO-NE "economies of scale exist for solar and possibly storage"; Sovacool & Ryu 2025 diseconomy breakpoints 1,280 MW and 1,561 MW; PNNL database grid = 1/10/100/1000 MW × 2/4/6/8/10/24/100 h – values NOT RETRIEVED. | – | Medium |
| 6 | AACE RPs (titles verified) | 17R-97, 18R-97, 96R-18, 40R-08, 41R-08, 42R-08, 44R-08, 57R-09, 58R-10, 62R-11, 63R-11, 65R-11, 66R-11, 68R-11, 113R-20 (see §6 for exact titles). | – | High |
| 6 | Cost-overrun base rates | Flyvbjerg (16,000+ projects): 47.9% on budget; 8.5% on budget+time; 0.5% budget+time+benefits. Energy: solar +1%, wind +13%, transmission +8%, fossil +16%, hydro +75%, nuclear +120%. Sovacool 2014 (401 projects): mean +66.3%; Sovacool & Ryu 2025 (662 projects): mean +40.6%; nuclear +102.5%, hydro +36.7%, geothermal +20.7%, CCS +14.9%, bioenergy +10.7%, fossil +9.7%, wind +5.2%, solar −2.2%, transmission −3.6%. Battery-specific: ~+6% mean (secondary cite of Oxford database; Low). ACCURE 2025: 19% of >10 MWh BESS had revenue-reducing operational faults. | – | High (Flyvbjerg/Sovacool), Low (battery 6%) |

---

## 1. ISO/RTO interconnection cost distributions (LBNL series) and ISO-NE specifics

### 1.1 What the LBNL series measures
LBNL's "Generator Interconnection Costs to the Transmission System" series (emp.lbl.gov/interconnection_costs) compiles project-level cost estimates from ISO interconnection studies (2,500+ estimates across MISO, PJM, SPP, NYISO, ISO-NE; CAISO added later; 2010–2023 study years; non-ISO BAs added Feb 2026). Costs are split into **POI** (interconnection facilities and the interconnecting substation) and **network** (upgrades beyond the POI substation, incl. shared/affected-system upgrades). Projects are grouped by status: **complete** (all studies done / in service), **active**, **withdrawn**. Consistent finding across all ISOs: withdrawn > active > complete, and network upgrades drive the escalation. Dollar year: LBNL briefs normalize to real dollars (2022$ for the 2022–23 briefs) — **Medium** confidence on the exact base year because excerpts did not state it.

### 1.2 ISO-NE — "Interconnection Cost Analysis in ISO-New England" (LBNL, June 2023; 194 projects, studies 2010–2021)
- All resources, 2010-17 → 2018-21: **mean $225 → $422/kW; median $124 → $224/kW**. (High)
- Withdrawn: mean $270 → $613/kW; median $198 → $455/kW (×2.3). (High)
- Complete: mean $134 → $114/kW; median $58 → $104/kW ("lack a clear trend due to small n in latter period"). (High)
- By resource (2018-21 means): onshore wind $909/kW, solar $450/kW, **storage $230/kW**; gas and offshore wind lower. (Medium – period inferred)
- **Storage median: $3/kW (2010-17) → $148/kW (2018-21)**; storage in the 85–200 MW bin median $148/kW (Fig. 8). (High)
- POI vs network: complete projects mostly POI (network = 31% of total for 2010-17 completes; 3% for the single 2018+ complete); active projects ≈ 58% network; withdrawn ≈ 50/50. (High)
- Scale: "economies of scale exist for solar and possibly storage projects." (High)
- Storage-specific mean/withdrawn split by status: NOT RETRIEVED (in the brief's Fig. 7/8; PDF blocked).
- URLs: https://emp.lbl.gov/publications/interconnection-cost-analysis-iso-new ; PDF https://eta-publications.lbl.gov/sites/default/files/iso-ne_interconnection_costs_vfinal.pdf ; OSTI 1986022; mirror https://escholarship.org/content/qt0919400z/qt0919400z.pdf

### 1.3 PJM — "Interconnection Cost Analysis in the PJM Territory" (LBNL, Jan 2023)
- Sample: solar 649, solar+storage hybrid 131, **storage 114**, gas 105, onshore wind 88, offshore wind 11.
- **Storage mean across all statuses $335/kW** (vs gas $24, solar $253, onshore wind $136, offshore $385). (High)
- Storage median across the sample $63/kW; complete standalone storage ≈ $4/kW (mean) and median fell $14 → $0/kW; active+withdrawn storage and solar hybrids ≈ $337/kW. (High)
- All-resource by status: complete mean $42 → $84/kW, median $18 → $30 (2000-19 vs 2020-22); active mean $29 → $240, median $8 → $85 (2017-19 vs 2020-22); withdrawn 2020-22 mean $599, median $156/kW. (High)
- Network upgrades (beyond POI substation), means since 2019: complete $71, active $227, withdrawn $563/kW. Medians 2017-22: complete POI $3 / network $16; active POI $7 / network $68. (High)
- Tail: 95% of 2020-22 completes < $200/kW; cluster ≈ $400/kW; one outlier $3,728/kW. (High)
- URLs: https://emp.lbl.gov/publications/interconnection-cost-analysis-pjm ; https://emp.lbl.gov/news/pjm-data-show-substantial-increases ; OSTI 1922201; Utility Dive summary https://www.utilitydive.com/news/PJM-generator-interconnection-costs-network-upgrades-berkeley-study/640824/

### 1.4 MISO — "Generator Interconnection Cost Analysis in MISO" (LBNL, Oct 2022; ~50% of 2010–2020 requests)
- Potential (all-status) 2018-21: **storage $248/kW**, wind $399, solar $209, gas $108. (High)
- All-resource: active $156/kW; withdrawn $452/kW (mean). (High)
- Storage by status: NOT RETRIEVED (an excerpt gave complete $52 ± 12, active $72, withdrawn $102 ± 19 /kW but attribution to MISO vs. the 2026 non-ISO brief is ambiguous — Low; do not cite without checking the PDF).
- URLs: https://emp.lbl.gov/publications/generator-interconnection-cost ; PDF https://eta-publications.lbl.gov/sites/default/files/berkeley_lab_2022.10.06-_miso_interconnection_costs.pdf ; OSTI 1891311; ICC mirror https://icc.illinois.gov/docket/P2024-0088/documents/356795/files/625240.pdf

### 1.5 NYISO — "Interconnection Cost Analysis in the NYISO Territory" (LBNL, Mar 2023; ≥43% of 2003–2019 requests)
- All resources 2006-16 → 2017-21: mean $86 → $167/kW; median $66 → $115/kW. Complete: mean $83 → $234, median $67 → $150. Withdrawn: mean $87 → $241, median $66 → $129. Active: above historical but below complete/withdrawn. (High)
- **Storage by size (mean $/kW): 1–50 MW $76; 50–100 MW $64; 100–250 MW $73; 250+ MW $32.** (High) — the only ISO-level storage size gradient retrieved; use for a scale adjustment on interconnection only.
- URLs: https://emp.lbl.gov/publications/interconnection-cost-analysis-nyiso ; PDF https://eta-publications.lbl.gov/sites/default/files/nyiso_interconnection_costs_vfinal.pdf

### 1.6 SPP — "Generator Interconnection Cost Analysis in SPP" (LBNL, Apr 2023; 845 projects, 2002–2023)
- Complete 2020-23: mean $106/kW, median $66/kW. Withdrawn: $22 (2000s) → $247 (2010s) → $304/kW (2020s); withdrawn ≈ 5× complete; network upgrades in withdrawn $388/kW = 85% of total. (High)
- **Active storage $95/kW** (below withdrawn, above complete). (High)
- URLs: https://emp.lbl.gov/publications/generator-interconnection-cost-0 ; OSTI 1971633; https://emp.lbl.gov/news/spp-data-show-rising-network-upgrade

### 1.7 CAISO, ERCOT, non-ISO BAs
- CAISO: LBNL states cleaned CAISO cost data (studies 2010–2023) are on the data page; storage $/kW NOT RETRIEVED. https://emp.lbl.gov/interconnection_costs
- ERCOT: not covered by LBNL (connect-and-manage; network upgrades socialized). NOT RETRIEVED.
- Non-ISO BAs (BPA, PacifiCorp, Duke DEC/DEP/DEF), LBNL Feb 2026: complete 2018-24 mean $194/kW; storage active $57/kW, withdrawn $91/kW. (Medium) https://eta-publications.lbl.gov/sites/default/files/2026-02/lbnl_2026.02.23_ba_interconnection_costs.pdf

### 1.8 ISO-NE Transitional Cluster Study (TCS) — the most relevant current datapoint
- First cluster study under FERC Order 2023 compliance; launched Oct 2025; interim results June 2026; developer response window to July 7 2026; final due Aug 6 2026 (tariff). (High)
- 26 requests qualified (21 BESS, 2 solar, 3 wind); most in MA, two each CT/ME/VT, one NH. Interim report covers 23 projects ≈ 4.8 GW. (High)
- **Total interconnection cost ≈ $3.2 B; System Network Upgrades ≈ $2.5 B**, of which ≈ $1.8 B deliverability (thermal) upgrades and ≈ $0.5 B energy upgrades. Average quoted as ≈ $664 k/MW (= **$664/kW**; my check: $3.2 B / 4.8 GW = $667/kW; SNU-only $2.5 B / 4.8 GW = $521/kW). (High for totals; Medium for the per-MW basis)
- Zonal: **WCMA ≈ 2,000 MW over 8 projects > $1,000/kW** (≈ $1.5 B thermal upgrades); **SEMA ≈ 1,460 MW over 5 projects ≈ $177/kW**. NEMA/Boston-specific figure NOT RETRIEVED. (Medium)
- Cost allocation: network upgrades allocated **pro rata by MW share of cluster requests, using Summer Network Resource Capability**; reactive/substation additions beyond POI allocated proportionally. Withdrawal penalties / readiness deposits: NOT RETRIEVED (Ask-ISO article blocked). (Medium)
- Consequence already observed: River Mill Storage (500 MW / 2,000 MWh, an §83E Round I selection) deferred/withdrew citing interim TCS upgrade costs; Massachusetts (letter of June 25 2026) expressed "deep concern" at >$3 B of upgrades falling mainly on MA BESS. (High)
- Relevance to a 10 MW distribution-connected project: these costs apply to transmission-level (≥ ~20 MW under ISO-NE Schedule 22/23 thresholds) requests. A distribution-connected 10 MW unit in Eversource territory is studied by the EDC (MA DPU interconnection tariff / Group Study process) rather than in the ISO cluster, but affected-system (ISO-NE Section I.3.9 / Schedule 23) review can still assign upgrade costs; the TCS figures are the right reference class for the "if it had been transmission-connected" comparison.
- URLs: https://www.mass.gov/doc/letter-to-iso-ne-on-transitional-cluster-study-interim-results-june-25-2026/download ; https://www.mass.gov/doc/transitional-cluster-study-presentation-72326/download ; https://epeconsulting.com/epe-intelligence/news/iso-nes-transitional-cluster-study-tc2-results-are-in-what-developers-need-to-know ; https://askiso.iso-ne.com/s/article/Cost-Allocation-for-the-Transitional-Cluster-Study ; https://isonewswire.com/2025/10/20/iso-ne-begins-interconnection-transitional-cluster-study/ ; https://www.rtoinsider.com/118175-storage-projects-dominate-iso-ne-cluster-study/ ; https://www.iso-ne.com/committees/key-projects/order-no-2023-key-project ; https://www.iso-ne.com/static-assets/documents/100013/order-2023-transition-faq.pdf

---

## 2. FERC: accounting, Form 1 extractability, storage-as-transmission cost data

### 2.1 Order No. 898 — Accounting and Reporting Treatment of Certain Renewable Energy Assets (Docket RM21-11-000; issued June 2023; 88 FR 68946, Oct 5 2023)
- Creates an **Energy Storage** function and plant accounts: **348 Energy Storage Equipment—Production; 351 Energy Storage Equipment—Transmission; 363 Energy Storage Equipment—Distribution.** (High)
- O&M: 548.1 / 553.1 (operation / maintenance, production); 562.1 / 570.1 (transmission); 582.1 / 592.2 (distribution). (High)
- Compliance effective **January 1, 2025**, prospective; legacy accounts cease for storage plant from that date. ISO-NE PTOs made an Order 898 compliance filing (Transmission Committee presentation). (High)
- Implication for benchmarking: the **first FERC Form 1 filings that segregate storage plant by function are FY2025 (filed ~April 2026)**; earlier storage capital sits inside generic accounts (e.g., 344/345/346 for production, 353/362 for T/D) and is not separable. Form 1 does not report MW/MWh for storage plant, so $/kW from Form 1 requires pairing with EIA-860 (Schedule 3.4 energy storage) by plant name. (Medium – inference)
- Extractability: Form 1 XBRL (2021+) and DBF (1994–2020) are parsed by **PUDL (Catalyst Cooperative)** — plant-in-service by account tables exist; account-348/351/363 columns will appear only once FY2025 XBRL is ingested. https://docs.catalyst.coop/pudl/en/stable/data_sources/ferc1.html ; raw archive https://zenodo.org/records/21860241. FERC eForms: https://www.ferc.gov/filing-forms/eforms-refresh. (Medium)
- URLs: https://www.ferc.gov/media/order-no-898 ; https://www.federalregister.gov/documents/2023/10/05/2023-14994/accounting-and-reporting-treatment-of-certain-renewable-energy-assets ; https://www.iso-ne.com/static-assets/documents/100027/a02_tc_pto_ac_order898_compliance_presentation.pdf ; https://www.troutman.com/insights/ferc-establishes-revised-accounting-rules-to-address-renewables-storage-and-recs/

### 2.2 Storage as transmission asset (SATA/SATOA) — filed cost data
- **Western Grid Development, 130 FERC ¶ 61,056 (Jan 2010)**: first holding that batteries supporting transmission are transmission facilities eligible for rate incentives (CAISO). $ NOT RETRIEVED. https://ferc.gov/sites/default/files/2020-04/E-6_14.pdf (High on holding)
- **Policy Statement PL17-2-000 (Jan 2017)**: storage may recover cost-based transmission rates and market revenues concurrently, with safeguards. (High)
- **MISO SATOA tariff, Docket ER20-588, 170 FERC ¶ 61,186 (Mar 2020)**; MISO Waupaca Area Storage Project (ATC), MTEP20 Appendix A (Dec 2020): **$8.1 M, 2.5 MW / 5 MWh Li-ion plus 14 MVAR capacitors vs $11.3 M double-circuit 115 kV rebuild** → derived $3,240/kW, $1,620/kWh (hybrid; small scale; nominal 2020). (High for $; Low for derived unit cost) https://www.ferc.gov/sites/default/files/2020-05/20200310135710-ER20-588-000.pdf ; https://www.misoenergy.org/engage/MISO-Dashboard/storage-as-transmission-only-asset/ ; https://www.sandia.gov/app/uploads/sites/273/2024/06/3_McKee_Bob_ATC_ICC_Session5_1-11-2022.pdf ; https://www.renewableenergyworld.com/power-grid/transmission/miso-leads-the-way-with-energy-storage-as-a-transmission-only-asset-satoa/
- **SPP SATOA framework accepted by FERC May 2023** (cost allocation/recovery, planning, interconnection, market participation). $ examples NOT RETRIEVED. https://www.troutmanenergyreport.com/2023/06/ferc-approves-spp-proposal-for-energy-storage-to-be-considered-transmission-only-assets/
- **NYISO storage-as-transmission evaluation**: press summary cites a 200 MW / 200 MWh BESS alternative at ≈ $120 M vs ≈ $700 M for the wires solution (→ $600/kW, 1-h; Low). https://www.nyiso.com/documents/20142/38699263/Storage%20as%20Transmission%20-%20Introduction.pdf ; https://www.energy-storage.news/nyiso-studies-unique-characteristics-of-energy-storage-as-a-transmission-asset/ ; NY-BEST SATA white paper https://cdn.ymaws.com/ny-best.org/resource/resmgr/reports/SATA_White_Paper_Final_01092.pdf (content NOT RETRIEVED)
- PJM, AEP, Xcel, ITC, National Grid, Eversource FERC formula-rate storage projects with public $/MW/MWh: **NOT RETRIEVED** (no public docket-level cost found in excerpts). Related state-jurisdictional datapoint: Xcel MN utility-owned distribution storage/VPP, 200 MW of 1–3 MW units by 2028, filed budget **$152–430 M** (→ $760–2,150/kW; Medium). https://www.utilitydive.com/news/minnesota-approves-xcels-controversial-utility-owned-virtual-power-plant/816673/
- Order 841 (2018) / 2222 (2020) bear on revenue stacking, not on capital cost; no cost content retrieved and none needed for the benchmark.
- Context article on SATA under-use: https://www.utilitydive.com/news/energy-storage-underused-transmission-asset-ferc/727946/

---

## 3. State-regulator storage cost references

### 3.1 Massachusetts DPU
- **D.P.U. 17-05 (Eversource rate case, 2017)** approved the Outer Cape BESS as the least-cost alternative to a 13-mile distribution line through the National Seashore. Built: **24.9 MW / 38 MWh Li-ion, ≈ $40 M**, in service Dec 1 2022 (backup for ~11,000 customers). Derived ≈ **$1,606/kW; $1,053/kWh** (1.5-h; includes microgrid/islanding scope; nominal 2019–22). (High on $40 M via Utility Dive/ICAST/power-technology; Low on derived) https://www.utilitydive.com/news/eversource-advances-cape-cod-battery-project-defers-13-mile-distribution-l/552171/ ; https://www.tdworld.com/distributed-energy-resources/energy-storage/article/21250829/ ; https://www.power-technology.com/marketdata/outer-cape-battery-energy-storage-system-us/ ; https://www.mass.gov/info-details/utility-owned-large-scale-battery-energy-storage
- **D.P.U. 17-13 (National Grid rate case)** – Nantucket BESS: **6 MW / 48 MWh Tesla, ≈ $81 M** (2019), defers ~$120 M third submarine cable. Derived $13,500/kW; $1,688/kWh (8-h; island logistics). (Medium) https://www.utilitydive.com/news/Tesla-national-grid-battery-energy-storage-8hour-long-duration-diesel-generation-system-nantucket/564428/ ; https://www.wbur.org/news/2019/10/08/nantucket-energy-storage-lithium-ion-giant-battery
- **ESMPs D.P.U. 24-10 (Eversource) / 24-11 (National Grid) / 24-12 (Unitil)**: filed Jan 29 2024, approved with modification Aug 29 2024 (Phase II order 2025); term Jul 1 2025–Jun 30 2030; Eversource ESMP includes a **1 MW / 2 MWh mobile BESS (Springfield)**; NG cost-recovery cap $569.96 M; Companies proposed > $2.5 B total. **Storage line-item $ NOT RETRIEVED.** https://www.mass.gov/doc/esmp-phase-ii-order/download ; https://electricgrid.mass.gov/wp-content/uploads/2025/07/D.P.U.-24-10-11-12-ESMP-Final-Order-8.29.24.pdf ; https://www.eversource.com/business/about/sustainability/renewable-generation/mobile-battery-energy-storage-system
- **§83E procurement (2024 climate law; 5,000 MW by Jul 31 2030)**: Round I (D.P.U. 25-xx RFP, bids Sep 10 2025; 13 bids ≈ 1,500 MW, all transmission-connected, 40–1,000 MW, 4–10 h): DOER selected 1,268 MW (Energizar 250, River Mill 500/2,000 MWh, Trimount 700, Salt Cod 168); **1,068 MW of contracts filed Jul 2 2026** (River Mill dropped after TCS interim costs); bid cap **97.75% of Clean Peak ACP**; DOER claims $516 M direct savings. Contract prices: **confidential – NOT RETRIEVED.** Round II RFP (D.P.U. 26-75, Jul 31 2026): 1,000 MW with a **distribution-connected carve-out** — directly relevant precedent for a 10 MW distribution BESS. https://macleanenergy.com/83e/ ; https://macleanenergy.com/wp-content/uploads/2026/05/attachment-a-section-83e-round2-rfp-dpu-26-75.pdf ; https://foleyhoag.com/news-and-insights/blogs/energy-and-climate-counsel/2025/september/massachusetts-energy-storage-procurement-underway/ ; https://cleanpeakmarketoutlook.com/massachusetts-83e-round-i-energy-storage-dpu/ ; https://mgrid.org/2026/08/08/massachusetts-83e-round-2-rfp-1000mw-storage-distribution-connected-carve-out/ ; https://www.utilitydive.com/news/massachusetts-utilities-dpu-contracts-energy-storage/824614/
- Other MA: Governor's EO 654 (Mar 16 2026) — 5,000 MW online/under development by 2035. DOE GRIP award ≈ $19.5 M to an Eversource BESS (Medium; https://www.renewableenergyworld.com/energy-storage/battery/innovative-eversource-battery-energy-storage-system-attracts-19-5m-from-doe/).

### 3.2 New York PSC / NYSERDA (Case 18-E-0130)
- 2018 Roadmap (E3/NYSERDA, Jun 2018; PSC order Dec 2018): 1,500 MW by 2025 / 3,000 MW by 2030; projected ≈ $150/kWh reduction for bulk/distribution systems by 2025 vs 2017-18; a later state citation used BNEF ≈ **$175/kWh by 2030** for large turnkey 4-h AC systems (Low – secondary). https://www.ethree.com/wp-content/uploads/2018/06/NYS-Energy-Storage-Roadmap-6.21.2018.pdf
- **Bulk Storage Incentive (PON 4139), > 5 MW**: **$110/kWh (2019 applications), $100 (2020), $90 (2021), $80 (2022), $70 (2023), $60 (2024), $50 (2025)**; $150 M bulk budget of $400 M total; program closed 2023. (High) https://www.nyserda.ny.gov/All-Programs/Energy-Storage-Program/Developers-and-Contractors/Bulk-Storage-Incentives ; data https://data.ny.gov/Energy-Environment/Retail-and-Bulk-Energy-Storage-Incentive-Programs-/ugya-enpy
- **6 GW Roadmap (Dec 2022 → PSC order Jun 20 2024)**: bulk program NPV estimate rose from $474 M–$1.19 B (2022 NPV) to **$701.5 M–$1.42 B (2024 NPV)**; Index Storage Credit RFP ISCRFP25-1 (Jul 28 2025) drew 46 bids ≈ 6 GW / 30 GWh; **Sept 23 2026 awards: 8 bulk projects, 950 MW** (prices NOT RETRIEVED). https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/ny-6-gw-energy-storage-roadmap.pdf ; https://www.utilitydive.com/news/up-to-300m-more-required-for-2030-energy-storage-goal-new-york-road-map/711619/ ; https://www.nyserda.ny.gov/About/Newsroom/2026-Announcements/2026-09-23-NYSERDA-Awards-Eight-Bulk-Energy-Storage-Projects-13-LSR-Projects
- **State of Storage in New York (annual report; as of Dec 2025): incentivized bulk (> 5 MW, wholesale) average total installed cost $524/kWh; FTM retail standalone average $666/kWh.** (High) https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BF0A94A9D-0000-CD3F-AD54-1B3672D3EA91%7D&DocTitle=State+of+Storage
- **Utility bulk dispatch-rights contracts**: PSC directed CECONY ≥ 300 MW, O&R ≥ 10 MW (also NG-NY, Central Hudson, others; 350 MW total, deadline extended); contract term raised 10 → 15 yr; in-service deadline moved to Dec 31 2028 then 2030; 2022 and 2024 solicitations closed, 2026 one-phase transmission-connected solicitation open; earlier rounds executed 120 MW (100 MW Con Ed, 20 MW NG). **$/kW-month prices NOT RETRIEVED (confidential).** Con Ed Ozone Park utility-owned 2 MW / 11 MWh (cost NOT RETRIEVED). https://www.coned.com/en/business-partners/business-opportunities/bulk-energy-storage-request-for-proposals ; https://www.coned.com/-/media/files/coned/documents/business-partners/business-opportunities/bulk-energy-storage/2024/bulk-storage-request-for-proposals.pdf ; https://www.utilitydive.com/news/storage-new-york-public-service-commission-con-edison-central-hudson/645628/ ; https://documents.dps.ny.gov/public/MatterManagement/CaseMaster.aspx?MatterCaseNo=18-E-0130

### 3.3 California CPUC (utility-owned)
- **SCE / Ameresco EPC + maintenance: $1.226 B, 537.5 MW / 2,150 MWh** at Springvale (225 MW), Hinson (200), Etiwanda (112.5) — CPUC approved Dec 2021 (Resolution, Dec 17 2021). Derived **$2,281/kW; $570/kWh** (4-h; includes maintenance scope; nominal 2021). (High) https://www.cpuc.ca.gov/news-and-updates/all-news/cpuc-approves-energy-storage-contract-for-sce ; https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M432/K713/432713159.PDF ; https://www.utilitydive.com/news/sces-12b-grid-reliability-storage-contract-receives-approval-from-regula/611765/
- **PG&E Elkhorn (Moss Landing) 182.5 MW / 730 MWh**, utility-owned, CPUC Res. E-4949 (Nov 2018); capex confidential; **2021–22 revenue requirement $80.248 M** ($41.204 M + $39.044 M). (Medium) https://docs.cpuc.ca.gov/publisheddocs/published/g000/m240/k050/240050937.pdf
- **SDG&E Westside Canal Phase 2a: $267.9 M, 119 MW incremental**, online Dec 2024 (→ $2,251/kW; MWh NOT RETRIEVED; Medium). SDG&E also owns Top Gun 30 MW, Kearny 20 MW, Fallbrook 40 MW ($ NOT RETRIEVED). https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M606/K399/606399033.PDF ; https://www.sdge.com/sites/default/files/S2450002-EnergyStorageMap-FLYER-FINAL%2003.21.24.pdf
- PG&E owned 183 MW / contracted 3,024 MW operational storage at Dec 31 2025 (10-K). CPUC Mid-Term Reliability (D.21-06-035 et seq.) cost assumptions and Lumen storage procurement study: https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/energy-storage/2023-05-31_lumen_energy-storage-procurement-study-report-attb.pdf (values NOT RETRIEVED).

### 3.4 Hawaii PUC — HECO self-build
- **Waena BESS, Maui, 40 MW / 160 MWh (Docket 2020-0132; D&O Dec 22 2023)**: estimate ≈ $60 M; **PUC-approved cost cap $82 M**; 2025 request to raise cap for tariff exposure; Tesla Megapacks; construction Jan 2026; COD 2027; enables retirement of 4 Kahului units. Derived $1,500–2,050/kW; $375–513/kWh. (High) https://www.hawaiianelectric.com/hawaiian-electric-to-begin-construction-of-first-standalone-load-shifting-battery-energy-storage-system-on-maui ; https://www.energy-storage.news/hawaiian-electric-requests-funds-with-tariffs-expected-to-drive-up-cost-of-tesla-bess/ ; https://www.hawaiianelectric.com/documents/about_us/investing_in_the_future/20200908_docket_20200132_ME_application.pdf

### 3.5 Connecticut PURA — Docket 17-12-03RE03 (Energy Storage Solutions)
- Final Decision Jul 28 2021: 9-year program, 580 MW by 2030 (1,000 MW statutory); **residential upfront ≈ $250/kWh (cap $7,500); C&I upfront capped at 50% of system cost**; plus performance incentives. (High) https://portal.ct.gov/-/media/PURA/electric/Final-Decision-Docket-No-17-12-03RE03.pdf
- 2025 commercial tranche: upfront **$280–450/kWh** depending on size/location/grid need (Medium; CT Green Bank/EticaAG). 2026 revision (effective Apr 1 2026): smaller enrollment incentive + performance **$325/kW yrs 1–5, $175/kW yrs 6–10 (small/medium C&I); $275 / $175 (large C&I)**. (Medium) https://www.ctgreenbank.com/connecticuts-energy-storage-solutions-program-updates-2026ratepayers-and-customers/ ; https://energystoragect.com/wp-content/uploads/2026/02/ESS-Program-Manual-Revised-for-02112026-CLEAN.pdf ; https://www.utilitydive.com/news/connecticut-energy-storage-battery-incentives-eversource-united-illuminating-pura/705273/

### 3.6 New Jersey BPU — Garden State Energy Storage Program (Order Jun 18 2025; awards Mar 4 2026)
- 2,000 MW by 2030; Phase 1 Tranche 1 = transmission-scale grid-supply, pay-as-bid **$/MW-year for 15 years**. Awards: **Woods Landing 200 MW $15 M/yr ($75/kW-yr); Two Rivers 150 MW $12.28 M/yr ($82/kW-yr); NAES Bordentown 5 MW $0.30 M/yr ($60/kW-yr); total $413.6 M over 15 yr; 355 MW**; Tranche 2 seeks 645 MW. (High) https://www.nj.gov/bpu/pdf/boardorders/2026/20260304/8A%20ORDER%20GSESP%20Phase%201%20Tranche%201.pdf ; https://www.nj.gov/bpu/pdf/boardorders/2025/20250618/8E%20ORDER%20Garden%20State%20Energy%20Storage%20Program.pdf ; https://mgrid.org/2026/03/05/nj-bpu-awards-413-6-million-to-355-mw-of-battery-storage-projects-including-jupiter-powers-woods-landing/ ; https://www.utilitydive.com/news/new-jersey-announces-355-mw-storage-procurement-solicits-645-mw-more/814971/

---

## 4. Program-level $/kW–$/kWh references regulators have accepted

| Source | Figure | $ yr | Conf. | URL |
|---|---|---|---|---|
| NYSERDA State of Storage (Dec 2025) | Bulk > 5 MW avg installed **$524/kWh**; retail FTM standalone **$666/kWh** | nominal | High | documents.dps.ny.gov (see §3.2) |
| NYSERDA bulk incentive schedule | $110 → $50/kWh (2019–2025) | nominal | High | see §3.2 |
| NY 6 GW Roadmap (2024) | Bulk incentive NPV $701.5 M–$1.42 B | 2024 NPV | High | see §3.2 |
| NREL Cost Projections 2023 Update (Cole & Karmakar) | 4-h: 2030 $245/$326/$403 per kWh; 2050 $159/$226/$348; 2028 mid ≈ $351/kWh | 2022$ | High | https://docs.nrel.gov/docs/fy23osti/85332.pdf |
| NREL Cost Projections 2025 Update (Cole, Ramasamy, Turan, Jun 2025) | 4-h: 2035 $152/$247/$349; 2050 $111/$184/$333 per kWh; 2025/2030 values NOT RETRIEVED | 2023$ (likely) | Medium | https://docs.nrel.gov/docs/fy25osti/93281.pdf |
| NREL ATB 2024 utility-scale BESS | 60 MW ref.; 2/4/6/8/10 h; CAPEX = pack×h + BOS; −18/−37/−52% 2022→2035; base-year $/kW NOT RETRIEVED | 2022$ | High (method) | https://atb.nrel.gov/electricity/2024/utility-scale_battery_storage |
| NREL Q1 2023 / Q1 2024 PV+ESS benchmarks (Ramasamy et al.) | Q1 2023 PV+60 MW/240 MWh MMP $2.11/Wdc vs MSP $1.65/Wdc; Q1 2024 ESS increment MSP $60/kWdc, MMP $234/kWdc — standalone-storage $/kWh NOT RETRIEVED | 2022$/2023$ | Medium | https://docs.nrel.gov/docs/fy23osti/87303.pdf ; https://data.nrel.gov/submissions/307 |
| EIA AEO2025 (S&L capital cost study, Jan 2024; Case 19 BESS 150 MW / 600 MWh) | Overnight $/kW, technological-optimism factor, and **regional (New England) multiplier: NOT RETRIEVED** | 2024$ | – | https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf ; EMM assumptions https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf ; mirror https://docs.catalyst.coop/pudl/en/nightly/_downloads/fcef77222b0e504440dfa03fa3984d08/eiaaeo_2025_electricity_market_assumptions.pdf |
| Lazard LCOE+ (Jun 2025) | 100 MW 4-h LCOS $115–254/MWh (unsubsidized), $83–192 (ITC); 2-h $129–277/MWh; capital $/kWh NOT RETRIEVED. Jun 2026 edition: "storage costs up 27% since 2020" headline | 2025 nominal | Medium | https://www.lazard.com/media/uounhon4/lazards-lcoeplus-june-2025.pdf ; https://www.ess-news.com/2026/07/13/battery-storage-costs-up-27-since-2020-says-lazard/ |
| Modo Energy global capex survey (Sep 2026; 100+ respondents, 20 markets) | Median 2-h **$325/kWh**, 4-h **$201/kWh**; doubling duration ≈ −38% per MWh | 2026 nominal | Medium | https://modoenergy.com/research/en/global-battery-capex-september-2026-research |
| Brattle, New England Energy Storage Duration Study (Feb 2024) | Models 1/2/4/8-h Li-ion; finds ~12 GW mid-duration need (4 GW 4-h, 8 GW 8-h) by mid-2030s; cost assumptions NOT RETRIEVED | – | – | https://www.brattle.com/wp-content/uploads/2024/02/New-England-Energy-Storage-Duration-Study.pdf |
| E3, Charging Forward: Energy Storage in a Net Zero Commonwealth (MassCEC/DOER, Dec 2023) | Basis for MA 5,000 MW target; cost assumptions NOT RETRIEVED | – | – | https://www.mass.gov/doc/charging-forward-energy-storage-in-a-net-zero-commonwealth-report/download |
| ISO-NE 2050 Transmission Study (Feb 2024) / EPCET (2024) | Storage capex assumptions NOT RETRIEVED | – | – | https://www.iso-ne.com/static-assets/documents/100008/2024_02_14_pac_2050_transmission_study_final.pdf ; https://www.iso-ne.com/static-assets/documents/100016/2024-epcet-report.pdf |
| CPUC IRP inputs | CPUC IRP (2022–2024 cycles) and the Lumen storage procurement study use NREL ATB-based storage costs; values NOT RETRIEVED this session | – | Low | see §3.3 |
| NJ GSESP awards | $60–82/kW-yr × 15 yr (grid-supply, transmission) | nominal | High | see §3.6 |
| CT ESS | $250/kWh residential upfront (2021); $280–450/kWh C&I (2025); $325/$175 per kW performance (2026) | nominal | Medium | see §3.5 |

---

## 5. Scale and duration effects (for a 10 MW / 2-h adjustment)

**Interconnection cost vs size (ISO data)**
- NYISO storage means: 1–50 MW $76/kW; 50–100 MW $64; 100–250 MW $73; 250+ MW $32/kW (LBNL, High) — mild scale effect below 250 MW; strong above.
- ISO-NE: 85–200 MW storage median $148/kW (2018-21); LBNL: "economies of scale exist for solar and possibly storage" (High).
- PJM: median standalone-storage complete cost fell to $0/kW; mean all-status $335/kW — distribution is right-skewed; use medians for a small project.

**Installed cost vs power (MW) and duration (h)**
- NREL ATB additive model: CAPEX($/kW) = Pack($/kWh) × h + BOS($/kW); i.e., $/kWh falls with duration because BOS/kW is spread over more MWh. ATB 2024 reference size 60 MW; durations 2–10 h; 2022→2035 reductions 18/37/52% (Cons/Mod/Adv). Numeric energy/power split NOT RETRIEVED. (High for structure)
- Modo (Sep 2026): global median 2-h $325/kWh vs 4-h $201/kWh (≈ −38%/MWh on doubling). (Medium) This is the most current empirical 2-h vs 4-h ratio retrieved; it implies a 2-h system at ~1.6× the $/kWh of a 4-h system (or ~0.8× the $/kW).
- PNNL Energy Storage Cost and Performance Database v2024 (2023 values) and 2022 Assessment (PNNL-33283; 2021 values, 2030 projections): tabulated total installed cost by chemistry (LFP, NMC), power (1, 10, 100, 1000 MW) and duration (2, 4, 6, 8, 10, 24, 100 h). **Values NOT RETRIEVED** (pnnl.gov and energy.gov mirrors blocked). URLs: https://www.pnnl.gov/projects/esgc-cost-performance ; https://www.pnnl.gov/projects/esgc-cost-performance/estimates ; https://www.pnnl.gov/sites/default/files/media/file/ESGC%20Cost%20Performance%20Report%202022%20PNNL-33283.pdf ; https://www.energy.gov/sites/default/files/2022-09/2022%20Grid%20Energy%20Storage%20Technology%20Cost%20and%20Performance%20Assessment.pdf ; 2020 report https://www.pnnl.gov/sites/default/files/media/file/Final%20-%20ESGC%20Cost%20Performance%20Report%2012-11-2020.pdf ; LCOS workbook doc https://www.pnnl.gov/sites/default/files/media/file/ESGC_LCOS_Workbook_v2024_Documentation.pdf. PNNL LCOS: Li-ion ≤ 10 h ≈ $200–400/MWh, LFP at low end (Medium).
- Lazard: LCOS 2-h $129–277/MWh vs 4-h $115–254/MWh (100 MW) — duration effect on LCOS ≈ 10–12% (Medium).
- Sovacool & Ryu 2025: diseconomies-of-scale breakpoints at 1,280 MW and 1,561 MW for energy projects generally (not storage-specific) — supports the position that a 10 MW project is far from the "megaproject" risk regime. (High)

**Actual utility-owned unit costs retrieved (nominal; derived; for reference-class use)**
| Project | MW / MWh | h | Cost | $/kW | $/kWh | Year |
|---|---|---|---|---|---|---|
| Eversource Provincetown (DPU 17-05) | 24.9 / 38 | 1.5 | $40 M | 1,606 | 1,053 | 2019–22 |
| National Grid Nantucket (DPU 17-13) | 6 / 48 | 8 | $81 M | 13,500 | 1,688 | 2019 |
| HECO Waena (cap) | 40 / 160 | 4 | $82 M | 2,050 | 513 | 2023 approval |
| SCE/Ameresco (EPC+maint.) | 537.5 / 2,150 | 4 | $1.226 B | 2,281 | 570 | 2021 |
| SDG&E Westside Canal 2a | 119 / n/r | n/r | $267.9 M | 2,251 | n/r | 2024 |
| MISO Waupaca SATOA (with 14 MVAR caps) | 2.5 / 5 | 2 | $8.1 M | 3,240 | 1,620 | 2020 |
| Xcel MN distribution VPP (budget range) | 200 / n/r | n/r | $152–430 M | 760–2,150 | n/r | 2025 filing |
| NYSERDA bulk avg (> 5 MW) | – | mostly 4 | – | – | 524 | to Dec 2025 |
| NYSERDA retail FTM avg | – | – | – | – | 666 | to Dec 2025 |

---

## 6. Statistical benchmarking practice

### 6.1 AACE International Recommended Practices (titles verified from AACE TOC pages / catalog listings)
- **10S-90** Cost Engineering Terminology. (High)
- **17R-97** Cost Estimate Classification System (generic). (High)
- **18R-97** Cost Estimate Classification System – As Applied in Engineering, Procurement, and Construction for the Process Industries. (High)
- **96R-18** Cost Estimate Classification System – As Applied in Engineering, Procurement, and Construction for the Power Transmission Line Infrastructure Industries (Aug 7 2020). (High) — closest AACE class system for a utility T&D-connected asset; 97R-18 = pipelines; 98R-18 = road/rail; 56R-08 = building.
- **40R-08** Contingency Estimating – General Principles. (High)
- **41R-08** Risk Analysis and Contingency Determination Using Range Estimating. (High)
- **42R-08** Risk Analysis and Contingency Determination Using Parametric Estimating. (High) (43R-08 = parametric example models for process industries — Medium.)
- **44R-08** Risk Analysis and Contingency Determination Using Expected Value. (High)
- **57R-09** Integrated Cost and Schedule Risk Analysis Using Monte Carlo Simulation of a CPM Model. (High)
- **58R-10** Escalation Estimating Principles and Methods Using Indices (May 25 2011). (High)
- **62R-11** Risk Assessment: Identification and Qualitative Analysis. (High)
- **63R-11** Risk Treatment. (High)
- **65R-11** Integrated Cost and Schedule Risk Analysis and Contingency Determination Using Expected Value. (High)
- **66R-11** Selecting Probability Distribution Functions for Use in Cost and Schedule Risk Simulation Models. (High) — NOTE: this is the correct title; it is *not* "selecting probabilistic methods". The guidance on choosing among methods is in **PGD-02 Guide to Quantitative Risk Analysis** (High) and PGD-01 Guide to Cost Estimate Classification Systems.
- **68R-11** Escalation Estimating Using Indices and Monte Carlo Simulation (May 2 2012). (High)
- **113R-20** Integrated Cost and Schedule Risk Analysis and Contingency Determination Using Combined Parametric and Expected Value. (High)
- **123R-22** Integrated Cost and Schedule Risk Analysis and … (remainder of title NOT RETRIEVED; flag). (Low)
- URLs: https://web.aacei.org/docs/default-source/toc/toc_40r-08.pdf ; …/toc_41r-08 (WSDOT copy: https://wsdot.wa.gov/sites/default/files/2021-12/risk-analysis-contingency-RangeEstimating.pdf) ; https://web.aacei.org/docs/default-source/toc/toc_42r-08.pdf ; https://web.aacei.org/docs/default-source/toc/toc_44r-08.pdf ; https://web.aacei.org/docs/default-source/toc/toc_58r-10.pdf ; https://web.aacei.org/docs/default-source/toc/toc_65r-11.pdf ; https://web.aacei.org/docs/default-source/toc/toc_68r-11.pdf ; https://web.aacei.org/docs/default-source/toc/toc_113r-20.pdf ; https://web.aacei.org/docs/default-source/toc/toc_96r-18.pdf ; https://web.aacei.org/docs/default-source/toc/toc_18r-97.pdf ; https://library.aacei.org/pgd02/pgd02.shtml ; https://library.aacei.org/pgd01/pgd01.shtml ; https://www.pathlms.com/aace/courses/2928/documents/3841 (58R-10) ; …/3848 (65R-11) ; …/46847 (113R-20) ; …/3845 (62R-11)

### 6.2 Reference class forecasting (Flyvbjerg)
- Flyvbjerg, Holm & Buhl (2002) "Underestimating Costs in Public Works Projects": mean real overruns rail +44.7%, bridges/tunnels +33.8%, roads +20.4% (High).
- Flyvbjerg (2018) "Five things you should know about cost overrun," Transportation Research Part A (Medium). https://bentflyvbjerg.medium.com/five-things-you-should-know-about-cost-overrun-d2bce69d6f51
- Flyvbjerg & Gardner, *How Big Things Get Done* (2023), database > 16,000 projects: **47.9% on budget; 8.5% on budget and on time; 0.5% on budget, on time and on benefits.** Energy base rates cited from the appendix/interviews: **solar +1%, wind +13% (1.12–1.13), transmission +8%, fossil +16%, hydro +75%, nuclear +120%**; Flyvbjerg states batteries "perform similarly to wind and solar." (High for headline rates; Medium for energy rows) https://cleantechnica.com/2024/08/14/how-big-things-get-done-talking-with-megaproject-expert-professor-bent-flyvbjerg/ ; https://budgetoverrun.com/studies/flyvbjerg-megaproject-database
- **Battery-storage-specific base rate**: a secondary site citing the "Oxford Projects Database Q2 2023" gives **mean overrun ≈ +6%, 40% of projects > 50% overrun, 0% meeting all criteria** — **Low confidence** (could not verify against the book appendix; treat as indicative only). https://budgetoverrun.com/reference-class-forecasting
- RCF methodology reviews: https://www.sciencedirect.com/science/article/pii/S2666721523000248 ; https://www.tandfonline.com/doi/full/10.1080/09537287.2025.2578708 ; PMI summary https://www.pmi.org/learning/library/nobel-project-management-reference-class-forecasting-8068

### 6.3 Electricity-infrastructure overrun studies (Sovacool et al.)
- Sovacool, Nugent & Gilbert (2014), *Electricity Journal* / *Energy Research & Social Science*: **401 projects, $820 B, 325 GW + 8,500 km lines; $388 B overruns; mean +66.3% per project**; nuclear +117.3%, hydro +70.6%, wind +8%, solar +1%; transmission low single digits. (High) https://www.sciencedirect.com/science/article/abs/pii/S1040619014000761 ; https://www.sciencedirect.com/science/article/abs/pii/S2214629614000942
- Sovacool & Ryu (2025), "Beyond economies of scale…," *ERSS*: **662 projects, 83 countries, 1936–2024, $1.358 T actual vs $812 B budget (+66% aggregate; mean +40.6% per project; > 60% overran; mean delay ≈ 2 yr)**; nuclear +102.5% (schedule +64%), hydro +36.7%, geothermal +20.7% (schedule +58.8%), CCS +14.9%, bioenergy +10.7%, fossil-thermal +9.7%, wind +5.2%, **solar −2.2%, transmission −3.6%**; diseconomy breakpoints 1,280 MW and 1,561 MW. **No separate battery-storage category reported.** (High) https://www.sciencedirect.com/science/article/abs/pii/S2214629625001380 ; https://www.eurekalert.org/news-releases/1084467
- Ryu (2025) wind-specific scale study: https://onlinelibrary.wiley.com/doi/10.1002/we.70053
- Orennia summary of typical energy project overruns: https://orennia.com/insights/typical-energy-project-cost-overruns (values NOT RETRIEVED).

### 6.4 Storage-specific performance / estimate-accuracy evidence
- **ACCURE 2025 Energy Storage System Health & Performance Report** (Sep 2025; > 100 systems > 10 MWh, 18 GWh, Jun–Sep 2025): **19% of projects had operational issues that reduced revenue** (trips, safety alerts, rack/module imbalance). Not a capex overrun statistic, but the only large-sample BESS delivery-quality dataset found. (High on figure) https://pv-magazine-usa.com/2025/10/07/operational-issues-hit-returns-in-one-in-five-battery-storage-projects-report-finds/
- Commissioning-delay anecdotes: typical 1–2 months, up to 8+ months (permitting, switchgear/transformer lead times) — trade-press paraphrase, Low.
- Observed regulatory cost-cap escalation datapoints usable as a mini reference class: HECO Waena $60 M est → $82 M approved cap (+37%) with further increase sought (tariffs); Massachusetts §83E River Mill withdrawal after interconnection-cost shock; NYSERDA roadmap bulk incentive NPV +48% (2022 → 2024 estimate). (Medium; derived)
- **No peer-reviewed study of BESS capex estimate accuracy / overrun rates was found.** Mark as a gap; the defensible approach is to (a) use Flyvbjerg's solar/wind/transmission classes (+1% to +13%) as the nearest reference class with the ACCURE and HECO datapoints as risk-register evidence, and (b) run AACE 41R-08/42R-08 contingency with 66R-11 distributions.

---

## URL index (by section; ✔ = content retrieved via search excerpt; ✖ = blocked, cite by title)

**§1 LBNL / ISO-NE**
- https://emp.lbl.gov/interconnection_costs ✔(excerpt)
- https://emp.lbl.gov/publications/interconnection-cost-analysis-iso-new ✔ ; https://eta-publications.lbl.gov/sites/default/files/iso-ne_interconnection_costs_vfinal.pdf ✖ ; https://www.osti.gov/biblio/1986022 ✖ ; https://escholarship.org/content/qt0919400z/qt0919400z.pdf ✖
- https://emp.lbl.gov/publications/interconnection-cost-analysis-pjm ✔ ; https://eta-publications.lbl.gov/sites/default/files/berkeley_lab_2023.1.12-_pjm_interconnection_costs.pdf ✖ ; https://www.utilitydive.com/news/PJM-generator-interconnection-costs-network-upgrades-berkeley-study/640824/ ✔
- https://emp.lbl.gov/publications/generator-interconnection-cost ✔ ; https://eta-publications.lbl.gov/sites/default/files/berkeley_lab_2022.10.06-_miso_interconnection_costs.pdf ✖ ; https://www.publicpower.org/periodical/article/interconnection-costs-have-risen-steeply-miso-berkeley-lab-report ✔
- https://emp.lbl.gov/publications/interconnection-cost-analysis-nyiso ✔ ; https://eta-publications.lbl.gov/sites/default/files/nyiso_interconnection_costs_vfinal.pdf ✖
- https://emp.lbl.gov/publications/generator-interconnection-cost-0 ✔ ; https://www.osti.gov/servlets/purl/1971633 ✖
- https://eta-publications.lbl.gov/sites/default/files/2026-02/lbnl_2026.02.23_ba_interconnection_costs.pdf ✖ (excerpt ✔)
- https://emp.lbl.gov/publications/generator-interconnection-costs (Summary Briefing 2023) ✔
- https://www.rtoinsider.com/49107-lbnl-webinar-interconnection-costs/ ✖
- ISO-NE TCS: https://www.mass.gov/doc/letter-to-iso-ne-on-transitional-cluster-study-interim-results-june-25-2026/download ✖(excerpt ✔) ; https://www.mass.gov/doc/transitional-cluster-study-presentation-72326/download ✖ ; https://epeconsulting.com/epe-intelligence/news/iso-nes-transitional-cluster-study-tc2-results-are-in-what-developers-need-to-know ✖(excerpt ✔) ; https://askiso.iso-ne.com/s/article/Cost-Allocation-for-the-Transitional-Cluster-Study ✖(excerpt ✔) ; https://isonewswire.com/2025/10/20/iso-ne-begins-interconnection-transitional-cluster-study/ ✖(excerpt ✔) ; https://www.rtoinsider.com/118175-storage-projects-dominate-iso-ne-cluster-study/ ✖(excerpt ✔) ; https://www.utilitydive.com/news/iso-new-england-launches-cluster-study-of-26-battery-wind-and-solar-projec/803333/ ; https://modoenergy.com/research/en/iso-ne-interconnection-queue-outlook-july-2026 ✖ ; https://www.iso-ne.com/static-assets/documents/2021/09/a06_tc_2021_09_28_oatt_sched11.pdf (Schedule 11 allocation) ✔(excerpt)

**§2 FERC**
- https://www.ferc.gov/media/order-no-898 ; https://www.federalregister.gov/documents/2023/10/05/2023-14994/accounting-and-reporting-treatment-of-certain-renewable-energy-assets ✖(excerpt ✔) ; https://public-inspection.federalregister.gov/2023-14994.pdf ; https://www.iso-ne.com/static-assets/documents/100027/a02_tc_pto_ac_order898_compliance_presentation.pdf ; https://www.troutman.com/insights/ferc-establishes-revised-accounting-rules-to-address-renewables-storage-and-recs/ ; https://blog.protiviti.com/2024/10/01/understanding-ferc-order-898-implications-and-opportunities-for-public-utilities-and-licensees/
- https://docs.catalyst.coop/pudl/en/stable/data_sources/ferc1.html ; https://zenodo.org/records/21860241 ; https://data.catalyst.coop/
- https://www.ferc.gov/sites/default/files/2020-05/20200310135710-ER20-588-000.pdf (MISO SATOA) ; https://ferc.gov/sites/default/files/2020-04/E-6_14.pdf (Western Grid) ; https://www.misoenergy.org/engage/MISO-Dashboard/storage-as-transmission-only-asset/ ; https://www.sandia.gov/app/uploads/sites/273/2024/06/3_McKee_Bob_ATC_ICC_Session5_1-11-2022.pdf ; https://www.troutmanenergyreport.com/2023/06/ferc-approves-spp-proposal-for-energy-storage-to-be-considered-transmission-only-assets/ ; https://www.insideenergyandenvironment.com/2020/08/electric-storage-may-be-treated-as-transmission/ ; https://www.nyiso.com/documents/20142/38699263/Storage%20as%20Transmission%20-%20Introduction.pdf ; https://cdn.ymaws.com/ny-best.org/resource/resmgr/reports/SATA_White_Paper_Final_01092.pdf ✖ ; https://www.utilitydive.com/news/energy-storage-underused-transmission-asset-ferc/727946/ ; https://www.morganlewis.com/pubs/2025/03/how-recent-ferc-orders-are-regulating-electric-storage-qfs-and-inverter-based-resources-in-2025

**§3 States** — see inline URLs in §3.1–3.6 (mass.gov, macleanenergy.com, foleyhoag.com, cleanpeakmarketoutlook.com, nyserda.ny.gov, documents.dps.ny.gov, coned.com, cpuc.ca.gov, docs.cpuc.ca.gov, hawaiianelectric.com, portal.ct.gov, ctgreenbank.com, nj.gov/bpu, mgrid.org, utilitydive.com).

**§4–5 Programs / scale** — https://docs.nrel.gov/docs/fy23osti/85332.pdf ; https://docs.nrel.gov/docs/fy25osti/93281.pdf ; https://atb.nrel.gov/electricity/2024/utility-scale_battery_storage ; https://data.openei.org/submissions/6006 (ATB 2024 data) ; https://docs.nrel.gov/docs/fy23osti/87303.pdf ; https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf ; https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf ; https://www.eia.gov/outlooks/aeo/electricity_generation/pdf/AEO2025_LCOE_report.pdf ; https://www.lazard.com/media/uounhon4/lazards-lcoeplus-june-2025.pdf ; https://www.energy-storage.news/lazard-says-us-energy-storage-cost-reduction-in-2025-offsets-prior-pandemic-driven-increases/ ; https://modoenergy.com/research/en/global-battery-capex-september-2026-research ; https://www.brattle.com/wp-content/uploads/2024/02/New-England-Energy-Storage-Duration-Study.pdf ; https://www.mass.gov/doc/charging-forward-energy-storage-in-a-net-zero-commonwealth-report/download ; https://www.pnnl.gov/projects/esgc-cost-performance ; https://www.pnnl.gov/sites/default/files/media/file/ESGC%20Cost%20Performance%20Report%202022%20PNNL-33283.pdf ; https://www.energy.gov/eere/analysis/2022-grid-energy-storage-technology-cost-and-performance-assessment

**§6 Methods** — AACE URLs in §6.1; https://bentflyvbjerg.medium.com/five-things-you-should-know-about-cost-overrun-d2bce69d6f51 ; https://cleantechnica.com/2024/08/14/how-big-things-get-done-talking-with-megaproject-expert-professor-bent-flyvbjerg/ ; https://budgetoverrun.com/studies/flyvbjerg-megaproject-database ; https://www.sciencedirect.com/science/article/abs/pii/S1040619014000761 ; https://www.sciencedirect.com/science/article/abs/pii/S2214629625001380 ; https://www.eurekalert.org/news-releases/1084467 ; https://pv-magazine-usa.com/2025/10/07/operational-issues-hit-returns-in-one-in-five-battery-storage-projects-report-finds/

---

### Items NOT RETRIEVED (for follow-up from an unrestricted network)
1. LBNL ISO-NE storage mean/withdrawn/active split by status (brief Figs 7–8); LBNL CAISO storage $/kW; MISO storage by status.
2. ISO-NE TCS: NEMA/Boston zonal $/MW; withdrawal-penalty/readiness-deposit terms.
3. FERC formula-rate storage projects with public capex (PJM/AEP/Xcel/ITC/NYISO-ConEd).
4. MA ESMP (24-10/24-11) storage line-item $; §83E Round I contract prices; DPU 26-87/88/89 filings.
5. NY utility dispatch-rights contract $/kW-month; NYSERDA ISC award prices.
6. PNNL database values at 1/10/100/1000 MW × 2/4/6/8/10 h; NREL ATB 2024 base-year $/kW and energy/power split; NREL 2025 Update 2025/2030 values; EIA AEO2025 BESS overnight $/kW and New England regional multiplier; Lazard 2025 capital-cost $/kWh ranges; Brattle/E3/ISO-NE study cost assumptions.
7. Peer-reviewed BESS-specific cost-overrun / estimate-accuracy statistics (none found); verification of the "+6% battery" Oxford base rate.

# Hyde Park BESS - Cost Analysis Deliverables (29 Sep 2026, updated 2 Oct 2026)

Prepared by the Cost Estimating Center of Excellence from the estimate files in this repository.
Basis of record: `1) Estimate Summary Form/ESF - Hyde Park BESS Total Rev 3.xlsm` (24 Sep 2026), $57,247,300 approval level for project 21334.

| File | What it is | Audience |
|---|---|---|
| `Hyde Park BESS - Cost Analysis Deck.pptx` (+ `.pdf`) | 24-slide executive deck in three sections (where the money sits; how the cost changed; can the number be defended): battery contract vs all-in project, 13-layer cost extraction, unit costs at every boundary, industry benchmarks, the battery installed-cost curve 2015-2028 with Hyde Park plotted on it, the escalation basis and common-dollar comparison, cost history 2021-2026, September revision walk, red-team kill shots, stress tests, pre-mortem, open items, appendix A-C, contributions. Speaker notes on every slide; a 13-slide core path is noted on slide 2. | Leadership / Digaunto review |
| `Hyde Park BESS - Basis of Estimate (Rev 3).docx` | Basis of Estimate following the Eversource Estimate Basis Document template headings, populated from the Rev 3 ESF, the Nomad cover agreement, E-23-373, the PAF Rev 3 and the Aug-Sep 2026 email record. Section 3 is the battery / station / interconnection extraction; Section 22 is the open-item register for full funding. | Estimating, PM, full-funding PAF |
| `Hyde Park BESS - All-In Cost Whitepaper.docx` | "The Battery Is Not the Project": why a $12.1M vendor contract is a $57.2M project, how to read vendor pricing against published benchmarks, and the cost-over-time narrative. Eighteen cited benchmarks with scope definitions and confidence tags. | Leadership, regulatory-facing narrative (after benchmark verification) |
| `Hyde Park BESS - Cost Analysis Workbook.xlsx` | Traceable data source: README, Layers (SUMIFS over 292 line items), Unit Costs, Timeline, Sept 2026 Walk, 2023 Indicative, Benchmarks, Cost Curve (industry series, Hyde Park points, 2-h / 10 MW adjustment, escalation basis, common-dollar comparison), Line Items, Public Projects, Statistics. Zero formula errors (LibreOffice recalc). Blue font = keyed inputs. | Anyone who needs to tie a slide number to a cell |
| `Hyde Park BESS - Unit Cost Ladder One-Pager.docx` (+ `.pdf`) | One page for the regulatory narrative: the seven cost boundaries, $/kW and $/kWh at each, what each boundary adds, and the rule for reading a published benchmark against it. | Regulatory narrative, PAF exhibit |
| `Hyde Park BESS - Statistical Benchmarking Memo.docx` | Can the number be defended statistically: reference class of 13 utility-owned projects, log-log regression on 26 public projects (size and duration elasticities, 80% prediction interval), Monte Carlo on the thirteen cost layers (base and Class 5-like calibrations), estimate-to-actual uplift on comparables, ISO interconnection references, AACE/Flyvbjerg method citations, and how to use each in the argument. | Estimating, leadership, regulatory prep |
| `Hyde Park BESS - Red Team Report.docx` | Independent challenge of the package: steelman, three kill shots (Haugland reconciliation, siting float, estimate class), 14-item challenge register, where to be more aggressive, base-rate check, seven stress tests, risk-register audit, pre-mortem with five early-warning indicators, what would change our mind, certification (ready with repairs). | Digaunto prep, full-funding gate |
| `build/` | Python scripts that generate every file above from the repository (`analysis.py` classifies the ESF line items; `stats_model.py` and `mc_model.py` run the regression and Monte Carlo; the others build the deck, documents and workbook). `benchmarks.json` is the curated benchmark set; `benchmark_research_log.md` is the research log. `build/data/` holds the 44-project public cost dataset (`bess_projects.csv`, sourcing notes) and the ISO / FERC / state-PUC reference log. | Reproducibility |

## Headline numbers (10 MW / 20 MWh)

| Boundary | Total | $/kW | $/kWh |
|---|---|---|---|
| Nomad fixed-price contract (10 Mar 2026) | $12,106,850 | $1,211 | $605 |
| Battery installed, direct (layers A+B+C) | $16,657,252 | $1,666 | $833 |
| Station 360 approval level | $49,994,200 | $4,999 | $2,500 |
| Project 21334 approval level (Sta 360 + Sta 496) | $57,247,300 | $5,725 | $2,862 |
| All-in incl. D-Line 24211 (2024 conceptual, memo) | $62,040,300 | $6,204 | $3,102 |

Battery supply contract = 21% of the project. Station, site and feeder interconnection (layers D+E+F) = 32% loaded. Risk, contingency, indirects and AFUDC = 41% of the approval level.

## Statistical evaluation (memo and deck appendix A-C)

- Reference class (13 utility-owned projects, <= 100 MWh): median $1,235/kWh. Hyde Park battery installed ($833) at the 38th percentile; station complete, direct ($1,483) at the 77th; approval level ($2,862) above the maximum.
- Regression (n = 26, R-squared 0.65): size elasticity -0.17, duration elasticity -0.29, year not significant. Prediction for 20 MWh / 2-h / 2028: $1,116/kWh, 80% interval $611 to $2,037. Use as a bracket, not a price.
- Monte Carlo on the layers (20,000 trials): P80 $53.0M base / $55.9M wide against $57.2M approval; reserve needed to reach P80 $3.4M / $6.2M vs $7.6M carried. Uncertainty concentrates in the landfill platform, Station 496 and owner soft costs; the battery contract contributes almost nothing.
- Estimate-to-actual uplift on comparable small utility BESS: +9% to +64%, median about +31%.

## Cost curve and escalation (2 Oct 2026, slides 10-11)

- Is there a battery curve? Yes. EIA reported all-in $2,152/kWh (2015) to $625 (2018); BNEF turnkey 4-h $324 (2022) to $117 global / $219 US (2025); NREL 4-h base $334 (2024), $247 by 2035. All four-hour, 60-150 MW, real dollars. Adjusted to 2-h and 20 MWh (factors 1.3-1.5 and 1.54), the US turnkey index is $440-$505 vs Nomad equipment $532. Owner-scope install and balance of plant add $183/kWh: $833 installed.
- Is escalation included? Yes: $2,948,100 inside the Rev 3 directs (Sta 360 $2,622,100; Sta 496 $326,100) at template rates (~3%/yr) on the 2026-2028 spend curve; 5.1% of the approval level, $147/kWh. $1,130,255 of it sits on the fixed-price Nomad balance (open decision). On a common 2028 dollar basis NREL's $334 becomes $376, and $750-$870 after the duration and size adjustments, against $833 installed.

## Red team (29 Sep 2026)

- Verdict: defensible as a station cost, not yet as a full-funding number. Ready with repairs.
- Kill shots: (1) Haugland Class 3 base $19.2M vs Rev 3 construction layers $8.3M direct, unmapped, likely points up; (2) siting chain has no float and an 18-24 month EFSB fallback; (3) maturity is Class 4, not Class 3.
- Defensible reductions about $3M, conditional on the Haugland reconciliation closing first.
- Combination downside (HEG midpoint plus 12-month slip): about +$13M, to ~$70M.

## Caveats

- Public project costs and benchmarks were retrieved from search-index excerpts of the primary sources (NREL, EIA, LBNL, BNEF, Lazard, utility filings); the research environment could not download the PDFs. Each carries a confidence tag. Verify against the primary PDFs before external use (list in whitepaper section 8 and the research log).
- The D-Line (24211) figure is the Feb 2024 SSF conceptual and has not been re-based.
- Rev 3 is classed Conceptual (-25% / +50%). The BOE lists eight reconciliations to close before full funding, led by the Haugland Class 3 reconciliation and the $1.13M escalation carried on the fixed-price battery balance.

## Regenerating

```bash
pip install openpyxl python-docx python-pptx pymupdf
python3 build/analysis.py          # writes data.json from the Rev 3 ESF
python3 build/build_xlsx.py        # workbook (then recalc with LibreOffice)
python3 build/build_deck.py        # deck
python3 build/build_boe.py         # basis of estimate
python3 build/build_whitepaper.py  # whitepaper
python3 build/build_onepager.py    # one-pager
python3 build/stats_model.py; python3 build/mc_model.py; python3 build/mc_model.py wide; python3 build/mc_charts.py
python3 build/build_stats_memo.py; python3 build/update_xlsx_stats.py; python3 build/update_xlsx_curve.py; python3 build/add_appendix_slides.py
```
Scripts reference the scratchpad path used during the original build; set `B`/`OUT` at the top of each script to a local folder before running.

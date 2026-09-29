# Hyde Park BESS - Cost Analysis Deliverables (29 Sep 2026)

Prepared by the Cost Estimating Center of Excellence from the estimate files in this repository.
Basis of record: `1) Estimate Summary Form/ESF - Hyde Park BESS Total Rev 3.xlsm` (24 Sep 2026), $57,247,300 approval level for project 21334.

| File | What it is | Audience |
|---|---|---|
| `Hyde Park BESS - Cost Analysis Deck.pptx` (+ `.pdf`) | 16-slide executive deck: battery contract vs all-in project, 13-layer cost extraction, unit costs at every boundary, industry benchmarks, cost history 2021-2026, September revision walk, open items, contributions. Speaker notes on every slide. | Leadership / Digaunto review |
| `Hyde Park BESS - Basis of Estimate (Rev 3).docx` | Basis of Estimate following the Eversource Estimate Basis Document template headings, populated from the Rev 3 ESF, the Nomad cover agreement, E-23-373, the PAF Rev 3 and the Aug-Sep 2026 email record. Section 3 is the battery / station / interconnection extraction; Section 22 is the open-item register for full funding. | Estimating, PM, full-funding PAF |
| `Hyde Park BESS - All-In Cost Whitepaper.docx` | "The Battery Is Not the Project": why a $12.1M vendor contract is a $57.2M project, how to read vendor pricing against published benchmarks, and the cost-over-time narrative. Eighteen cited benchmarks with scope definitions and confidence tags. | Leadership, regulatory-facing narrative (after benchmark verification) |
| `Hyde Park BESS - Cost Analysis Workbook.xlsx` | Traceable data source: README, Layers (SUMIFS over 292 line items), Unit Costs, Timeline, Sept 2026 Walk, 2023 Indicative, Benchmarks, Line Items. 400 formulas, zero errors (LibreOffice recalc). Blue font = keyed inputs. | Anyone who needs to tie a slide number to a cell |
| `build/` | Python scripts that generate every file above from the repository (`analysis.py` classifies the ESF line items; the others build the deck, documents and workbook). `benchmarks.json` is the curated benchmark set; `benchmark_research_log.md` is the full research log with URLs and access caveats. | Reproducibility |

## Headline numbers (10 MW / 20 MWh)

| Boundary | Total | $/kW | $/kWh |
|---|---|---|---|
| Nomad fixed-price contract (10 Mar 2026) | $12,106,850 | $1,211 | $605 |
| Battery installed, direct (layers A+B+C) | $16,657,252 | $1,666 | $833 |
| Station 360 approval level | $49,994,200 | $4,999 | $2,500 |
| Project 21334 approval level (Sta 360 + Sta 496) | $57,247,300 | $5,725 | $2,862 |
| All-in incl. D-Line 24211 (2024 conceptual, memo) | $62,040,300 | $6,204 | $3,102 |

Battery supply contract = 21% of the project. Station, site and feeder interconnection (layers D+E+F) = 32% loaded. Risk, contingency, indirects and AFUDC = 41% of the approval level.

## Caveats

- Benchmarks were retrieved from search-index excerpts of the primary sources (NREL, EIA, LBNL, BNEF, Lazard, utility filings); the research environment could not download the PDFs. Each carries a confidence tag. Verify against the primary PDFs before external use (list in whitepaper section 8 and the research log).
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
```
Scripts reference the scratchpad path used during the original build; set `B`/`OUT` at the top of each script to a local folder before running.

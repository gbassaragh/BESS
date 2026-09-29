# BESS project cost dataset – sourcing notes

Companion to `bess_projects.csv` (44 rows). Compiled 2026-09-29 for a statistical benchmark against a 10 MW / 20 MWh utility-owned, distribution-connected BESS in Boston (ISO-NE, in service Dec 2028).

Method: search-engine excerpts (WebSearch) of regulator filings, utility/SEC releases and trade press. The sandbox proxy blocked direct fetches of nearly every host tried (mass.gov, sec.gov, cpuc, psc.maryland.gov, utility sites, tdworld, publicpower, prnewswire, local papers), so **figures below are as they appeared in search excerpts and were not read in the primary document**. Every row should be spot-checked against its URL before publication. The WebSearch budget (200 calls) was exhausted before all verification searches could be run; unverified fields were left blank rather than guessed.

Confidence tags: High = regulator order/filing, SEC filing, utility press release; Medium = trade/local press quoting those; Low = informal statement or unverified secondary source.

Currency: `cost_usd` is nominal USD. For non-US rows the native figure is stated below and the conversion rate used is approximate (my conversion, not the source's) unless the source itself gave a USD figure.

---

## Per-project notes

### 1. Eversource Outer Cape (Provincetown) BESS – 25 MW / 38 MWh – $49M
- Quote (Provincetown Independent, 2026): "Eversource spent $49 million installing a 25-megawatt BESS battery at Provincetown's transfer station along with a new fiber optic control grid for Provincetown and Truro." capecod.com: "The $49 million project comprises lithium-ion battery units in a new 8,000-square-foot building at the town transfer station and new circuitry for the loop of power lines just in Provincetown."
- DPU 17-05 (2017) approved a budget range of $35–45M (per search summary of mass.gov page, which could not be fetched). In service Dec 2022 (Eversource) / went live Sept 2022 (TRC).
- Problem: cost includes fiber/control network and loop circuitry; battery share not disclosed. Most relevant comparable (MA IOU, distribution-connected, ISO-NE).

### 2. National Grid Nantucket BESS – 6 MW / 48 MWh – $81M
- "The project cost approximately $81 million. This figure includes a new 15 MW generator and power control house." (Utility Dive / RenewableEnergyWorld, Oct 2019). Tesla Powerpack, 8-hour. Alternative was a ~$200M third submarine cable.
- Problem: cost includes diesel generator; battery-only cost not disclosed.

### 3–4. Eversource Martha's Vineyard BESS Phase 1 (4.9 MW/20 MWh, ~$15M) and Phase 2 (9.8 MW/64 MWh, ~$28M) – DPU 18-155
- Microgrid Knowledge (2019): "first phase was a 4.9-MW/20-MWh project ... at a cost of about $15 million. The second phase was a 9.8-MW/64-MWh project ... at an estimated cost of $28 million."
- Eversource notified DPU on May 17, 2021 that it cancelled the project ("no longer a good financial investment"). cod_year set to DPU approval year 2019.
- Problem: estimates only; never built. Useful as an approved-estimate datapoint for a MA distribution-connected utility BESS.

### 5. Sterling MLD – 2 MW / 3.9 MWh – $2.7M (2016)
- CESA/Clean Energy Group: "the $2.7 million project is expected to pay for itself in just over two years with the help of grants"; funded by $1.4M DOER resiliency grant and $250k DOE. Commissioned Dec 2016; NEC Energy Solutions.

### 6. O&R Pomona (Ladentown) – 3 MW / 12 MWh – $7.4M (2021)
- O&R press release (Apr 2021): "The 3MW battery is owned by O&R and was built on O&R property adjacent to O&R's Ladentown electric substation in Pomona. The cost of the project is $7.4 million."

### 7. PGE Salem Smart Power Center – 5 MW / 1.25 MWh – $23M (2013)
- PGE release: "$23 million Salem Smart Power Project" with Eaton and EnerDel; DOE matching funds (PNW Smart Grid Demonstration).
- Problem: R&D demonstration incl. building/microgrid/smart-grid systems; not representative of commercial BESS cost.

### 8. Hawaiian Electric Waena BESS (Maui) – 40 MW / 160 MWh – $82.1M approved estimate
- HEI 10-Q (June 30, 2026): "In December 2023, the PUC approved Maui Electric's request to commit funds estimated at $82.1 million for the purchase and installation of the Waena BESS project, and to recover costs ... under EPRM." "In July 2025, the PUC approved ... recovery of costs in addition to the amounts approved in December 2023 due to the uncertainty of changes in law, limited to the lesser of either the actual costs or 20% over the approved estimated capital costs." "Project costs incurred as of June 30, 2026, amount to $27.2 million." Original 2020 application: ~$60M. Tesla Megapacks; COD expected 2027.

### 9. Snohomish PUD Arlington Microgrid – 1 MW / 1.4 MWh – $12M (2020)
- "Snohomish County PUD's $12 million microgrid"; $3.5M WA Clean Energy Fund. Includes 500 kW solar, Clean Energy Center building, V2G. Battery-only cost not separated.

### 10. NV Energy Reid Gardner – 220 MW / 440 MWh – $257M (2023)
- Las Vegas Review-Journal: "NV Energy cuts ribbon on $257M facility"; Wikipedia: "construction cost of $257 million"; ~40% (~$100M) offset by IRA credits. Energy Vault EPC; PUCN approval July 2022; commissioned Dec 2023. Coal site.

### 11. PGE Constable (Evergreen) – 75 MW / 300 MWh – $156M incl. AFUDC (2024)
- PGE 2024 10-K: "As of December 31, 2024, the Company had recorded $156 million in Electric Utility Plant, net, including AFUDC for this facility." EPC by Mortenson; COD Dec 2024; Hillsboro OR.

### 12. PGE Seaside – 200 MW / 800 MWh – $360M excl. AFUDC (2025)
- PGE 10-K: "PGE and Eolian, L.P. agreed to construct the 200 MW battery system with an investment of approximately $360 million, excluding AFUDC" (fixed-cost build-transfer agreement). OPUC Order 25-417 (Oct 2025): rate base increase $220M net of estimated ITC $125M.

### 13. GMP Essex solar+storage – 2 MW / 8 MWh + 4.9 MW solar – $14.3M
- VTDigger (Sept 2022): "The Essex project's development and interconnection is expected to cost about $14.3 million ... 18,326 solar panels and a 2MW/4-hour Tesla PowerPack battery system."
- Problem: solar included; not separable.

### 14. NYPA Northern NY (Chateaugay) – 20 MW / 20 MWh – $29.8M (2023)
- NYPA/APPA: "estimated cost of $29.8 million ... received $6 million in funding from NYPA board in addition to the earlier approved $23.8 million." One-hour Li-ion; adjacent to NYPA substation; operating Aug 2023.

### 15. Con Edison Ozone Park – 1.5 MW / 12 MWh – ~$15M (2019)
- NY1 (May 2019): "a facility with battery storage to get past peak demand costs about $15 million according to Con Edison's spokesman." Con Ed lists Ozone Park as 1.5 MW/12 MWh (other sources 2 MW). Low confidence – informal.

### 16. Duke Energy Hot Springs microgrid – 4.4 MW battery + 2 MW(AC) solar – $14.5M (2023)
- The Assembly NC: "Constructing the grid cost $14.5 million." Duke: "2-megawatt (AC) solar facility and a 4.4-megawatt lithium-based battery." NCUC approval 2019 described the battery as 4 MW/16 MWh; MWh left blank because not confirmed in retrieved excerpts. 2017 announcement: Hot Springs + Asheville "around $30 million" combined.

### 17. Dominion Energy Virginia pilot portfolio – 16 MW – ~$33M estimate
- T&D World / PRNewswire (Aug 2019): "The pilot projects will total 16 MW ... The lithium-ion battery pilots will cost approximately $33 million to construct." SCC approved Feb 2020. Scott Solar (Powhatan) 10 MW + 2 MW, 4-hour = 48 MWh, operational 2022; 2 MW New Kent; 2 MW Hanover (Ashland substation). MWh blank because 2 MW units' durations not confirmed.

### 18. PSE Glacier – 2 MW / 4.4 MWh – $11.2M (2016)
- PSE: "The Washington State Department of Commerce provided a $3.8 million Smart Grid grant, and PSE invested $7.4 million in the Glacier BESS demonstration project." PNNL test report PNNL-28379.

### 19. Chugach Electric BESS – 40 MW / 80 MWh – $65M (2024)
- Energy-Storage.News / Chugach: "The US$65 million BESS consists of 24 Tesla Megapack units"; ADN (July 2023) headline "$63 million Tesla battery system". Co-owned 75% Chugach / 25% MEA; may qualify for ITC. Range $63–65M; $65M used.

### 20. DTE Trenton Channel – 220 MW / 880 MWh – ~$460M (2026 planned)
- Energy-Storage.News: "The MPSC stated the expected cost of the project would be around US$460 million"; "$140 million in tax incentives" (IRA). Includes new substation and transmission tie. Powin LFP; MPSC approval Mar 2024.

### 21–22. TEP Roadrunner Reserve Phase 1 and Phase 2 – 200 MW / 800 MWh each
- tucson.com (Oct 2023): "Tucson Electric Power plans $294M battery plant"; DEPCOM Power EPC. TEP news: first 200 MW "representing a $350 million investment"; second 200 MW "about $350 million investment", online June 2026.
- Problem: unclear whether $350M supersedes $294M for Phase 1. Phase 1 recorded at $294M (announcement estimate) with $350M noted; Phase 2 recorded at $350M.

### 23. Xcel Energy Minnesota utility-owned battery program – 200 MW – $430M
- Utility Dive / pv magazine (Apr 2026): "The PUC approved Xcel's proposed 200 MW with an interim program assessment at 50 MW, with the program's full-capacity budget being $430 million."
- Problem: programmatic budget across multiple distribution sites; duration not confirmed. Included because it is a regulator-approved, utility-owned, distribution-connected cost basis.

### 24. IPL Harding Street – 20 MW / 20 MWh – $25M (2016)
- Utility Dive (2015): "IPL plans a $25 million power-storage facility at Harding Street plant"; COD May 20, 2016; placed in rate base. Announcement estimate.

### 25. Austin Energy Kingsbery – 1.5 MW / 3 MWh – $3M (2016)
- Austin American-Statesman: "The $3 million cost was partially defrayed with a $1 million grant from the Texas Commission on Environmental Quality."

### 26. Nova Scotia Power BESS portfolio (3 x 50 MW / 200 MWh) – C$354M incl. AFUDC [CANADA]
- CBC / Energy-Storage.News (2024): "total expected cost of the 150MW BESS buildout is CA$354 million, including AFUDC. The capital cost to NS Power's customer base will be approximately CA$243 million" (after C$109M NRCan grant); C$138.2M CIB loan. In service 2026. Converted at ~0.73 USD/CAD => $258M.

### 27. Guam Power Authority ESS (Agana 24 MW/6 MWh; Talofofo 16 MW/16 MWh) – $43M contract
- pv magazine / Utility Dive (June 2017): "LG CNS secured a $43 million contract with GPA for the 40-MW/22-MWh energy storage systems ... turnkey basis within 12 months." Post-Guam (May 2021) reports facilities operating. COD year left blank (not confirmed).

### 28. BGE Fairhaven – 2.5 MW / 9.74 MWh – $16,161,336 actual (2023)
- MD PSC Energy Storage Pilot Program interim report: "BGE's Fairhaven Project was estimated to cost $9,841,000. However, the Company has reported actual costs of $16,161,336." MWh cited as 7.1 (proposal, degrading to 4) and 9.74 (report). Strong comparable: IOU-owned, substation-sited, ~4-hour, PJM.

### 29. SaskPower Regina BESS – 20 MW – C$34M (2024) [CANADA]
- CBC: "The $34-million facility ... capable of providing 20 megawatts"; "initially projected to cost an estimated $26 million"; federal $13.1M. MWh not confirmed in excerpt (left blank). Converted at ~0.74 => $25M.

### 30. GMP Stafford Hill – 4 MW / 3.4 MWh – $4.2M storage component (2015)
- Clean Energy Group: "the storage component cost about $4.2 million, with the solar installation costing about $5.77 million" (total ~$10M). Mixed chemistry: 4 x 500 kW/250 kWh Li-ion + 4 x 500 kW/600 kWh advanced lead-acid.

### 31–32. SDG&E Westside Canal Phase 2a (119 MW, $267.9M, COD Dec 2024) and Phase 2b (100 MW, $224.5M, 2025)
- Sempra release / CPUC: "The estimated total cost of the project is $267.9 million" (2a); "The estimated total cost of the project is $224.5 million. The expansion project will add 100 MW ... to the existing 131 MW facility" (2b, CPUC approval Mar 2025). MWh not confirmed in excerpts (left blank; SDG&E's utility-owned fleet is described as ~480 MW / 1.9 GWh, i.e. ~4-hour).

### 33. UK Power Networks Smarter Network Storage – 6 MW / 10 MWh – £18.7M (2014) [UK]
- "The project cost £18.7 million" (edie / pv magazine); Low Carbon Networks Fund; includes trials/R&D. Converted at ~1.55 => $29M.

### 34. ElectraNet Dalrymple ESCRI – 30 MW / 8 MWh – A$30M (2018) [AUSTRALIA]
- ARENA: "ARENA provided $12 million in funding towards the construction of the $30 million ... ESCRI project"; grant later repaid. Converted at ~0.74 => $22.2M.

### 35. Oneida Energy Storage – 250 MW / 1,000 MWh – ~C$700M (2025) [CANADA, IPP]
- Northland Power (May 2025): completed "below budget"; NS Energy: "final cost of approximately $700 million, compared to the initial $800 million estimate at financial close in 2023." Converted at ~0.73 => $511M.

### 36. CPS Energy SwRI solar+storage – 5 MW PV + 10 MW / 10 MWh – $16.3M (2019)
- POWER/PRNewswire: "The $16.3 million project was approved by CPS Energy's Board of Trustees and consists of a 5 megawatt (MW) solar power facility and a 10 MW battery storage system"; $3M TCEQ grant. Solar included.

### 37. SCE substation BESS portfolio (Ameresco EPCM) – 537.5 MW / 2,150 MWh – $1.226B (2022)
- CPUC press release (Dec 2021): "authorized SCE to enter into a $1.226 billion, 537.5 megawatt ... engineering, procurement, construction, and maintenance energy storage contract with Ameresco"; Springvale 225 MW, Hinson 200 MW, Etiwanda 112.5 MW; 4-hour; online by Aug 2022. Contract includes maintenance.

### 38. Yukon Energy Whitehorse BESS – 7 MW / 40 MWh – C$31.7M estimate [CANADA]
- Yukon Energy / YUB application: "preliminary capital cost estimate (2020$, +/- 30% accuracy) is $31.7 million"; federal C$16.5M. SunGrid Solutions EPC. COD not confirmed in excerpts. Converted at ~0.745 => $23.6M.

### 39. Duke Energy Asheville Rock Hill – 9 MW – "<$15M" (2020)
- Duke release: "With a total cost of less than $15 million, the project will primarily be used to help the electric system operate more efficiently." Upper bound recorded; MWh not confirmed.

### 40. Vistra Morro Bay BESS (proposed) – 600 MW / 2,400 MWh – $500–600M estimate
- Estero Bay News: "Vistra estimates a project to cost $500-$600 million and will result in a value of some $450 million for property tax purposes." Midpoint $550M. Not approved; reported shelved. Low confidence, IPP.

### 41. Synergy Kwinana BESS 1 – 100 MW / 200 MWh – A$155M (USD 103.5M) (2023) [AUSTRALIA]
- pv magazine Australia: "The $155 million (USD 103.5 million) battery"; state-owned utility; decommissioned coal-plant site.

### 42. TransAlta WindCharger – 10 MW / 20 MWh – C$14.5M (USD 11M) (2020) [CANADA, IPP]
- Renewables Now: "total capital cost of CAD 14.5 million (USD 11m) ... around 50% of the funding through ... Emissions Reduction Alberta." Tesla Megapack at Summerview II wind farm.

### 43. Weld Energy Storage (NextEra, for Platte River) – 400 MWh – $141M (2026 planned)
- ColoradoBiz: "Platte River Power Authority has a $141 million battery project in Weld County ... up to 400 megawatt-hours ... owned and operated by Weld Energy Storage." MW not confirmed (left blank). IPP-owned with long-term storage agreement.

### 44. Glenarm BESS (EPC Energy SPE, for Pasadena Water & Power) – 25 MW / 100 MWh – $55.3M 15-year contract
- Pasadena Now: "approved a 15-year, $55.3 million contract with Glenarm BESS LLC ... for a 25 MW battery energy storage system"; $9.6M CEC DEBA grant to PWP; COD 2027.
- Problem: contract value (services), not construction cost.

---

## Projects investigated but excluded (no usable cost figure or wrong technology)
- SDG&E Escondido 30/120 and El Cajon (2017): cost not disclosed (AES contract).
- SCE Mira Loma 20/80: no cost disclosed.
- PG&E Elkhorn 182.5/730: CPUC approved 2018; cost not found in excerpts.
- Georgia Power Mossy Branch 65/260: cost redacted as trade secret in GA PSC docket.
- APS Punkin Center 2/8: cost confidential (AES contract).
- Unitil Townsend 2/4 (2021): only a $1.2M state grant disclosed.
- Holyoke G&E Mt. Tom 3/6 (2018): only $475k DOER grant disclosed; Engie-owned.
- Wakefield MGLD 3/5 (2019) and Templeton 1.6/3.2 (2019): no total cost (ACES grant ~30% for Wakefield).
- Lightshift/MMWEC muni projects (Groton, Ipswich, Marblehead, Wakefield 5 MW, etc.): third-party owned; no capex disclosed.
- Con Edison Fox Hills 7.5/30 (2023) and Brownsville 5.8 MW (2025): no cost disclosed.
- Central Hudson: no owned project found (10 MW dispatch-rights RFP only).
- Homer Electric 46.5/93 (2022): HEA/Tesla did not release cost; only a $38M USDA RUS loan is public (lower bound at best).
- GVEA 46/92: vendor selected 2025; no final budget ("no final budget or construction timeframe has been established").
- Idaho Power Hemingway 80/320 (2025): cost not found in excerpts (may be in IPUC case IPC-E-23-20 / order 36817).
- IID 30/20 (2016): CESP supply contract value not found.
- LADWP Beacon 20/10 (2018): no cost.
- TVA Vonore 20/40 (2024): no cost.
- United Power Firestone 4/16 (2018): no cost (only ~$1M/yr savings).
- Alabama Power Gorgas 150 MW 2-hour (2027): no cost.
- Alliant Grant County 100/400 (2025): no cost; Columbia 20/200 is CO2 (Energy Dome), not Li-ion.
- Xcel Sherco Form Energy 10/1000: iron-air, not Li-ion; excluded.
- Snohomish MESA 1 (2 x 1 MW/0.5 MWh) and MESA 2 (2.2 MW/8 MWh vanadium flow): Clean Energy Fund $7.3M/$6.6M and a HeraldNet "$11.2 million" headline cover both, mixed chemistry; not separable – excluded.
- Avista Turner (vanadium flow) and Kodiak (originally lead-acid) excluded on chemistry.
- Vermont Electric Coop Hinesburg 1/4: leased from Viridity; no capex.
- Liberty Utilities NH: residential Powerwall pilot, not stationary utility-scale.
- GMP Panton 1/4: only "about $700,000" for microgrid additions – not the battery cost.
- Consumers Energy (Voyager/Tibbits) and KIUC: PPAs, not capex.
- Kapolei Energy Storage 185/565: $219M financing only; developer declined to give cost.
- Vistra Moss Landing I–III, Manatee (FPL), Crimson, Edwards Sanborn, Gemini: no project-level capex disclosed in retrievable sources.
- WEC Paris (110 MW battery within $390M solar-battery park) and Darien ($446M incl. 250 MW solar): not separable.
- Pepco/Delmarva MD pilots: costs are in the MD PSC interim report (blocked host); not captured.
- Colorado Springs Utilities Jackson Fuller (100 MWh, 2025): no cost.
- Nome JUS (2024): only $2.3M in grants disclosed.
- Hornsdale Power Reserve (A$90M, Neoen IPP, Australia): excluded as non-utility, non-US.

## Known data problems (read before using statistically)
1. **Bundled scope**: Nantucket (15 MW diesel generator), Provincetown (fiber/control network, loop circuitry, building), Salem SSPC (smart-grid demo), Arlington and Hot Springs (solar + microgrid), Essex, Stafford Hill and CPS SwRI (solar), SCE (includes maintenance), DTE (new substation + transmission). Battery-only shares are not disclosed for these.
2. **Estimates vs actuals**: rows flagged "estimate" or "approved budget" (MV Ph1/2, Waena, Dominion, Harding Street, TEP, DTE, Xcel program, Westside Canal, Yukon, Morro Bay, Weld) are pre-construction figures. BGE Fairhaven shows a 64% overrun from estimate to actual, Provincetown ran above its $35–45M approved range, SaskPower rose from C$26M to C$34M, Waena from ~$60M to $82.1M (+ up to 20%).
3. **Upper bounds / midpoints**: Duke Asheville is "<$15M"; Morro Bay is a range midpoint; Chugach $63–65M.
4. **Not capex**: Glenarm (15-year service contract value). Seaside is a fixed-price BTA excluding AFUDC; Constable includes AFUDC.
5. **Programmatic**: Xcel MN $430M is a 200 MW multi-site program budget.
6. **Tax credits**: post-2022 US rows (Reid Gardner, Seaside/Constable, DTE, TEP, Chugach, SDG&E) are gross of IRA ITC unless noted; pre-2022 rows had no ITC for standalone storage.
7. **Blank fields**: mwh blank for Hot Springs, Dominion portfolio, Xcel program, Westside Canal 2a/2b, SaskPower, Asheville; mw blank for Weld; cod_year blank for Guam, Yukon, Morro Bay. Duration cannot be derived for those rows.
8. **Currency conversions** for NS Power, SaskPower, Yukon, Oneida, UKPN, Dalrymple are approximate and mine; Kwinana and WindCharger use the USD figure given by the source.
9. **Chemistry**: Stafford Hill is half advanced lead-acid; all others Li-ion (LFP or NMC).
10. **Verification gap**: primary documents were not opened; every figure came from search-result excerpts. Highest-priority items to verify at source: mass.gov utility-owned BESS page (Provincetown, Nantucket, MV, Unitil), MD PSC interim report (BGE + Pepco/Delmarva), PGE 2024 10-K, HEI 10-Q, CPUC SCE resolution, NYPA release, O&R release.
11. **Nominal dollars**: all costs are nominal in the year reported; no escalation applied. Years span 2013–2027.

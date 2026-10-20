# Sources — dataset for "Programmers Deserve Teachers' Holidays"

Date of download/consultation for everything: **2026-10-20**. The original files (`raw/`) are not included in the repo: they can be downloaded from the URLs in each section.
Evidence status: **verified** = figure read by me in the downloaded primary file/PDF; **reported** = figure taken from the press or an official note without the primary report.

---

## S1 — Annual hours per worker (OWID: Huberman & Minns + Penn World Table)
- CSV URL: https://ourworldindata.org/grapher/annual-working-hours-per-worker.csv?v=1&csvType=full&useColumnShortNames=true
- Metadata URL: https://ourworldindata.org/grapher/annual-working-hours-per-worker.metadata.json (+ full: https://api.ourworldindata.org/v1/indicators/1103669.metadata.json)
- Dataset: "Working hours per worker – Huberman and Minns, Penn World Table" (OWID variable 1103669; lastUpdated 2025-08-05; timespan 1870–2023).
- Origins: Feenstra, Inklaar & Timmer, *Penn World Table 11.0* (indicator `avh`, 1950 onwards), licence **CC BY 4.0**; Huberman, M. & Minns, C. (2005) "Hours of Work in Old and New Worlds: The Long View, 1870-2000", IIIS Discussion Paper 95, Tables 1–3 (1870–1938), licence "© 2005 Huberman and Minns" (OWID redistributes it; cite both). Note: the published version is Huberman & Minns (2007), *Explorations in Economic History* 44(4); OWID cites the 2005 working paper.
- Files: `raw/annual-working-hours-per-worker.csv` (columns: entity, code, year, working_hours_omm, owid_region) → `annual_hours_per_worker_5countries.csv` (columns: country, year, annual_hours_per_worker, source_segment) for Spain, United Kingdom, United States, Germany, France.
- Coverage: 1870, 1880, 1890, 1900, 1913, 1929, 1938 (Huberman–Minns, isolated data points) and annual 1950–2023 (PWT). Status: verified.

## S2 — Productivity: GDP per hour worked (OWID / Penn World Table)
- CSV URL: https://ourworldindata.org/grapher/labor-productivity-per-hour-pennworldtable.csv?v=1&csvType=full&useColumnShortNames=true
- Metadata URL: https://ourworldindata.org/grapher/labor-productivity-per-hour-pennworldtable.metadata.json (+ https://api.ourworldindata.org/v1/indicators/1108544.metadata.json)
- Dataset: "Productivity: output per hour worked" (OWID variable 1108544; lastUpdated 2025-10-09; timespan 1950–2023). GDP (output side, multiple benchmarks) / (employment × average hours). Unit: international dollars at 2021 prices per hour (PPP).
- Origin: Penn World Table 11.0 (Feenstra et al.), **CC BY 4.0**, processed by OWID (CC BY 4.0).
- Files: `raw/labor-productivity-per-hour-pennworldtable.csv` (entity, code, year, productivity) → `productivity_per_hour_5countries.csv` (country, year, gdp_per_hour_intl_usd_2021).
- The alternative URL `productivity-per-hour-worked` returns **404** (that slug does not exist); not used.
- Status: verified.

## S3 — Derived table: productivity vs hours, 1950→2023
- File: `productivity_vs_hours_1950_2023.csv` (country, prod_1950, prod_2023, prod_multiple, hours_1950, hours_2023, hours_change_pct, hours_1870, hours_change_1870_2023_pct). Calculated by me from S1 and S2 (no other transformation).

## S4 — Actual weekly hours (Eurostat lfsa_ewhan2)
- URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/lfsa_ewhan2/A.TOTAL.EMP+SAL.TOTAL+FT+PT.Y15-64.T.HR.ES+EU27_2020+DE+FR+NL+IT/?format=SDMX-CSV&startPeriod=2008
- Dataset: Eurostat `lfsa_ewhan2` "Average number of actual weekly hours of work in main job, by sex, age, professional status, full-time/part-time and economic activity" (EU-LFS). Last update shown in the file: 10/09/26. Licence: Eurostat reuse policy (Decision 2011/833/EU; equivalent to CC BY 4.0).
- Filters: nace_r2=TOTAL; wstatus=EMP (employed persons) and SAL (employees); worktime=TOTAL/FT/PT; age=Y15-64; sex=T; unit=HR; geo=ES, EU27_2020, DE, FR, NL, IT; 2008–2025.
- Files: `raw/lfsa_ewhan2.csv` (raw SDMX-CSV) → `eurostat_actual_weekly_hours_lfsa_ewhan2.csv` (geo, wstatus, worktime, year, actual_weekly_hours_main_job, flag). Flag `d` = definition differs; `b` = break in series (ES from 2024 onwards and FR 2024 carry `d`/`bd`).
- Not downloaded: INE EPA (Spain's Labour Force Survey; actual hours table) — Eurostat already provides the harmonised version of the EPA.
- Status: verified.

## S6 — UK four-day week pilot 2022 (final report)
- URL: https://autonomy.work/wp-content/uploads/2023/02/The-results-are-in-The-UKs-four-day-week-pilot.pdf (page: https://autonomy.work/portfolio/uk4dwpilotresults/)
- Autonomy / 4 Day Week Global / Boston College / Cambridge, "The results are in: The UK's four-day week pilot", February 2023. Licence: not stated (cite with attribution).
- Figures used in `four_day_week_trials.csv`, read in the PDF (pp. ~4–6, 29, 30, 32): 61 companies, ~2,900 workers; 56 continue (92%), 18 permanently; revenue +1.4% start→end (n=23) and +34.5% vs a comparable period (n=24); resignations 2.0→0.8 per 100 (−57%); sick days + personal days 2.0→0.7 per employee/month (−65%); **the report itself says these three trends are not statistically significant**; 71% less burnout, 39% less stress; hours 38→34/week. Status: verified.

## S7 — UK pilot, one-year follow-up
- URL: https://autonomy.work/wp-content/uploads/2024/02/making-it-stick_-1.pdf (page: https://autonomy.work/portfolio/making-it-stick/)
- Autonomy, "Making It Stick: The UK Four-Day Week Pilot One Year On", February 2024.
- Figures: at least 54 of 61 continue (89%); at least 31 permanently (51%). Status: verified.

## S8 — US/Ireland pilot 2022
- URL: https://www.4dayweek.com/s/US-Ireland-Results-2023.pdf (redirects to static1.squarespace.com; page https://www.4dayweek.com/us-ireland-results)
- Schor, J.B., Fan, W., Kelly, O., Gu, G., Bezdenezhnykh, T., Bridson-Hubbard, N. (2022) "The Four Day Week: Assessing Global Trials of Reduced Work Time with No Reduction in Pay", Four Day Week Global, Auckland.
- Figures: 33 companies, 903 employees; 27 respond: 18 definitely continuing, 7 planning to, 1 leaning towards it, 0 against; revenue +8.14% (n=16) and +37.55% vs 2021 (n=20); resignations 1.76→1.70; absenteeism 0.56→0.39 days/month (not significant); hours 40.83→34.83; 96.9% want to continue. Status: verified.

## S9 — Portugal, interim report (Dec 2023)
- URL: https://rr.pt/noticia/economia/2023/12/12/semana-de-quatro-dias-reduz-em-137-em-media-de-horas-de-trabalho-semanais/358908/ (Renascença/Lusa, 12 Dec 2023, citing the report by Pedro Gomes and Rita Fontinha for the IEFP).
- Figures: hours 39.3→34 according to companies (−13.7%); 41.1→36.5 according to workers (−11.3%); anxiety −21%, fatigue −23%; 95% of companies rate it positively. Status: **reported** (IEFP PDF not located).

## S10 — Portugal, final report (24 Jun 2024)
- URLs: https://rr.pt/artigo/explicador-renascenca/2024/06/24/trabalhadores-e-empresas-que-testaram-semana-de-quatro-dias-querem-manter-o-modelo/383570/ ; https://www.rtp.pt/noticias/economia/mais-de-80-das-empresas-que-testaram-semana-de-4-dias-decidiram-manter-modelo_n1581253
- Figures: 41 companies, 6 months; exhaustion −19%; 93% of workers want to continue; ">80%" of companies (RTP: they are keeping it; Renascença: they rate it positively / financially neutral). Status: **reported**; the continuation figure is ambiguous.

## S11 — Germany, 2024 pilot
- URL: https://idw-online.de/de/news841503 (University of Münster press release, 18 Oct 2024; Prof. Julia Backmann, Dr Felix Hoch).
- Figures: 45 organisations; 41 completed or nearly completed; 2 dropped out; >70% want to continue; +38 min sleep/week vs control group; turnover and profit slightly up but not significant; sick leave slightly down, not significant. Status: **reported** (press release from the research team, not the full report). The "73%" circulating in the press does not appear in the release.

## S12 — Vote on the 37.5-hour bill
- URL: https://www.congreso.es/docu/tramit/LegXV/AT/ATCD_15_PL_20250910.pdf (verbatim record, plenary session of 10 Sep 2025, p. 198). File 121/000058, "Proyecto de Ley para la reducción de la duración máxima de la jornada ordinaria de trabajo y la garantía del registro de jornada y el derecho a la desconexión" (Bill to reduce the maximum length of the ordinary working day and guarantee working-time recording and the right to disconnect).
- Result: amendments to the whole calling for the bill to be returned to the Government (Junts, VOX, PP) passed: 348 votes cast, 178 in favour, 170 against → **bill rejected**. Status: verified.
- Current statutory working week of 40 h: art. 34.1 of the Workers' Statute (Estatuto de los Trabajadores, Royal Legislative Decree 2/2015); the record of proceedings of 14 Oct 2025 itself notes that it has been "set at a maximum of 40 hours since 1983".

## S13 — BNG 35-hour private member's bill
- URL: https://www.congreso.es/docu/tramit/LegXV/AT/ATCD_15_PL_20251014.pdf (verbatim record, plenary session of 14 Oct 2025; the record's header says "Wednesday", but 14 Oct 2025 was a Tuesday). File 122/000159.
- Result: not taken into consideration: 346 votes cast, 162 in favour, 178 against, 6 abstentions. Status: verified.

## S14 — Status in 2026
- Web searches on 2026-10-20: I found no new 37.5-hour bill tabled or passed; the royal decree on digital working-time recording had still not been approved as of July 2026, according to the press (https://www.que.es/2026/07/17/nuevo-registro-horario-julio-2026/). Status: **not verified** (not finding it does not prove it doesn't exist; check the BOE and congreso.es before publishing).

## S15 — Ministry of Industry pilot (EOI)
- URLs: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/industria/Paginas/2023/170323-empresas-programa-piloto-jornada-4-dias.aspx (17 Mar 2023: 41 companies apply); https://www.mintur.gob.es/es-es/gabineteprensa/notasprensa/2024/paginas/resolucion-definitiva-proyecto-piloto-reduccion-jornada-laboral-eoi.aspx (20 Sep 2024).
- Figures (2024 note, read): 42 applicants, **5 beneficiaries**, almost €530,000; an international comparative study is announced. Initial budget for the call ~€10m (€9.6m according to the press). **I found no published results.** Status: verified (award decision); results = not run/not published.

## S16 — Valencian Community
- URL: https://www.eldiario.es/comunitat-valenciana/valencia-constata-trabajar-cuatro-dias-mejora-salud-reduce-estres-generalitat-pp-vox-elimina-ayudas_1_10603853.html (20 Oct 2023).
- Two separate things: (a) **Generalitat (regional government) grants** (2022–2023) for SMEs that cut working hours by ≥20% without cutting pay: 1st call ~3 SMEs, 2nd call 18; suspended in Oct 2023 for "lack of interest" (and the 2024 budget line only to pay what had already been awarded: https://valenciaplaza.com/valenciaplaza/mazon-mantiene-las-ayudas-a-la-semana-laboral-de-cuatro-dias-en-2024-pese-a-anunciar-susupresion). (b) **City of València**: 4 four-day weeks (10 Apr to 7 May 2023) taking advantage of public holidays; evaluation by Las Naves/Avalua·lab: 64% slept more, 34% less stress, 45.5% more job satisfaction, retailers reported −20% sales. Status: **reported** (press; original report not located).
- I found no "2024 Valencian pilot" with results different from these.

# Fuentes — dataset "Programadores con vacaciones de profesor"

Fecha de descarga/consulta de todo: **2026-10-20**. Los ficheros originales (`raw/`) no se incluyen en el repo: se pueden descargar de las URL de cada apartado.
Estado de evidencia: **verificado** = cifra leída por mí en el fichero/PDF primario descargado; **reportado** = cifra tomada de prensa o de una nota oficial sin el informe primario.

---

## S1 — Horas anuales por trabajador (OWID: Huberman & Minns + Penn World Table)
- URL CSV: https://ourworldindata.org/grapher/annual-working-hours-per-worker.csv?v=1&csvType=full&useColumnShortNames=true
- URL metadatos: https://ourworldindata.org/grapher/annual-working-hours-per-worker.metadata.json (+ completo: https://api.ourworldindata.org/v1/indicators/1103669.metadata.json)
- Dataset: "Working hours per worker – Huberman and Minns, Penn World Table" (OWID variable 1103669; lastUpdated 2025-08-05; timespan 1870-2023).
- Orígenes: Feenstra, Inklaar & Timmer, *Penn World Table 11.0* (indicador `avh`, 1950+), licencia **CC BY 4.0**; Huberman, M. & Minns, C. (2005) "Hours of Work in Old and New Worlds: The Long View, 1870-2000", IIIS Discussion Paper 95, Tablas 1-3 (1870-1938), licencia "© 2005 Huberman and Minns" (OWID la redistribuye; citar ambos). Nota: la versión publicada es Huberman & Minns (2007), *Explorations in Economic History* 44(4); OWID cita el working paper de 2005.
- Ficheros: `raw/annual-working-hours-per-worker.csv` (columnas: entity, code, year, working_hours_omm, owid_region) → `annual_hours_per_worker_5countries.csv` (columnas: country, year, annual_hours_per_worker, source_segment) para Spain, United Kingdom, United States, Germany, France.
- Cobertura: 1870, 1880, 1890, 1900, 1913, 1929, 1938 (Huberman-Minns, puntos sueltos) y anual 1950-2023 (PWT). Estado: verificado.

## S2 — Productividad: PIB por hora trabajada (OWID / Penn World Table)
- URL CSV: https://ourworldindata.org/grapher/labor-productivity-per-hour-pennworldtable.csv?v=1&csvType=full&useColumnShortNames=true
- URL metadatos: https://ourworldindata.org/grapher/labor-productivity-per-hour-pennworldtable.metadata.json (+ https://api.ourworldindata.org/v1/indicators/1108544.metadata.json)
- Dataset: "Productivity: output per hour worked" (OWID variable 1108544; lastUpdated 2025-10-09; timespan 1950-2023). PIB (output side, multiple benchmarks) / (empleo × horas medias). Unidad: dólares internacionales a precios de 2021 por hora (PPA).
- Origen: Penn World Table 11.0 (Feenstra et al.), **CC BY 4.0**, procesado por OWID (CC BY 4.0).
- Ficheros: `raw/labor-productivity-per-hour-pennworldtable.csv` (entity, code, year, productivity) → `productivity_per_hour_5countries.csv` (country, year, gdp_per_hour_intl_usd_2021).
- La URL alternativa `productivity-per-hour-worked` devuelve **404** (no existe ese slug); no se usa.
- Estado: verificado.

## S3 — Tabla derivada productividad vs horas 1950→2023
- Fichero: `productivity_vs_hours_1950_2023.csv` (country, prod_1950, prod_2023, prod_multiple, hours_1950, hours_2023, hours_change_pct, hours_1870, hours_change_1870_2023_pct). Calculado por mí a partir de S1 y S2 (sin otra transformación).

## S4 — Horas semanales efectivas (Eurostat lfsa_ewhan2)
- URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/lfsa_ewhan2/A.TOTAL.EMP+SAL.TOTAL+FT+PT.Y15-64.T.HR.ES+EU27_2020+DE+FR+NL+IT/?format=SDMX-CSV&startPeriod=2008
- Dataset: Eurostat `lfsa_ewhan2` "Average number of actual weekly hours of work in main job, by sex, age, professional status, full-time/part-time and economic activity" (EU-LFS). Última actualización en el fichero: 10/09/26. Licencia: reutilización Eurostat (Decisión 2011/833/UE; equivalente a CC BY 4.0).
- Filtros: nace_r2=TOTAL; wstatus=EMP (ocupados) y SAL (asalariados); worktime=TOTAL/FT/PT; age=Y15-64; sex=T; unit=HR; geo=ES, EU27_2020, DE, FR, NL, IT; 2008-2025.
- Ficheros: `raw/lfsa_ewhan2.csv` (SDMX-CSV crudo) → `eurostat_actual_weekly_hours_lfsa_ewhan2.csv` (geo, wstatus, worktime, year, actual_weekly_hours_main_job, flag). Flag `d` = definición difiere; `b` = ruptura de serie (ES desde 2024 y FR 2024 llevan `d`/`bd`).
- No descargado: INE EPA (tabla de horas efectivas) — Eurostat ya es la EPA armonizada.
- Estado: verificado.

## S6 — UK four-day week pilot 2022 (informe final)
- URL: https://autonomy.work/wp-content/uploads/2023/02/The-results-are-in-The-UKs-four-day-week-pilot.pdf (página: https://autonomy.work/portfolio/uk4dwpilotresults/)
- Autonomy / 4 Day Week Global / Boston College / Cambridge, "The results are in: The UK's four-day week pilot", febrero 2023. Licencia: no declarada (cita con atribución).
- Cifras usadas en `four_day_week_trials.csv` leídas en el PDF (págs. ~4-6, 29, 30, 32): 61 empresas, ~2.900 trabajadores; 56 continúan (92 %), 18 permanentes; ingresos +1,4 % inicio→fin (n=23) y +34,5 % vs periodo comparable (n=24); bajas voluntarias 2,0→0,8 por 100 (-57 %); días de baja+asuntos propios 2,0→0,7 por empleado/mes (-65 %); **el propio informe dice que estas tres tendencias no son estadísticamente significativas**; 71 % menos burnout, 39 % menos estrés; horas 38→34/semana. Estado: verificado.

## S7 — UK pilot, seguimiento a un año
- URL: https://autonomy.work/wp-content/uploads/2024/02/making-it-stick_-1.pdf (página: https://autonomy.work/portfolio/making-it-stick/)
- Autonomy, "Making It Stick: The UK Four-Day Week Pilot One Year On", febrero 2024.
- Cifras: al menos 54 de 61 siguen (89 %); al menos 31 permanentes (51 %). Estado: verificado.

## S8 — US/Ireland pilot 2022
- URL: https://www.4dayweek.com/s/US-Ireland-Results-2023.pdf (redirige a static1.squarespace.com; página https://www.4dayweek.com/us-ireland-results)
- Schor, J.B., Fan, W., Kelly, O., Gu, G., Bezdenezhnykh, T., Bridson-Hubbard, N. (2022) "The Four Day Week: Assessing Global Trials of Reduced Work Time with No Reduction in Pay", Four Day Week Global, Auckland.
- Cifras: 33 empresas, 903 empleados; 27 responden: 18 continúan seguro, 7 planean, 1 inclinada, 0 en contra; ingresos +8,14 % (n=16) y +37,55 % vs 2021 (n=20); bajas voluntarias 1,76→1,70; absentismo 0,56→0,39 días/mes (no significativos); horas 40,83→34,83; 96,9 % quiere continuar. Estado: verificado.

## S9 — Portugal, informe intermedio (dic. 2023)
- URL: https://rr.pt/noticia/economia/2023/12/12/semana-de-quatro-dias-reduz-em-137-em-media-de-horas-de-trabalho-semanais/358908/ (Renascença/Lusa, 12-12-2023, citando el informe de Pedro Gomes y Rita Fontinha para el IEFP).
- Cifras: horas 39,3→34 según empresas (-13,7 %); 41,1→36,5 según trabajadores (-11,3 %); ansiedad -21 %, fatiga -23 %; 95 % de empresas valoran positivamente. Estado: **reportado** (PDF del IEFP no localizado).

## S10 — Portugal, informe final (24-jun-2024)
- URLs: https://rr.pt/artigo/explicador-renascenca/2024/06/24/trabalhadores-e-empresas-que-testaram-semana-de-quatro-dias-querem-manter-o-modelo/383570/ ; https://www.rtp.pt/noticias/economia/mais-de-80-das-empresas-que-testaram-semana-de-4-dias-decidiram-manter-modelo_n1581253
- Cifras: 41 empresas, 6 meses; agotamiento -19 %; 93 % de trabajadores quiere continuar; ">80 %" empresas (RTP: lo mantienen; Renascença: lo valoran positivamente / financieramente neutro). Estado: **reportado**; el dato de continuidad es ambiguo.

## S11 — Alemania, piloto 2024
- URL: https://idw-online.de/de/news841503 (nota de prensa Universität Münster, 18-10-2024; Prof. Julia Backmann, Dr. Felix Hoch).
- Cifras: 45 organizaciones; 41 completadas o casi; 2 abandonan; >70 % quiere continuar; +38 min sueño/semana vs grupo control; facturación y beneficio ligeramente al alza pero no significativos; bajas ligeramente a la baja, no significativas. Estado: **reportado** (nota de prensa del equipo investigador, no informe completo). El "73 %" que circula en prensa no aparece en la nota.

## S12 — Votación del proyecto de ley de 37,5 h
- URL: https://www.congreso.es/docu/tramit/LegXV/AT/ATCD_15_PL_20250910.pdf (Acta taquigráfica, Pleno 10-sep-2025, pág. 198). Expediente 121/000058, "Proyecto de Ley para la reducción de la duración máxima de la jornada ordinaria de trabajo y la garantía del registro de jornada y el derecho a la desconexión".
- Resultado: enmiendas a la totalidad de devolución (Junts, VOX, PP) aprobadas: 348 emitidos, 178 a favor, 170 en contra → **proyecto rechazado**. Estado: verificado.
- Jornada legal vigente 40 h: art. 34.1 Estatuto de los Trabajadores (RDL 2/2015); el propio diario de sesiones de 14-oct-2025 recuerda "fijada en un máximo de 40 horas desde 1983".

## S13 — Proposición de ley BNG 35 h
- URL: https://www.congreso.es/docu/tramit/LegXV/AT/ATCD_15_PL_20251014.pdf (Acta taquigráfica, Pleno 14-oct-2025; el encabezado del acta dice "miércoles", pero el 14-oct-2025 fue martes). Expediente 122/000159.
- Resultado: no tomada en consideración: 346 emitidos, 162 a favor, 178 en contra, 6 abstenciones. Estado: verificado.

## S14 — Estado en 2026
- Búsquedas web del 2026-10-20: no encontré ningún nuevo proyecto de 37,5 h presentado ni aprobado; el real decreto de registro digital de jornada seguía sin aprobarse en julio de 2026 según prensa (https://www.que.es/2026/07/17/nuevo-registro-horario-julio-2026/). Estado: **no verificado** (que no lo encontrara no prueba que no exista; mirar BOE y congreso.es antes de publicar).

## S15 — Piloto del Ministerio de Industria (EOI)
- URLs: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/industria/Paginas/2023/170323-empresas-programa-piloto-jornada-4-dias.aspx (17-03-2023: 41 empresas solicitan); https://www.mintur.gob.es/es-es/gabineteprensa/notasprensa/2024/paginas/resolucion-definitiva-proyecto-piloto-reduccion-jornada-laboral-eoi.aspx (20-09-2024).
- Cifras (nota de 2024, leída): 42 solicitantes, **5 beneficiarias**, casi 530.000 €; se anuncia un estudio comparativo internacional. Presupuesto inicial de la convocatoria ~10 M€ (9,6 M€ según prensa). **No encontré resultados publicados.** Estado: verificado (resolución), resultados = no ejecutado/no publicado.

## S16 — Comunitat Valenciana
- URL: https://www.eldiario.es/comunitat-valenciana/valencia-constata-trabajar-cuatro-dias-mejora-salud-reduce-estres-generalitat-pp-vox-elimina-ayudas_1_10603853.html (20-10-2023).
- Dos cosas distintas: (a) **Ayudas de la Generalitat** (2022-2023) a pymes que redujeran ≥20 % la jornada sin bajar sueldo: 1.ª convocatoria ~3 pymes, 2.ª 18; suspendidas en oct. 2023 por "falta de interés" (y partida 2024 solo para pagar lo ya concedido: https://valenciaplaza.com/valenciaplaza/mazon-mantiene-las-ayudas-a-la-semana-laboral-de-cuatro-dias-en-2024-pese-a-anunciar-susupresion). (b) **Ciudad de València**: 4 semanas de 4 días (10-abr a 7-may-2023) aprovechando festivos; evaluación de Las Naves/Avalua·lab: 64 % durmió más, 34 % menos estrés, 45,5 % más satisfacción laboral, el comercio reportó -20 % ventas. Estado: **reportado** (prensa; informe original no localizado).
- No encontré un "piloto valenciano 2024" con resultados distintos de esto.

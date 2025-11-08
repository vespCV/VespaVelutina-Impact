# Removal Priority Index (RPI): Methodology and Documentation

Version: 2025-11-08  
Maintainer: [to be verified]  
Update cadence: Monthly (synchronized with repository updates)

## Purpose
Provide a transparent, reproducible, and policy‑relevant index to prioritize areas for Asian hornet (Vespa velutina) nest removal within the next update cycle (approximately 30 days). The RPI translates occurrence intensity, apiary risk, seasonal dynamics, and cost‑of‑delay into an actionable 0–100 score with recommended actions.

Audience: Provincial coordinators, municipal decision‑makers, beekeeper organizations.

Scope: Europe (with initial operationalization for the Netherlands).

## Approved Data Sources and Access
- GBIF: `https://www.gbif.org/` (occurrence records for Vespa velutina)  
  - Accessed: [to be verified], Export: CSV, Filters: species = Vespa velutina, has coordinates = true, date within last 90 days, country/region filters as applicable.
- EPPO Global Database: `https://gd.eppo.int/` (distribution/regulatory status)  
  - Accessed: [to be verified], Use: presence/absence context and regulatory notes.
- Vespa‑Watch.nl: `https://vespa-watch.nl/` (Netherlands sightings/nests)  
  - Accessed: [to be verified], Use: recent nests/sightings; note reporting biases.
- FAOSTAT: `https://www.fao.org/faostat/` (hives and apiculture baseline)  
  - Accessed: [to be verified], Use: country‑level hives; subnational proxy [to be verified].
- InvaCost: `https://invacost.fr/` (cost categories for invasive species)  
  - Accessed: [to be verified], Use: inform cost‑of‑delay construct.
- EASIN: `https://easin.jrc.ec.europa.eu/` (suitability, climate context)  
  - Accessed: [to be verified], Use: context for seasonal factor assumptions.

All downloads must record: download date, version/DOI where applicable, filters applied, preprocessing steps (see Data Management Standards in README).

## Spatial Units
Two recommended options (choose one and document choice):
1) Administrative: municipality (or LAU level) codes.  
2) Hexagonal grid: H3 (e.g., resolution 7–8) covering target country/region.

Document the chosen unit in the monthly CSV (column `area_id_type`: admin | h3).

## Variables and Definitions
Let areas be indexed by i.
- S_30d_i: Number of validated sightings/nests in last 30 days in area i (secondary nests weighted higher than primary/embryonal where identifiable). Source: Vespa‑Watch.nl and/or GBIF.
- S_90d_i: Number of validated sightings/nests in last 90 days in area i (for smoothing and momentum).
- SecRate_i: Share of secondary nests among all nests in last 90 days in area i (proxy for reproductive/late‑season risk).
- ApiaryProxy_i: Apiary/hive density proxy for area i. If only national hives available (FAOSTAT), scale by population density or land area to approximate relative exposure [to be verified].
- SeasonFactor_i: Seasonal multiplier (0–1) capturing July–October peak and 15–26°C optimal activity (Monceau et al. 2018; Requier et al. 2019; Diéguez‑Antón et al. 2022, 2025). Example rule‑set:  
  - July–October: 1.0  
  - Shoulder months with mean daily T in 15–26°C: 0.8  
  - Otherwise: 0.5  
  Document the exact rule and meteorological source if used.
- CostDelay_i: Cost‑of‑delay multiplier (0–1) reflecting expected escalation if removal is postponed one cycle (literature‑informed by Requier et al. 2023; Barbet‑Massin et al. 2020; InvaCost categories). Start conservatively; document assumptions.

## Normalization
To ensure comparability across areas and limit outlier influence, apply percentile‑based scaling to [0,1]:
- nS_30d_i = min(1, rank_percentile(S_30d_i))
- nS_90d_i = min(1, rank_percentile(S_90d_i))
- nSec_i = SecRate_i (already 0–1)
- nApiary_i = rank_percentile(ApiaryProxy_i)
- nSeason_i = SeasonFactor_i (by definition 0–1)
- nCostDelay_i = CostDelay_i (0–1)

Note: Percentile definitions and winsorization thresholds must be documented monthly.

## Weighting Scheme
Initial weights (sum to 1; justify and adjust with sensitivity analysis):
- w_sightings = 0.40 (use nS_30d_i, optionally blend with nS_90d_i)
- w_secondary = 0.20
- w_apiary = 0.20
- w_season = 0.10
- w_costdelay = 0.10

[to be verified]: Local experts may suggest province‑specific adjustments.

## RPI Formula
RPI_i = 100 × ( w_sightings × nS_30d_i + w_secondary × nSec_i + w_apiary × nApiary_i + w_season × nSeason_i + w_costdelay × nCostDelay_i )

Range: 0–100.

## Bands and Recommended Actions
- 0–24 (Low): Monitor; beekeeper self‑protection briefing; no removal scheduling.  
- 25–49 (Moderate): Validate; remove if repeated events ≥5 hornets reported (Diéguez‑Antón et al. 2025).  
- 50–74 (High): Schedule removal ≤7 days; alert local beekeepers; pre‑position resources.  
- 75–100 (Very High): Immediate removal ≤72 h; surge capacity; consider prioritizing secondary nests.

## Output Data Model (Monthly CSV)
File: `4_data_extraction/rpi_scores_YYYYMM.csv`  
Delimiter: semicolon (;)

Columns (all required unless noted):
- area_id: Municipality code or H3 index
- area_id_type: admin | h3
- area_name: Human‑readable name (if admin)
- country: ISO‑2
- observations_30d: integer
- observations_90d: integer
- secondary_nests_90d: integer
- normalized_sightings_30d: 0–1
- secondary_rate_90d: 0–1
- apiary_proxy: numeric (document unit)
- normalized_apiary: 0–1
- seasonal_factor: 0–1
- cost_of_delay: 0–1
- rpi_score: 0–100
- rpi_band: Low | Moderate | High | Very High
- recommended_action: categorical (Monitor | Validate | Schedule ≤7d | Remove ≤72h)
- target_sla_days: integer (e.g., 2, 7, 30)
- notes: free text (assumptions, data quality flags)

## Monthly Artifact Set
- CSV scores: `4_data_extraction/rpi_scores_YYYYMM.csv`
- Choropleth map: `5_visualisation_reporting/rpi_map_YYYYMM.jpg`  
  - Legend: RPI bands; caption includes methods, data sources, and access dates.
- Table “Top 20 areas” extracted from CSV (`rpi_top20_YYYYMM.csv` or included in README section).

## Assumptions and Limitations
- Sightings and nest reports are subject to spatial/temporal reporting bias (citizen science).  
- ApiaryProxy is an approximation where subnational hive counts are unavailable.  
- Seasonal and cost‑of‑delay multipliers reflect literature‑based heuristics; validate with local experts.  
- RPI is a decision support tool, not a causal estimate of colony survival or economic loss.

## Quality Assurance
- Document all downloads (dates, filters) and preprocessing steps.  
- Validate a sample of coordinates and classifications (secondary vs primary nests).  
- Sensitivity analysis: vary weights by ±10–20% and report stability of top‑ranked areas.  
- Cross‑validate with EPPO distribution notes and EASIN suitability when feasible.

## References (URLs)
- GBIF: `https://www.gbif.org/` (citation guidelines: `https://www.gbif.org/citation-guidelines`)  
- EPPO Global Database: `https://gd.eppo.int/`  
- Vespa‑Watch.nl: `https://vespa-watch.nl/`  
- FAOSTAT: `https://www.fao.org/faostat/`  
- InvaCost: `https://invacost.fr/` (GitHub: `https://github.com/Farewe/invacost`)  
- EASIN: `https://easin.jrc.ec.europa.eu/`  
- Core studies informing thresholds:  
  - Monceau et al. 2018 [to be verified]  
  - Requier et al. 2019; Requier et al. 2020; Requier et al. 2023 [to be verified]  
  - Rojas‑Nossa et al. 2022 [to be verified]  
  - Diéguez‑Antón et al. 2022; 2025 [to be verified]  
  - Barbet‑Massin et al. 2020 [to be verified]



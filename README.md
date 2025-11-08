# Impact of Vespa velutina on Apis mellifera in Europe
_If bees only gathered nectar from perfect flowers, they wouldn't be able to make even a single drop of honey_ – Matshona Dhliwayo

- **Status:** Complete - ready for monthly updates
- **Updated:** 2025-11-08
- Klik [hier](nederlands/LEESME.md) voor de nederlandse versie.


## Summary

This repository synthesizes evidence from **30 scientific studies** to quantify the impact of Asian hornet (_Vespa velutina_) on domestic honeybee colonies (_Apis mellifera_) in Europe.

### Predation Pressure on _Apis mellifera_
- **Honeybee in diet**: 22-98% depending on method and location — [see details](#422-prey-composition)
- **Per _Vespa velutina_ colony consumption**: 
  - **11.32 kg** of insects per season
  - **97,246 honeybee-equivalent** per season
- **Observed _Vespa velutina_ counts at apiaries**: 
  - 0-4: Low pressure (observed in studies)
  - 5-9: Moderate pressure (minimum risk threshold: Diéguez-Antón et al. 2025)
  - 10-12: High pressure (foraging decline observed: Monceau et al. 2018)
  - ≥13: Very high pressure (foraging paralysis threshold: Requier et al. 2019)
- **Peak periods**: July-October (varies by location) — [see details](#422-prey-composition)
- **Predation success rate**: 2.4% (video tracking of natural predation at hive entrance) — [see details](#421-predation-rates-and-success)

### Domesticated Honeybee Colony Survival
- **Without protection**: **35-56%** of colonies survive under high _Vespa velutina_ pressure (Requier et al. 2020; Rojas-Nossa et al. 2022) — [see details](#431-colony-survival)
- **With protection** (electric harps, muzzles): **55-78%** survival (Requier et al. 2020; Rojas-Nossa et al. 2022) — [see details](#431-colony-survival)
- **Timing of colony losses**: 
  - During predation period: **2.5%** of colonies (Requier et al. 2019)
  - During winter (January-May): Majority of losses occur (Requier et al. 2019)
- **Risk threshold**: **≥5 _Vespa velutina_** at apiary (Diéguez-Antón et al. 2025) — [see details](#432-mortality-factors)
- **Colony loss**: is multifactoral, influence of _Vespa velutina_ cannot be separated from other causes of colony loss — [see details](#43-colony-survival-and-loss)

### Behavioral Changes of _Apis mellifera_
- **Foraging paralysis threshold**: **≥12.6 _Vespa velutina_** present (Requier et al. 2019) — [see details](#441-foraging-paralysis-thresholds)
- **Foraging decline threshold**: **>10 _Vespa velutina_** per hive (Monceau et al. 2018)
- **Activity reduction with protection**: Up to **41%** reduction in foraging paralysis (Requier et al. 2020) — [see details](#441-foraging-paralysis-thresholds)
- **Defensive behavior effectiveness** (*Apis mellifera*):
  - Natural conditions (outside hive): **9.5%** of _Vespa velutina_ killed by balling (Arca et al. 2014)
  - Experimental conditions (inside hive): **76.4%** killed (Arca et al. 2014)
  - Note: _Vespa velutina_ do not naturally enter hives; this was experimental — [see details](#442-activity-reductions)
- **Consequence**: Foraging paralysis leads to colony starvation and winter mortality (Requier et al. 2019) — [see details](#44-apis-mellifera-behavior)

### Economic Impact of _Vespa velutina_ on _Apis mellifera_
- **Data source**: InvaCost database — [see details](#453-invacost-database)
- The InvaCost database provides a comprehensive global repository of economic costs of invasive alien species, including *Vespa velutina*. Data can be accessed via the website, GitHub repository, or R package for analysis.

### Quick Reference: Key Thresholds and Observations

| Metric | Threshold/Observation | Study | Context |
|--------|----------------------|-------|---------|
| Minimum risk | ≥5 _Vespa velutina_ at apiary | Diéguez-Antón et al. 2025 | Colony survival risk |
| High risk | ≥10 _Vespa velutina_ at apiary | Diéguez-Antón et al. 2025 | Colony survival risk |
| Foraging decline | >10 _Vespa velutina_ per hive | Monceau et al. 2018 | Bee behavior |
| Foraging paralysis | ≥12.6 _Vespa velutina_ | Requier et al. 2019 | Complete foraging stop |
| Peak predation period | July-October | Multiple | Seasonal pattern |
| Peak daily activity | 13:00-15:00 h | Multiple | Time of day |
| Optimal temperature | 15-26°C | Diéguez-Antón et al. 2022, 2025 | _Vespa velutina_ activity |
| Colony survival (unprotected) | 35-56% | Requier et al. 2020; Rojas-Nossa et al. 2022 | High pressure conditions |
| Colony survival (protected) | 55-78% | Requier et al. 2020; Rojas-Nossa et al. 2022 | With protection measures |

## Table of Contents
- [Summary](#summary)
  - [Predation Pressure on _Apis mellifera_](#predation-pressure-on-apis-mellifera)
  - [Domesticated Honeybee Colony Survival](#domesticated-honeybee-colony-survival)
  - [Behavioral Changes of _Apis mellifera_](#behavioral-changes-of-apis-mellifera)
  - [Economic Impact of _Vespa velutina_ on _Apis mellifera_](#economic-impact-of-vespa-velutina-on-apis-mellifera)
- [1. Literature searches](#1-literature-searches)
  - [1.1 Keywords](#11-keywords)
  - [1.2. Database searches](#12-database-searches)
  - [1.3 Citation chaser](#13-citation-chaser)
  - [1.4 Deduplication](#14-deduplication)
- [2. Phase I screening](#2-phase-i-screening)
  - [2.1. ASReview LAB screening](#21-asreview-lab-screening)
  - [2.2 Download PDFs](#22-download-pdfs)
- [3 Phase II screening](#3-phase-ii-screening)
  - [3.1 Full-text screening](#31-full-text-screening)
  - [3.2 Code template preparation](#32-code-template-preparation)
- [4 Data Extraction](#4-data-extraction)
  - [4.1 Data Extraction](#41-data-extraction)
  - [4.2 Predation Data](#42-predation-data)
    - [4.2.1 Predation Rates and Success](#421-predation-rates-and-success)
    - [4.2.2 Prey Composition](#422-prey-composition)
  - [4.3 Colony Survival and Loss](#43-colony-survival-and-loss)
    - [4.3.1 Colony Survival](#431-colony-survival)
    - [4.3.2 Mortality Factors](#432-mortality-factors)
  - [4.4 Apis mellifera behavior](#44-apis-mellifera-behavior)
    - [4.4.1 Foraging Paralysis Thresholds](#441-foraging-paralysis-thresholds)
    - [4.4.2 Activity Reductions](#442-activity-reductions)
  - [4.5 Economic Impact](#45-economic-impact)
    - [4.5.1 Colony Loss Costs](#451-colony-loss-costs)
    - [4.5.2 Other Countries](#452-other-countries)
    - [4.5.3 Invacost Database](#453-invacost-database)
  - [4.6 Background data](#46-background-data)
    - [4.6.1 Study Locations](#461-study-locations)
    - [4.6.2 Apiaries and Colonies](#462-apiaries-and-colonies)
    - [4.6.3 _Vespa velutina_ Nests Studied](#463-vespa-velutina-nests-studied)
  - [4.7 Notes and biases](#47-notes-and-biases)
    - [4.7.1 Methodological Heterogeneity](#471-methodological-heterogeneity)
- [5 [EXPERIMENTAL] Planning and Prioritization](#5-experimental-planning-and-prioritization)
  - [5.1 Removal Priority Index (RPI)](#51-removal-priority-index-rpi)
  - [5.2 Monthly Outputs](#52-monthly-outputs)
- [Notes](#notes)
  - [Quick Reference: Key Thresholds and Observations](#quick-reference-key-thresholds-and-observations)
  - [Limitations](#limitations)
  
## Project Overview

Nearly a quarter century has passed since _Vespa velutina_ arrived by accident in Europe. And this Asian hornet (_Vespa velutina_) with its yellow legs is using her wings to spread over a large part of Europe. Adult workers need protein-rich prey to feed the developing larvae in their nests, which they obtain primarily from insects. They don't make it difficult for themselves—in Europe domesticated bees (_Apis mellifera_) are widely available and easy to catch. So, let's find out what is published about the potential impact of the yellow-legged hornet (_Vespa velutina_) on Western honeybee (_Apis mellifera_) populations.

**Population:** _Apis mellifera_ colonies in Europe

**Comparison:** Colonies without _Vespa velutina_ predation/presence

**Outcome:** Impact measures including:
- _Apis mellifera_ Predation rates
- _Apis mellifera_ Colony loss
- _Apis mellifera_ behavior changes
- Economic impact of _Vespa velutina_ on _Apis mellifera_

**Limitations**
- Studies on the impact of _Vespa velutina_ on _Apis mellifera_ aren't perfect flowers
  - High methodological heterogeneity
  - Inconsistent outcome measures
  - Lack of explicit control groups
  - This overview is limited to free online literature databases and available PDFs.

## 1. Literature searches
**Updated:** 2025-10-30

### 1.1 Keywords
- **Vespa velutina:** ("vespa velutina" OR "asian hornet" OR "yellow-legged hornet")
- AND
- **Apis mellifera:**  ("apis mellifera" OR honeybee* OR "honey bee*" OR beekeep* OR apiary* OR "managed pollinator*" OR "bee colony" OR "bee colonies")
- AND
(Europe OR European OR 
Austria OR Austrian OR 
Belgium OR Belgian OR 
Bulgaria OR Bulgarian OR 
Croatia OR Croatian OR 
Cyprus OR Cypriot OR 
Czech OR "Czech Republic" OR "Czechia" OR 
Denmark OR Danish OR 
Estonia OR Estonian OR 
Finland OR Finnish OR 
France OR French OR 
Germany OR German OR 
Greece OR Greek OR 
Hungary OR Hungarian OR 
Ireland OR Irish OR 
Italy OR Italian OR 
Latvia OR Latvian OR 
Lithuania OR Lithuanian OR 
Luxembourg OR Luxembourgish OR 
Malta OR Maltese OR 
Netherlands OR Dutch OR 
Poland OR Polish OR 
Portugal OR Portuguese OR 
Romania OR Romanian OR 
Slovakia OR Slovak OR 
Slovenia OR Slovenian OR 
Spain OR Spanish OR 
Sweden OR Swedish OR 
"United Kingdom" OR Britain OR British OR England OR Scotland OR Wales OR "Northern Ireland")

### 1.2. Database searches

Only open access databases were used.

[Lens.org](https://www.lens.org/lens/search/scholar/list?q=(%22vespa%20velutina%22%20OR%20%22asian%20hornet%22%20OR%20%22yellow-legged%20hornet%22)%20AND%20(%22apis%20mellifera%22%20OR%20honeybee*%20OR%20%22honey%20bee*%22%20OR%20beekeep*%20OR%20apiary*%20OR%20%22managed%20pollinator*%22%20OR%20%22bee%20colony%22%20OR%20%22bee%20colonies%22)%20AND%20(Europe%20OR%20European%20OR%20%20Austria%20OR%20Austrian%20OR%20%20Belgium%20OR%20Belgian%20OR%20%20Bulgaria%20OR%20Bulgarian%20OR%20%20Croatia%20OR%20Croatian%20OR%20%20Cyprus%20OR%20Cypriot%20OR%20%20Czech%20OR%20%22Czech%20Republic%22%20OR%20%22Czechia%22%20OR%20%20Denmark%20OR%20Danish%20OR%20%20Estonia%20OR%20Estonian%20OR%20%20Finland%20OR%20Finnish%20OR%20%20France%20OR%20French%20OR%20%20Germany%20OR%20German%20OR%20%20Greece%20OR%20Greek%20OR%20%20Hungary%20OR%20Hungarian%20OR%20%20Ireland%20OR%20Irish%20OR%20%20Italy%20OR%20Italian%20OR%20%20Latvia%20OR%20Latvian%20OR%20%20Lithuania%20OR%20Lithuanian%20OR%20%20Luxembourg%20OR%20Luxembourgish%20OR%20%20Malta%20OR%20Maltese%20OR%20%20Netherlands%20OR%20Dutch%20OR%20%20Poland%20OR%20Polish%20OR%20%20Portugal%20OR%20Portuguese%20OR%20%20Romania%20OR%20Romanian%20OR%20%20Slovakia%20OR%20Slovak%20OR%20%20Slovenia%20OR%20Slovenian%20OR%20%20Spain%20OR%20Spanish%20OR%20%20Sweden%20OR%20Swedish%20OR%20%20%22United%20Kingdom%22%20OR%20Britain%20OR%20British%20OR%20England%20OR%20Scotland%20OR%20Wales%20OR%20%22Northern%20Ireland%22))
- Last accessed: 2025-10-30 
    - 767 records

[Open Alex](https://openalex.org/works?page=1&sort=publication_year:desc&filter=title_and_abstract.search:(%22vespa+velutina%22+OR+%22asian+hornet%22+OR+%22yellow-legged+hornet%22)+AND+(%22apis+mellifera%22+OR+%22honey+bee%22+OR+%22beekeeping%22+OR+%22apiary%22+OR+%22managed+pollinator%22+OR+%22bee+colony%22)+AND+(Europe+OR+European+OR+Austria+OR+Belgium+OR+Bulgaria+OR+Croatia+OR+Cyprus+OR+Czech+OR+%22Czech+Republic%22+OR+Czechia+OR+Denmark+OR+Estonia+OR+Finland+OR+France+OR+Germany+OR+Greece+OR+Hungary+OR+Ireland+OR+Italy+OR+Latvia+OR+Lithuania+OR+Luxembourg+OR+Malta+OR+Netherlands+OR+Poland+OR+Portugal+OR+Romania+OR+Slovakia+OR+Slovenia+OR+Spain+OR+Sweden+OR+%22United+Kingdom%22),type:types/article)
- Last accessed: 2025-10-30
    - 67 articles
    - 5 preprints


[Pubmed](https://pubmed.ncbi.nlm.nih.gov/?term=%28+%22vespa+velutina%22%5Btiab%5D+OR+%22asian+hornet%22%5Btiab%5D+OR+%22yellow-legged+hornet%22%5Btiab%5D+%29+AND+%28+%22apis+mellifera%22%5Btiab%5D+OR+honeybee*%5Btiab%5D+OR+beekeep*%5Btiab%5D+OR+apiary*%5Btiab%5D+%29+AND+%28Europe+OR+European+OR+Austria+OR+Belgium+OR+Bulgaria+OR+Croatia+OR+Cyprus+OR+Czech+OR+%22Czech+Republic%22+OR+Czechia+OR+Denmark+OR+Estonia+OR+Finland+OR+France+OR+Germany+OR+Greece+OR+Hungary+OR+Ireland+OR+Italy+OR+Latvia+OR+Lithuania+OR+Luxembourg+OR+Malta+OR+Netherlands+OR+Poland+OR+Portugal+OR+Romania+OR+Slovakia+OR+Slovenia+OR+Spain+OR+Sweden+OR+%22United+Kingdom%22%29&sort=date)
- Last accessed: 2025-10-30
    - 56 articles

**Google Scholar** is used to screen for additional articles or relevant gray literature after the initial literature search.
- Last accessed: 2025-10-30
    - 2.160 records ([sorted for relevance](https://scholar.google.com/scholar?hl=nl&as_sdt=0,5&as_vis=1&q=(%22vespa+velutina%22+OR+%22asian+hornet%22+OR+%22yellow-legged+hornet%22)+AND+(%22apis+mellifera%22+OR+%22honey+bee%22+OR+beekeeping+OR+apiary+OR+%22managed+pollinator%22+OR+%22bee+colony%22)+AND+(Europe+OR+European+OR+Austria+OR+Belgium+OR+Bulgaria+OR+Croatia+OR+Cyprus+OR+Czech+OR+%22Czech+Republic%22+OR+Czechia+OR+Denmark+OR+Estonia+OR+Finland+OR+France+OR+Germany+OR+Greece+OR+Hungary+OR+Ireland+OR+Italy+OR+Latvia+OR+Lithuania+OR+Luxembourg+OR+Malta+OR+Netherlands+OR+Poland+OR+Portugal+OR+Romania+OR+Slovakia+OR+Slovenia+OR+Spain+OR+Sweden+OR+%22United+Kingdom%22)&scisbd=1))
    - 168 records ([sorted for date](https://scholar.google.com/scholar?scisbd=2&q=(%22vespa+velutina%22+OR+%22asian+hornet%22+OR+%22yellow-legged+hornet%22)+AND+(%22apis+mellifera%22+OR+%22honey+bee%22+OR+beekeeping+OR+apiary+OR+%22managed+pollinator%22+OR+%22bee+colony%22)+AND+(Europe+OR+European+OR+Austria+OR+Belgium+OR+Bulgaria+OR+Croatia+OR+Cyprus+OR+Czech+OR+%22Czech+Republic%22+OR+Czechia+OR+Denmark+OR+Estonia+OR+Finland+OR+France+OR+Germany+OR+Greece+OR+Hungary+OR+Ireland+OR+Italy+OR+Latvia+OR+Lithuania+OR+Luxembourg+OR+Malta+OR+Netherlands+OR+Poland+OR+Portugal+OR+Romania+OR+Slovakia+OR+Slovenia+OR+Spain+OR+Sweden+OR+%22United+Kingdom%22)&hl=nl&as_sdt=0,5&as_vis=1)) 

### 1.3 Citation chaser
[Citation chaser](https://estech.shinyapps.io/citationchaser/)
- Initial search 2025-10-30: 56 references

### 1.4 Deduplication
[Rayyan](https://new.rayyan.ai/)
- Imported references: 915
- Duplications detected: 347
- Unique references for phase I screening: 612

## 2. Phase I screening
### 2.1. ASReview LAB screening
[ASReview LAB](https://github.com/asreview/asreview) screening based on title and abstract
#### Inclusion Criteria
- Language is English, Dutch, or German
- Contains predation data and/or secondary effect data
- Study type is observational or experimental with field component

#### Exclusion Criteria
- No Apis mellifera data
- No Vespa velutina data
- Non-European location
- Not English, Dutch, or German language
- Simulation studies, models, prediction, laboratory conditions
- Reviews (check for missed articles with citation chaser)
- Gray literature
- Only nest removal methods (no impact data)
- Duplicate (data) of already included study

### 2.2 Download PDFs
- Free online: 32
- Free pre-print: 1
- PDF requested 2025-11-01: 1
- `pdf_phaseI.csv` contains the list with the included articles for phase II screening

## 3 Phase II screening
### 3.1 Full-text screening
Screening based on full text and supplemental material (if available). `_update_phase_II.md` is used to instruct Cursor.AI to extract the quantitative items from the PDFs. First inclusion and exclusion criteria are extracted, subsequent additional quantifiable data are extracted. Short notes were allowed. The results are saved in a .md file with a similar name as the PDF. Then they were manually checked, corrected, and additional relevant information was added.
#### Included: 28
- Apis_mellifera_predation
- Other_species_predation
- Colony_loss
- Foraging_activity
- Other_behavior_changes
- Honey_yield
- Economic_loss
- Management_costs
#### Excluded: 5
- Editorial: 1
- Review_ or _meta-analysis: 3
- No_quantifiable-data: 0
- Gray_literature: 0
- PDF_not_available: 1
- No original data (article based on invacost): 1
### 3.2 Code template preparation
`_pdf_phase_II.csv` contains the master dataset with all included articles for phase II screening and data extraction. This CSV file serves as the primary data source for all quantitative analyses.

## 4 Data Extraction

**Quantitative data** extracted from 34 studies (30 included, 4 excluded) on the impact of *Vespa velutina* on *Apis mellifera* in Europe.

**Master Dataset**: `3_phase_II/_pdf_phase_II.csv` contains all extracted quantitative data, study characteristics, inclusion/exclusion criteria, and outcome measures.

### 4.1 Data Extraction
Draft data extraction of the quantitative data for each PDF is done with Cursor.ai and checked manually.
### 4.2 Predation Data

#### 4.2.1 Predation Rates and Success

**Key Metrics Summary**

| Metric | Value | Study | Location |
|--------|-------|-------|----------|
| Overall predation success rate | 2.4% | Poidatz et al. 2023 | France |
| Success rate (bees entering hive) | 69.46% | Poidatz et al. 2023 | France |
| Success rate (bees leaving hive) | 15.27% | Poidatz et al. 2023 | France |
| Peak success (_Vespa velutina_ number) | ~8 _Vespa velutina_ | Poidatz et al. 2023 | France |
| Attack success rate | 25% | Perrard et al. 2009 | France |
| Maximum captures (_Vespa velutina_ number) | 9 _Vespa velutina_ | Monceau et al. 2013 | France |

**Detailed Findings**

**Poidatz et al. 2023** (France)
- Overall predation success: **2.4%** (126 successful events out of 5,175 interactions)
- Success rate for bees entering hive: **69.46%** (4× higher than bees leaving)
- Success rate for bees leaving hive: **15.27%**
- Peak success occurs at **~8 _Vespa velutina_**, then decreases
- Sample: 5,175 predator-prey interactions from 603,259 trajectories

**Perrard et al. 2009** (France, 2007)
- Attack success rate: **25%** (average 4 trials necessary to catch one honeybee)
- Honeybee predation rate (captive colony): **37.5 honeybees/day** (range: 25-50)
- Sample: 359 attacks observed, 1 captive colony

**Monceau et al. 2013** (France, 2008-2009)
- Maximum captures at **9 _Vespa velutina_ per hive**
- Peak capture time: **13:00-14:00 h** (midday)
- _Vespa velutina_ trapped:
  - ART site: **916 individuals** (14 hives), peak: 106 on 12 Nov 2008
  - VIL site: **1,894 individuals** (9 hives), peak: 217 on 12 Nov 2008
- Predation duration: **5 months**
- Delay to predation increase: **~44 days** from first capture
- Sample: 23 hives across 2 sites

**Monceau et al. 2014** (France, 2011)
- _Vespa velutina_ visiting daily: **~350 individuals** (6 hives)
- Maximum _Vespa velutina_ at single hive: **20 individuals** simultaneously
- Recapture rate: **56.67%** overall (204/360 marked), **73.94%** on D1 morning
- Daily visits per half-day: **1.88 visits** (range: 1.70-2.20)
- Sample: 360 marked _Vespa velutina_, 6 hives

**Rome et al. 2021** (France, 2008-2010)
- Peak predation timing: **Early October**
- Peak predation time of day: **Midday**
- Sample: 16 nests

**Diéguez-Antón et al. 2025** (Spain, 2021-2022)
- Total _Vespa velutina_ counted: **11,406 individuals** across all apiaries (6 colonies)
- Predation pressure duration: Up to **11 months** (Apiary 3, both years)
- Sample: 3 apiaries, 6 colonies

#### 4.2.2 Prey Composition

**Key Metrics Summary**

| Metric | Value Range | Method | Studies |
|--------|-------------|--------|---------|
| Apis mellifera in diet | 22.55% - 98.1% | Various | Multiple |
| Apis mellifera found in all nests | 100% | Metabarcoding | Pedersen et al. 2025 |
| Prey consumption per _Vespa velutina_ colony | 97,246 honeybee-equivalent/season | Pellet analysis | Rome et al. 2021 |
| Biomass consumption per _Vespa velutina_ colony | 11.32 kg/season | Pellet analysis | Rome et al. 2021 |
| Proportion hive production consumed | 40% | Pellet analysis | Rome et al. 2021 |

**Detailed Findings**

**Rome et al. 2021** (France, 2008-2010, 16 nests, pellet collection)
- Apis mellifera in prey pellets: **38.1%** (820/2,151 pellets)
- Prey consumption per _Vespa velutina_ colony: **97,246 honeybee-equivalent** per season
- Biomass consumption per _Vespa velutina_ colony: **11.32 kg** of insects per season
- Proportion of hive production consumed: **~40%** (one _Vespa velutina_ colony consumes ~40% of individuals produced by one hive)
- Wild bees proportion: **0.02%** (bumblebees and solitary bees, excluding wild honeybee colonies)

**Pedersen et al. 2025** (Multiple countries, 2020-2022, 103 nests, larval gut contents)
- Apis mellifera prevalence: **98.1%** average (found in every nest)
- Apis mellifera found in all nests: **100%**
- Top 50 prey species: **43 were potential pollinators**
- Crop pollinators: **3 most dominant European crop pollinators** identified

**Perrard et al. 2009** (France, 2007, pellet analysis)
- Apis mellifera in pellets: **84.8%** (145/171 flesh pellets)

**Herrera et al. 2025** (Spain, Mallorca, 2016, 7 nests, meconium analysis)
- Apis mellifera in diet: **22.55%** of Apidae family
- Range across nests: **14.86-29.27%**
- Shared OTU: Yes (found across all nests)

**Verdasca et al. 2022** (Portugal, 2018, 12 nests, metabarcoding)
- Honeybee reads:
  - Total: **75%** (79,143/108,979 reads)
  - Faecal pellets: **84%** (50,549/60,518 reads)
  - Jaws: **74%** (20,458/27,546 reads)
  - Stomachs: **39%** (8,136/20,915 reads)
- Detection rates:
  - Faecal pellets: **100%** (all replicates)
  - Jaws: **70%**
  - Stomachs: **40%**
- DNA persistence in faecal pellets: **≥28 days** (maximum known period)

**Stainton et al. 2023** (UK, 2016-2020, 5 nests, larval gut contents)
- Honeybee detection rate: **65.8%** (25/38 larvae)
- Detection by nest: **80%** (4/5 nests)
- Honeybee reads by location:
  - Jersey (2019): **20.5%** (9 samples)
  - Tetbury (2016): **0.33%** (10 samples)
  - Woolacombe (2017): **7.3%** (10 samples)

### 4.3 Colony Survival and Loss

#### 4.3.1 Colony Survival

**Key Metrics Summary**

| Metric | Value | Study | Location |
|--------|-------|-------|----------|
| Protected colony survival | 77.8% | Rojas-Nossa et al. 2022 | Spain |
| Muzzle-equipped survival | 55% | Requier et al. 2020 | France |
| Unprotected colony survival | 55.6% | Rojas-Nossa et al. 2022 | Spain |
| Control survival (no protection) | 35% | Requier et al. 2020 | France |
| Colony collapse rate | 55.3% | Requier et al. 2019 | France |

**Detailed Findings**

**Requier et al. 2020** (France, 2013-2016, BEEHAVE model simulations)
- Muzzle-equipped survival: **55%** (100 simulations)
- Control survival: **35%** (100 simulations)
- Survival increase with protection: **Up to 51%** in context of high _Vespa velutina_ abundance (>5 _Vespa velutina_)
- Low _Vespa velutina_ loads (<5): Muzzle survival marginally lower than control
- High _Vespa velutina_ loads (>5): Muzzle significantly increases survival probability

**Rojas-Nossa et al. 2022** (Spain, 2018-2020, electric harp protection)
- Protected colony survival: **77.8%**
- Unprotected colony survival: **55.6%**
- Honeybee weight reduction (unprotected): **6.7%** lighter workers

**Requier et al. 2019** (France, 2012-2016, BEEHAVE model simulations, 993 simulations)
- Colony collapse rate: **55.3%** (549/993 reached endpoint)
- Collapse during predation period: **2.5%** (24 colonies)
- Collapse during winter: January 13 - May 1

**Field Observations**
- **Diéguez-Antón et al. 2022** (Spain, 2020-2021): 1 colony died out of 2 monitored
- **Monceau et al. 2018** (France, 2009): Both monitored colonies died (H1 before winter, H2 later in winter)

#### 4.3.2 Mortality Factors

**Risk Thresholds**

| Threshold | Risk Level | Study | Location |
|----------|------------|-------|----------|
| ≥5 _Vespa velutina_ | Minimum risk | Diéguez-Antón et al. 2025 | Spain |
| ≥10 _Vespa velutina_ | High risk | Diéguez-Antón et al. 2025 | Spain |

**Winter Mortality Profiles** (Requier et al. 2019, France, 2012-2016, BEEHAVE simulations)

- **Profile A** (n=27): **100% mortality**
  - Larvae population <5 individuals
  - Changes: Larvae decreased, adult population increased (+4,874), honey reserves decreased (-26.8 kg)

- **Profile B** (n=288): **80.5-96.8% mortality**
  - Larvae >5, adult population <9,950
  - Changes: Larvae decreased, adult population decreased (-19,732), honey reserves increased (+12.3 kg)

- **Profile C** (n=66): **100% mortality**
  - Larvae >5, adult >9,950, honey reserve ≤21 kg
  - Changes: Intermediary population and reserve trajectories

**Pan-European Mortality** (Jacques et al. 2017, EPILOBEE, 17 countries, 2012-2014)

**Year 1** (2,332 apiaries):
- Winter mortality range: **5.01%** (Italy) to **31.73%** (Belgium)
- Seasonal mortality range: **0.09%** (Lithuania) to **9.63%** (France)

**Year 2** (2,426 apiaries):
- Winter mortality range: **2.16%** (Lithuania) to **13.85%** (Belgium)
- Seasonal mortality range: **0.16%** (Lithuania) to **8.06%** (France)

**Beekeeper Type Comparison**:
- Hobby beekeepers: **14.04%** winter mortality
- Professional beekeepers: **8.11%** winter mortality
- Hobby beekeepers had **double** the winter mortality

**High Pressure Events** (Diéguez-Antón et al. 2025, Spain, 2021-2022)
- Apiary 1 (October 2021): **31 events** with >5 _Vespa velutina_, **5 days** with >10 _Vespa velutina_
- Apiary 2 (August 2021): **20 days** with ≥5 _Vespa velutina_, up to **37 times** per day

### 4.4 Apis mellifera Behavior

#### 4.4.1 Foraging Paralysis Thresholds

**Key Thresholds Summary**

| Threshold | Value | Study | Location |
|-----------|-------|-------|----------|
| Complete foraging paralysis | ≥12.6 _Vespa velutina_ | Requier et al. 2019 | France |
| Foraging decline | >10 _Vespa velutina_ | Monceau et al. 2018 | France |
| Foraging paralysis (HRH) | >0.8 _Vespa velutina_/hive/10min | Rojas-Nossa et al. 2022 | Spain |

**Detailed Findings**

**Requier et al. 2019** (France, 2012-2016, 131 colonies, 603 observations)
- Foraging paralysis threshold: **≥12.6 _Vespa velutina_** (95% CI) for complete FP
- Statistical effect: Z=-20.65, P<0.001 (negative impact on flight activity)
- Peak period: August 28 - November 6 (_Vespa velutina_ >5 only during this period)

**Requier et al. 2020** (France, 2013-2016, 44 colonies, muzzle protection study)
- Foraging paralysis reduction with muzzle: **Up to 41%**
- Activity levels:
  - Muzzle (0 _Vespa velutina_): **84%** of baseline
  - Muzzle (20 _Vespa velutina_): **76%** of baseline (16-24% FP)
  - Control (0 _Vespa velutina_): **100%** of baseline
  - Control (20 _Vespa velutina_): **35%** of baseline (0-65% FP)
- Control max FP: **Up to 76%** (95% CI prediction)

**Monceau et al. 2018** (France, 2009, 2 hives)
- Foraging decline threshold: **>10 _Vespa velutina_** per hive (number of foragers drops above this)

**Rojas-Nossa et al. 2022** (Spain, 2018-2020)
- Foraging paralysis threshold: **>0.8 _Vespa velutina_/hive/10min** (HRH)

**Diéguez-Antón et al. 2025** (Spain, 2021-2022, 6 colonies)
- Foraging paralysis observed: Yes (when _Vespa velutina_ pressure is high)

#### 4.4.2 Activity Reductions and Behavioral Responses

**Defensive Behaviors**

**Arca et al. 2014** (France, 2008-2010, 95 colonies, simulated attacks)
- **Colony activity**: Dramatic drop when _Vespa velutina_ present
- **Bee-carpet formation**:
  - 30-60% increase: 14 colonies
  - 60-80% increase: 17 colonies
  - > 80% increase: 48 colonies
  - Patterns: 42% large gathering, 20% coordinated behavior, 38% no coordination
  - **Balling behavior** (*Apis mellifera*):
    - Occurrence: 68 colonies (72%) exhibited balling
    - Ball size distribution:
      - <10 bees: 31 colonies (33%)
      - 10-20 bees: 20 colonies (21%)
      - 20-30 bees: 15 colonies (16%)
      - > 30 bees: 1 colony (1%)
    - Effectiveness:
      - Outside hive (natural conditions): **9.5%** _Vespa velutina_ killed by balling in 5 min
      - Inside hive (experimental conditions): **76.4%** _Vespa velutina_ killed (42/55) — Note: _Vespa velutina_ do not naturally enter hives; this was experimental
- **_Vespa velutina_ hovering distance**: ~15 cm from hive entrance

**Monceau et al. 2018** (France, 2009, 2 hives)
- **Bee-carpet maximum**: Late August-early September at **7 _Vespa velutina_**
- **Honeybees tracking _Vespa velutina_**: H1: 21 instances, H2: 46 instances
- **Balling occurrences**: H1: 2 occurrences, H2: 1 occurrence

**Flight Performance Changes**

**Poidatz et al. 2023** (France, 603,259 trajectories)
- **Flight speed**:
  - Bees leaving vs entering: **1.9× faster** (bees leaving)
  - Bees vs _Vespa velutina_: **1.25× faster** (bees entering)
- **Hovering time**: _Vespa velutina_ **2.1× more** hovering time than bees
- **Response to _Vespa velutina_ density**:
  - Bees entering: Speed and curvature **increase** with _Vespa velutina_ density
  - Bees leaving: Speed **decreases** with _Vespa velutina_ density

**Activity Patterns**

**Temporal Patterns**

| Study | Peak Activity Time | Peak Season | Location |
|-------|-------------------|-------------|----------|
| Poidatz et al. 2023 | _Vespa velutina_: 13:00 h, Bee: 15:00 h | - | France |
| Monceau et al. 2017 | Nest A: 14:00 h, Nest B: 13:00 h | October | France |
| Requier et al. 2019 | 9:06-18:08 h (daily period) | September-October | France |
| Perrard et al. 2009 | 15:30-16:30 h | - | France |
| Diéguez-Antón et al. 2022 | 7:00-21:00 h (daily period) | Sept (2020), Oct (2021) | Spain |

**Monceau et al. 2013** (France, 2009, 2 hives)
- **Flying activity pattern**: Higher early morning, decreased afternoon/evening
- **Seasonal pattern**: Higher in July, decreased throughout summer until October
- **Activity relation to _Vespa velutina_**: Negative (negatively related to number of _Vespa velutina_)
- **Returning foragers vs guards**: P=0.01 (flying honeybees returning suffered more predation)
- **Forager load**: Up to **40%** extra body mass (pollen or nectar loads)

**Environmental Correlations**

**Diéguez-Antón et al. 2022** (Spain, 2020-2021, 2 colonies)
- **Optimal temperature**: **15-25°C** for _Vespa velutina_ activity
- **Optimal humidity**: **>60%** for _Vespa velutina_ activity
- **Temperature correlation**: r=0.368, p<0.01 (positive)
- **Humidity correlation**: r=-0.347, p<0.01 (inverse)

**Diéguez-Antón et al. 2025** (Spain, 2021-2022, 6 colonies)
- **Optimal temperature range**: **17-26°C** (most suitable for observing higher number of _Vespa velutina_)

**Perrard et al. 2009** (France, 2007, 1 captive colony)
- **Activity start**: 6:00 h (workers' flights)
- **Activity end**: 22:00-22:30 h (dusk)
- **Peak activity**: 15:30-16:30 h (3:30-4:30 pm)
- **Minimum activity temperature**: **10°C** (no activity below this)

**Homing Failure**

**Requier et al. 2019** (France, 2012-2016, 603 observations)
- **Homing failure effect**: Z=-5.37, P<0.001 (significantly dependent on flight activity)
- Pattern: Maximal under very low flight activity, decreases with increased flight activity

### 4.5 Economic Impact

#### 4.5.1 Colony Loss Costs

**France (Requier et al. 2023)**

**Note**: This analysis was originally based on a preprint version (published 2023, Science of the Total Environment). The study is France-specific and uses spatial modeling combining field data, niche modeling, and BEEHAVE agent-based simulations. No comparable quantitative economic impact studies are available for other European countries.

**National Economic Costs (Yearly)**

| Scenario | Colonies Lost | Percentage of Livestock | Economic Cost (€) | Impact vs Honey Revenues |
|----------|---------------|------------------------|-------------------|--------------------------|
| Low predation (1 _Vespa velutina_/nest) | 27,821 | 2.6% | €2.8 million | 2.4% |
| High predation (20 _Vespa velutina_/nest) | 308,379 | 29.2% | €30.8 million | 26.6% |

**Key Metrics**:
- **Colony replacement cost**: €100 per colony (Requier et al. 2020a)
- **National honey production (2015)**: 14,490 tons
- **National honey revenue (2015)**: €116 million (at €8/kg)
- **Colonies at risk**: 98.2% (1,017,713 out of 1,056,314 colonies)
- **Average loss per township (low scenario)**: 10.2% (sd = 15.3%)
- **Average loss per township (high scenario)**: 48.3% (sd = 25.7%)

**Regional Economic Costs (High Predation Scenario)**:
- **Average regional cost**: €1.3 million per year
- **Range**: €0.4 million (Corse) to €5.5 million (Occitanie)
- **Regional economic impact**: Average 21.9% of honey revenues
- **Regional impact range**: 13.2% (Bourgogne-Franche-Comté) to 96.5% (Normandie)

**Comparison with Control Costs**:
- **Control cost (France, yearly)**: €11.9 million (Barbet-Massin et al. 2020)
- **Damage cost vs control cost**: Up to 3× higher (€30.8M vs €11.9M)

**Methodological Notes**:
- Based on spatial modeling combining field data (1,260 nests over 28,348 km²), niche modeling, and BEEHAVE agent-based simulations
- Low scenario likely underestimated (1 _Vespa velutina_/nest < observed mean of 2.3)
- High scenario based on maximum observed values (realistic but extreme)
- Real economic cost likely between low and high scenarios

#### 4.5.2 Other Countries

**Spain** (Angulo et al. 2021):
- Total economic costs of invasive alien species: €232 million (1997-2022)
- Cost increase: €4 million/year before 2000 → €15 million/year in recent years
- **Limitation**: Costs aggregated across 174 invasive species; *Vespa velutina*-specific costs not separately reported
- Study excluded from main analysis (no original *Vespa velutina* data)

**Portugal and Belgium**: No quantitative economic impact studies available. Studies from these countries focus on predation behavior and colony monitoring rather than economic costs.

**Control Cost Projections** (Barbet-Massin et al. 2020):
- Potential control costs if species fills climatically suitable distribution:
  - Italy: €9.0M/year
  - United Kingdom: €8.6M/year
- **Note**: These are control cost projections, not damage cost estimates

#### 4.5.3 Invacost Database

The InvaCost database is a comprehensive global repository documenting economic costs of invasive alien species worldwide, including *Vespa velutina*. The database provides standardized cost data that can be used for comparative analyses and policy assessments.

**Access and Data Format:**
- **Website**: https://invacost.fr/
- **GitHub Repository**: https://github.com/Farewe/invacost
- **Data Format**: CSV/Excel files, R package (`invacost`)
- **Citation**: Diagne et al. (2020). High and rising economic costs of biological invasions worldwide. *Nature*, 592, 571-576. https://doi.org/10.1038/s41586-021-03405-6

**Database Contents:**
- Global coverage of invasive species economic costs
- Standardized cost categories (damage, management, prevention)
- Temporal data (costs over time)
- Geographic data (costs by country/region)
- Cost type classification (observed vs. potential, robust vs. extrapolated)

**Use for *Vespa velutina* Research:**
- Filter database for *Vespa velutina*-specific cost entries
- Compare costs across different countries and time periods
- Analyze cost trends and patterns
- Extract data for economic impact assessments

**Note**: The database aggregates cost data from multiple sources. Users should verify data quality and methodology for specific entries. Some entries may represent aggregated costs (e.g., all invasive species in a region) rather than species-specific costs.

### 4.6 Background data
![Study timeline](https://raw.githubusercontent.com/vespCV/VespaVelutina-Impact/main/images/study_timeline.jpg)
#### 4.6.1 Study Locations
| Country | Number of Studies | Key Findings |
|---------|-------------------|--------------|
| France | 17 | Highest number of studies, longest invasion history |
| Spain | 5 | Multiple regions (Galicia, Catalonia, Mallorca) |
| Portugal | 1 | Metabarcoding studies on prey composition |
| United Kingdom | 2 | Early detection and eradication efforts |
| Europe (pan-European) | 1 | EPILOBEE study across 17 countries |
| Multiple countries | 1 | Pedersen et al. 2025 (Jersey, France, Spain, UK) |
![Study locatons](https://raw.githubusercontent.com/vespCV/VespaVelutina-Impact/main/images/study_locations.jpg)
### 4.6.2 Apiaries and Colonies

| Study | Apiaries | Colonies | Nests | _Vespa velutina_ | Notes |
|-------|----------|----------|-------|---------|-------|
| Arca et al. 2014 | 8 | 95 | Not specified | Variable | Defensive behavior study |
| Monceau et al. 2013 | 2 | 23 | Not specified | 2,810 trapped | Predation pressure |
| Requier et al. 2018 | 75 | 131 | Not specified | 0-20 observed | Foraging paralysis |
| Requier et al. 2020 | 22 | 44 | Not specified | 0-20 observed | Muzzle effectiveness |
| Requier et al. 2023 | 51 plots | Variable (4-24 per apiary) | 1,260 | Variable | Economic cost study |
| Diéguez-Antón et al. 2022 | 1 | 2 | Not specified | Variable | Photo monitoring |
| Diéguez-Antón et al. 2025 | 3 | 6 | Not specified | 11,406 total | Long-term pressure |
| Rojas-Nossa et al. 2022 | 3 | Variable | Not specified | 4,359 captured | Electric harps |
| Jacques et al. 2017 | 5,798 | Variable | Not applicable | Not applicable | Pan-European study |

### 4.6.3 _Vespa velutina_ Nests Studied

| Study | Nests | Method | Location |
|-------|-------|--------|----------|
| Rome et al. 2021 | 16 | Pellet collection | France |
| Verdasca et al. 2021 | 12 | Metabarcoding | Portugal |
| Herrera et al. 2025 | 7 | Meconium analysis | Spain (Mallorca) |
| Pedersen et al. 2025 | 103 | Larval gut contents | Multiple countries |
| Stainton et al. 2023 | 5 | Larval gut contents | UK |
| Requier et al. 2023 | 1,260 | Field observations | France (4 districts) |

### 4.7 Notes and biases

#### 4.7.1 Methodological Heterogeneity

- Different observation methods (visual, video, photo, trapping)
- Varying time periods and frequencies
- Different sample sizes and study designs
- Geographic and temporal variation
- Inconsistent statistical reporting
![Observartion methods](https://raw.githubusercontent.com/vespCV/VespaVelutina-Impact/main/images/observation_methods.jpg)

![outcome types](https://raw.githubusercontent.com/vespCV/VespaVelutina-Impact/main/images/outcome_types.jpg)

## Notes

- This synthesis is based on extracted quantitative data from included studies
- Numbers are reported as found in original studies
- Ranges and means are presented where available
- Statistical significance is noted where reported
- Methodological differences between studies should be considered when interpreting results
- This summary is made with a human in the loop, when you see an error please create an issue.

### Limitations
1. **High methodological heterogeneity**: Studies use different observation methods (visual counts, video tracking, trapping, DNA metabarcoding, pellet analysis), making direct comparison of effect sizes problematic.
2. **Inconsistent outcome measures**: Predation rates, survival percentages, and behavioral changes are measured using different metrics, timeframes, and units across studies.
3. **Lack of standardized control groups**: Most studies are observational without explicit control groups, making it difficult to calculate comparable effect sizes.
4. **Geographic and temporal variation**: Studies span different countries, years, and seasons, with varying _Vespa velutina_ population densities and beekeeping practices.
5. **Small sample sizes per study**: Many studies have small sample sizes (2-6 colonies, 1-3 apiaries), limiting statistical power for meta-analysis.
6. **Diverse study designs**: Mix of experimental interventions (muzzles, electric harps), observational studies, and modeling approaches cannot be meaningfully combined in a single meta-analysis.

## 5 [EXPERIMENTAL] Update hornet hotspots 

### 5.1 Removal Priority Index (RPI)

Purpose: prioritize areas for Asian hornet nest removal in the next month using a transparent, reproducible 0–100 score.

Inputs (normalized; see detailed documentation):
- Recent vespa velutina/nests intensity (last 30–90 days), weighting secondary nests higher (waarnemingen.nl; GBIF).
- Apiary/hive density proxy (FAOSTAT national hives scaled subnationally) [to be verified].
- Seasonal factor (peak July–October; 15–26°C optimal) based on published thresholds.
- Cost-of-delay multiplier informed by economic impact/control cost literature.

Formula (summary): RPI = 100 × Σ(weight × normalized_input). Initial weights: sightings 0.40; secondary share 0.20; apiary proxy 0.20; season 0.10; cost-of-delay 0.10. Bands and actions:
- 0–24 Low: Monitor; beekeeper self-protection briefing.
- 25–49 Moderate: Validate; remove if repeated events ≥5 hornets.
- 50–74 High: Schedule removal ≤7 days; alert local beekeepers.
- 75–100 Very High: Immediate removal ≤72 h; surge capacity.

Methodology and variables are specified here: `5_visualisation_reporting/RPI_methodology.md`.

Data sources and URLs: GBIF (`https://www.gbif.org/`), EPPO (`https://gd.eppo.int/`), Vespa‑Watch.nl (`https://vespa-watch.nl/`), FAOSTAT (`https://www.fao.org/faostat/`), InvaCost (`https://invacost.fr/`), EASIN (`https://easin.jrc.ec.europa.eu/`).

Key thresholds referenced: Monceau et al. 2018; Requier et al. 2019, 2020, 2023 [to be verified]; Rojas‑Nossa et al. 2022; Diéguez‑Antón et al. 2025.

Assumptions and limitations:
- Citizen science data are biased; normalization uses percentile scaling and bands are interpreted with caution.
- Apiary proxy may be coarse where subnational data are unavailable [to be verified].
- RPI is decision support, not causal impact.

### 5.2 Monthly Outputs

- Scores (CSV): `4_data_extraction/rpi_scores_202511.csv` (schema documented in `RPI_methodology.md`).
- Choropleth map: `5_visualisation_reporting/rpi_map_202511.jpg` (RPI bands).
- Optional: Top 20 areas table: `5_visualisation_reporting/rpi_top20_202511.csv`.

Each monthly artifact must include download dates, filters, and any preprocessing notes consistent with the Data Management Standards.

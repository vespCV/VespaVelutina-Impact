# Impact of Vespa velutina on Apis mellifera in Europe
_If bees only gathered nectar from perfect flowers, they wouldn’t be able to make even a single drop of honey_ – Matshona Dhliwayo


## Project Status

- **Current Phase:** Data extraction
- **Status:** Work in progress
- **Updated:** 2025-11-08

This repository contains available articles on the impact of *Vespa velutina* (Asian hornet) on honeybees (*Apis mellifera*) in Europe. The aim is to develop an online summary of published data in a monthly updated repository.

Klik [hier]() voor de nederlandse versie.

## Table of Contents
- [Project Overview](#project-overview)
- [Rationale](#rationale)
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
    - [4.5.1 Invacost](#451-invacost)
  - [4.6 Background data](#46-background-data)
    - [4.6.1 Study Locations](#461-study-locations)
    - [4.6.2 Apiaries and Colonies](#462-apiaries-and-colonies)
    - [4.6.3 Hornet Nests Studied](#463-hornet-nests-studied)
  - [4.7 Notes and biases](#47-notes-and-biases)
    - [4.7.1 Study Locations](#471-study-locations)
    - [4.7.2 Methodological Heterogeneity](#472-methodological-heterogeneity)
- [5. Key Quantitative Findings Summary](#5-key-quantitative-findings-summary)
  - [5.1 Predation Pressure](#51-predation-pressure)
  - [5.2 Colony Survival](#52-colony-survival)
  - [5.3 _Apis mellifera_ behavior](#53-apis-mellifera-behavior)
  - [5.3 Economic Impact](#53-economic-impact)
- [Notes](#notes)

## Project Overview

Nearly a quarter century has passed since _Vespa velutina_ arrived by accident in Europe. And this Asian hornet with its yellow legs is using her wings to spread over a large part of Europe. Adult workers need protein-rich prey to feed the developing larvae in their nests, which they obtain primarily from insects. They don't make it difficult for themselves—in Europe domesticated bees (_Apis mellifera_) are widely available and easy to catch. So, let's find out what is published about the contribution of the **yellow-legged hornet** to the decline of Western **honeybee** populations.

**Population:** _Apis mellifera_ colonies in Europe

**Comparison:** Colonies without _Vespa velutina_ predation/presence

**Outcome:** Impact measures including:
- Predation rates
- Colony loss
- _Apis mellifera_ behavior changes
- Economic impact

**Note:** 
- Many observational studies lack explicit control groups.
- Study locations are mainly in Spain and France
- Economic impact is 

## Rationale
Effective management strategies require evidence-based decisions. To date, the quantitative evidence base for predation impacts and associated economic consequences remains fragmented. This exploratory work aims to assess whether sufficient evidence exists to conduct a systematic review or meta-analysis that may contribute to better-informed decisions about management policies, nest removal strategies, and beekeeping practices.

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
- initial search 2025-10-30: 56 references

### 1.4 Deduplication
[Rayyan](https://new.rayyan.ai/)
- imported references: 915
- duplications detected: 347
- unique references for phase I screening: 612

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
- Not English, -Dutch, -German language
- Simulation studies, models, prediction, laboratory conditions
- Reviews (check for missed articles with citation chaser)
- Gray literature
- Only nest removal methods (no impact data)
- Duplicate (data) of already included study

### 2.2 Download PDFs
- Free online: 32
- PDF requested 2025-11-01: 1
- `pdf_phaseI.csv` contains the list with the included articles for phase II screening

## 3 Phase II screening
### 3.1 Full-text screening
Screening based on full text and supplemental material (if available). `_updata_phase_II.md is used to instruct Cursor.AI to extract the quantitative items from the pdf's. First inclusion- and excludion criteria are extracted, subsequent additional quantifiable data are extracted. Short notes were allowed. The results are saved in a .md file with the similar name as the pdf. Then the were manualy checked, corrected and additional relevant information was added.
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
`pdf_phaseII.csv` contains the list with the included articles for phase II screening. 

## 4 Data Extraction

**Quantitative data** extracted from 33 studies on the impact of *Vespa velutina* on *Apis mellifera* in Europe.

### 4.1 Data Extraction
Draft data extraction of the quatitative data for each pdf is done with Cursor.ai and checked manually.
### 4.2 Predation Data

#### 4.2.1 Predation Rates and Success

| Study | Metric | Value | Sample Size | Location | Time Period | Notes |
|-------|--------|-------|-------------|----------|-------------|-------|
| Poidatz et al. 2023 | Overall predation success rate | 2.4% | 5,175 interactions | France | - | 126 successful events out of 5,175 interactions |
| Poidatz et al. 2023 | Success rate (bees entering hive) | 69.46% | 126 events | France | - | 4× higher for bees entering vs leaving |
| Poidatz et al. 2023 | Success rate (bees leaving hive) | 15.27% | 126 events | France | - | - |
| Poidatz et al. 2023 | Peak success (hornet number) | ~8 hornets | 5,175 interactions | France | - | Peak success at ~8 hornets, then decreases |
| Perrard et al. 2009 | Attack success rate | 25% | 359 attacks | France | 2007 | Average 4 trials necessary to catch one honeybee |
| Perrard et al. 2009 | Honeybee predation rate (captive) | 37.5 honeybees/day | 1 captive colony | France | 2007 | 25 to 50 honeybees per day (mean 37.5) |
| Monceau et al. 2013 | Maximum captures (hornet number) | 9 hornets | 2 hives | France | 2009 | Maximum captures at 9 hornets per hive |
| Monceau et al. 2013 | Peak capture time | 13:00-14:00 h | 2 hives | France | 2009 | Peak at midday (01:00-02:00 pm) |
| Monceau et al. 2013 | Hornets trapped (ART site) | 916 individuals | 14 hives | France | 2008 | Artigues-près-Bordeaux site |
| Monceau et al. 2013 | Hornets trapped (VIL site) | 1,894 individuals | 9 hives | France | 2008 | Villenave d'Ornon site |
| Monceau et al. 2013 | Peak capture (ART site) | 106 individuals | 14 hives | France | 2008 | 12th November 2008 |
| Monceau et al. 2013 | Peak capture (VIL site) | 217 individuals | 9 hives | France | 2008 | 12th November 2008 |
| Monceau et al. 2013 | Predation duration | 5 months | 23 hives | France | 2008 | 5 months duration |
| Monceau et al. 2013 | Delay to predation increase | 44 days | 23 hives | France | 2008 | Approximately 44 days from first capture |
| Monceau et al. 2014 | Hornets visiting daily | ~350 hornets | 6 hives | France | 2011 | ~350 hornets visiting patch daily |
| Monceau et al. 2014 | Maximum hornets (single hive) | 20 hornets | 6 hives | France | 2011 | Up to 20 hornets at same time |
| Monceau et al. 2014 | Recapture rate (D1 morning) | 73.94% | 188 marked | France | 2011 | 73 out of 188 |
| Monceau et al. 2014 | Recapture rate (overall) | 56.67% | 360 marked | France | 2011 | 204 out of 360 recaptured at least once |
| Monceau et al. 2014 | Daily visits per half-day | 1.88 visits | 360 marked | France | 2011 | Average range 1.70-2.20 |
| Rome et al. 2021 | Peak predation timing | Early October | 16 nests | France | 2008-2010 | - |
| Rome et al. 2021 | Peak predation time of day | Midday | 16 nests | France | 2008-2010 | Around midday |
| Diéguez-Antón et al. 2025 | Total hornets counted (all apiaries) | 11,406 individuals | 6 colonies | Spain | 2021-2022 | Total across all apiaries |
| Diéguez-Antón et al. 2025 | Predation pressure duration (Apiary 3) | 11 months | 2 colonies | Spain | 2021-2022 | Both years |

#### 4.2.2 Prey Composition

| Study | Metric | Value | Sample Size | Location | Time Period | Notes |
|-------|--------|-------|-------------|----------|-------------|-------|
| Rome et al. 2021 | Apis mellifera in prey pellets | 38.1% | 2,151 pellets | France | 2008-2010 | 820 out of 2,151 pellets |
| Rome et al. 2021 | Prey consumption per colony | 97,246.45 honeybee-equivalent | 16 nests | France | 2008-2010 | Per colony per season |
| Rome et al. 2021 | Biomass consumption per colony | 11.32 kg | 16 nests | France | 2008-2010 | 11.32 kg of insects per average colony per season |
| Rome et al. 2021 | Proportion hive production consumed | 40% | 16 nests | France | 2008-2010 | ~40% of individuals produced by one hive consumed by one hornet colony |
| Rome et al. 2021 | Wild bees proportion | 0.02% | 2,151 pellets | France | 2008-2010 | Bumblebees and solitary bees excluding wild honeybee colonies |
| Perrard et al. 2009 | Apis mellifera in pellets | 84.8% | 171 flesh pellets | France | 2007 | 145 out of 171 flesh pellets |
| Herrera et al. 2025 | Apis mellifera in diet | 22.55% | 7 nests | Spain | 2016 | 22.55% of Apidae family |
| Herrera et al. 2025 | Apis mellifera range | 14.86-29.27% | 7 nests | Spain | 2016 | Range across nests |
| Herrera et al. 2025 | Apis mellifera shared OTU | Yes | 7 nests | Spain | 2016 | Shared OTU across all nests |
| Pedersen et al. 2025 | Apis mellifera prevalence | 98.1% | 103 nests | Multiple | 2020-2022 | Found in every nest, average prevalence |
| Pedersen et al. 2025 | Apis mellifera found in all nests | 100% | 103 nests | Multiple | 2020-2022 | Found in every nest |
| Pedersen et al. 2025 | Top 50 prey pollinators | 43 species | 103 nests | Multiple | 2020-2022 | 43 were potential pollinators |
| Pedersen et al. 2025 | Crop pollinators dominant | 3 species | 103 nests | Multiple | 2020-2022 | 3 most dominant European crop pollinators |
| Stainton et al. 2023 | Honeybee detection rate | 65.8% | 38 samples | UK | 2016-2020 | Present in 25 of 38 larvae |
| Stainton et al. 2023 | Honeybee detection by nest | 80% | 5 nests | UK | 2016-2020 | 4 of 5 nests |
| Stainton et al. 2023 | Honeybee reads (Jersey) | 20.5% | 9 samples | UK | 2019 | - |
| Stainton et al. 2023 | Honeybee reads (Tetbury) | 0.33% | 10 samples | UK | 2016 | - |
| Stainton et al. 2023 | Honeybee reads (Woolacombe) | 7.3% | 10 samples | UK | 2017 | - |
| Verdasca et al. 2022 | Honeybee reads (total) | 75% | 32 samples | Portugal | 2018 | 79,143 out of 108,979 reads |
| Verdasca et al. 2022 | Honeybee reads (faecal pellets) | 84% | 12 samples | Portugal | 2018 | 50,549 out of 60,518 reads |
| Verdasca et al. 2022 | Honeybee reads (jaws) | 74% | 10 samples | Portugal | 2018 | 20,458 out of 27,546 reads |
| Verdasca et al. 2022 | Honeybee reads (stomachs) | 39% | 10 samples | Portugal | 2018 | 8,136 out of 20,915 reads |
| Verdasca et al. 2022 | Honeybee detection (faecal pellets) | 100% | 12 samples | Portugal | 2018 | All replicates of all samples |
| Verdasca et al. 2022 | Honeybee detection (jaws) | 70% | 10 samples | Portugal | 2018 | - |
| Verdasca et al. 2022 | Honeybee detection (stomachs) | 40% | 10 samples | Portugal | 2018 | - |
| Verdasca et al. 2022 | DNA persistence (faecal pellets) | ≥28 days | 12 samples | Portugal | 2018 | At least 28 days maximum known period |

### 4.3 Colony Survival and Loss

#### 4.3.1 Colony Survival

| Study | Metric | Value | Sample Size | Location | Time Period | Notes |
|-------|--------|-------|-------------|----------|-------------|-------|
| Requier et al. 2020 | Muzzle-equipped survival rate | 55% | 100 simulations | France | 2013-2016 | BEEHAVE model simulations |
| Requier et al. 2020 | Control survival rate | 35% | 100 simulations | France | 2013-2016 | BEEHAVE model simulations |
| Requier et al. 2020 | Survival increase (high hornets) | Up to 51% | 100 simulations | France | 2013-2016 | Up to 51% increase with >5 hornets |
| Rojas-Nossa et al. 2022 | Protected colony survival | 77.8% | Variable colonies | Spain | 2018-2020 | - |
| Rojas-Nossa et al. 2022 | Unprotected colony survival | 55.6% | Variable colonies | Spain | 2018-2020 | - |
| Requier et al. 2019 | Colony collapse rate | 55.3% | 993 simulations | France | 2012-2016 | BEEHAVE model simulations |
| Requier et al. 2019 | Collapse during predation period | 2.5% | 993 simulations | France | 2012-2016 | 24 colonies out of 993 |
| Diéguez-Antón et al. 2022 | Colony death | 1 colony | 2 colonies | Spain | 2020-2021 | Colony 2 died at end of study |
| Monceau et al. 2018 | Colony survival (H1) | Died | 1 hive | France | 2009 | Passed away first before winter |
| Monceau et al. 2018 | Colony survival (H2) | Died | 1 hive | France | 2009 | Survived longer but died later in winter |

#### 4.3.2 Mortality Factors

| Study | Metric | Value | Sample Size | Location | Time Period | Notes |
|-------|--------|-------|-------------|----------|-------------|-------|
| Requier et al. 2019 | Winter mortality (Profile A) | 100% | 27 simulations | France | 2012-2016 | Larvae population <5 individuals |
| Requier et al. 2019 | Winter mortality (Profile B low) | 80.5% | 288 simulations | France | 2012-2016 | Larvae >5 adult <9950 |
| Requier et al. 2019 | Winter mortality (Profile B high) | 96.8% | 288 simulations | France | 2012-2016 | Larvae >5 adult <9950 |
| Requier et al. 2019 | Winter mortality (Profile C) | 100% | 66 simulations | France | 2012-2016 | Larvae >5 adult >9950 honey ≤21 kg |
| Diéguez-Antón et al. 2025 | Risk threshold (minimum) | ≥5 hornets | 6 colonies | Spain | 2021-2022 | ≥5 hornets poses risk to colony survival |
| Diéguez-Antón et al. 2025 | Risk threshold (high) | ≥10 hornets | 6 colonies | Spain | 2021-2022 | ≥10 hornets high risk |
| Diéguez-Antón et al. 2025 | High pressure events (Apiary 1, Oct 2021) | 31 events | 2 colonies | Spain | 2021 | Events with >5 hornets |
| Diéguez-Antón et al. 2025 | High pressure days (Apiary 1, Oct 2021) | 5 days | 2 colonies | Spain | 2021 | Days with >10 hornets |
| Diéguez-Antón et al. 2025 | High pressure days (Apiary 2, Aug 2021) | 20 days | 2 colonies | Spain | 2021 | Days with ≥5 hornets |
| Jacques et al. 2017 | Winter mortality range (Year 1, low) | 5.01% | 2,332 apiaries | 17 countries | 2012-2014 | Italy lowest |
| Jacques et al. 2017 | Winter mortality range (Year 1, high) | 31.73% | 2,332 apiaries | 17 countries | 2012-2014 | Belgium highest |
| Jacques et al. 2017 | Seasonal mortality range (Year 1, low) | 0.09% | 2,332 apiaries | 17 countries | 2012-2014 | Lithuania lowest |
| Jacques et al. 2017 | Seasonal mortality range (Year 1, high) | 9.63% | 2,332 apiaries | 17 countries | 2012-2014 | France highest |
| Jacques et al. 2017 | Winter mortality range (Year 2, low) | 2.16% | 2,426 apiaries | 17 countries | 2012-2014 | Lithuania lowest |
| Jacques et al. 2017 | Winter mortality range (Year 2, high) | 13.85% | 2,426 apiaries | 17 countries | 2012-2014 | Belgium highest |
| Jacques et al. 2017 | Seasonal mortality range (Year 2, low) | 0.16% | 2,426 apiaries | 17 countries | 2012-2014 | Lithuania lowest |
| Jacques et al. 2017 | Seasonal mortality range (Year 2, high) | 8.06% | 2,426 apiaries | 17 countries | 2012-2014 | France highest |
| Jacques et al. 2017 | Hobby vs professional mortality | 14.04% vs 8.11% | 2,332 apiaries | 17 countries | 2012-2014 | Hobby beekeepers had double the winter mortality |
| Rojas-Nossa et al. 2022 | Honeybee weight reduction | 6.7% | Variable bees | Spain | 2018-2020 | Workers from unprotected hives 6.7% lighter |

### 4.4 Apis mellifera Behavior

#### 4.4.1 Foraging Paralysis Thresholds

| Study | Metric | Value | Sample Size | Location | Time Period | Notes |
|-------|--------|-------|-------------|----------|-------------|-------|
| Requier et al. 2019 | Foraging paralysis threshold | ≥12.6 hornets | 131 colonies | France | 2012-2016 | Complete FP at ≥12.6 hornets (95% CI) |
| Requier et al. 2019 | Foraging paralysis effect | Z=-20.65, P<0.001 | 603 observations | France | 2012-2016 | Negative impact on flight activity |
| Requier et al. 2020 | Foraging paralysis reduction (muzzle) | Up to 41% | 44 colonies | France | 2013-2016 | Up to 41% FP reduction with muzzle |
| Requier et al. 2020 | Muzzle activity (0 hornets) | 84% of baseline | 22 colonies | France | 2013-2016 | 84% of baseline activity |
| Requier et al. 2020 | Muzzle activity (20 hornets) | 76% of baseline | 22 colonies | France | 2013-2016 | 76% of baseline activity (16-24% FP) |
| Requier et al. 2020 | Control activity (0 hornets) | 100% of baseline | 22 colonies | France | 2013-2016 | 100% of baseline activity |
| Requier et al. 2020 | Control activity (20 hornets) | 35% of baseline | 22 colonies | France | 2013-2016 | 35% of baseline activity (0-65% FP) |
| Requier et al. 2020 | Control max FP | Up to 76% | 22 colonies | France | 2013-2016 | 95% CI prediction up to 76% FP |
| Monceau et al. 2018 | Foraging decline threshold | >10 hornets | 2 hives | France | 2009 | Above 10 hornets per hive number of foragers drops |
| Rojas-Nossa et al. 2022 | Foraging paralysis threshold | >0.8 hornets/hive/10min | Variable hives | Spain | 2018-2020 | Occurred at HRH > 0.8 |
| Diéguez-Antón et al. 2025 | Foraging paralysis observed | Yes | 6 colonies | Spain | 2021-2022 | Observed when hornet pressure is high |

#### 4.4.2 Activity Reductions and Behavioral Responses

| Study | Metric | Value | Sample Size | Location | Time Period | Notes |
|-------|--------|-------|-------------|----------|-------------|-------|
| Arca et al. 2014 | Colony activity drop | Dramatic drop | 95 colonies | France | 2008-2010 | Activity dropped dramatically when hornet present |
| Arca et al. 2014 | Bee-carpet formation (30-60% increase) | 14 colonies | 95 colonies | France | 2008-2010 | 30-60% increase in bee-carpet behavior |
| Arca et al. 2014 | Bee-carpet formation (60-80% increase) | 17 colonies | 95 colonies | France | 2008-2010 | 60-80% increase in bee-carpet behavior |
| Arca et al. 2014 | Bee-carpet formation (>80% increase) | 48 colonies | 95 colonies | France | 2008-2010 | >80% increase in bee-carpet behavior |
| Arca et al. 2014 | Bee-carpet pattern 1 | 42% | 95 colonies | France | 2008-2010 | Large number of honeybees gathered on flight board |
| Arca et al. 2014 | Bee-carpet pattern 2 | 20% | 95 colonies | France | 2008-2010 | Bee-carpet with coordinated behavior |
| Arca et al. 2014 | Bee-carpet pattern 3 | 38% | 95 colonies | France | 2008-2010 | No coordinated behavior |
| Arca et al. 2014 | Balling occurrence | 68 colonies (72%) | 95 colonies | France | 2008-2010 | 72% of colonies exhibited balling |
| Arca et al. 2014 | Balling size (<10 bees) | 31 colonies (33%) | 95 colonies | France | 2008-2010 | - |
| Arca et al. 2014 | Balling size (10-20 bees) | 20 colonies (21%) | 95 colonies | France | 2008-2010 | - |
| Arca et al. 2014 | Balling size (20-30 bees) | 15 colonies (16%) | 95 colonies | France | 2008-2010 | - |
| Arca et al. 2014 | Balling size (>30 bees) | 1 colony (1%) | 95 colonies | France | 2008-2010 | - |
| Arca et al. 2014 | Hornets killed by balling (outside) | 9.5% | 95 colonies | France | 2008-2010 | Only 9.5% hornets killed by balling in 5 min |
| Arca et al. 2014 | Hornets killed (inside hive) | 76.4% | 55 hornets | France | 2008-2010 | 42 out of 55 hornets killed inside hive |
| Arca et al. 2014 | Hornet hovering distance | ~15 cm | NA | France | 2008-2010 | About 15 cm from hive entrance |
| Monceau et al. 2013 | Flying activity pattern | Decreased | 2 hives | France | 2009 | Higher early morning, decreased afternoon/evening |
| Monceau et al. 2013 | Seasonal activity pattern | Decreased | 2 hives | France | 2009 | Higher in July, decreased throughout summer until October |
| Monceau et al. 2013 | Activity relation to hornets | Negative | 2 hives | France | 2009 | Negatively related to number of hornets |
| Monceau et al. 2013 | Returning foragers vs guards | P=0.01 | 2 hives | France | 2009 | Flying honeybees returning suffered more predation |
| Monceau et al. 2013 | Forager load extra mass | Up to 40% | NA | France | 2009 | Pollen or nectar loads can represent up to 40% extra body mass |
| Monceau et al. 2018 | Bee-carpet maximum timing | Late August-early September | 2 hives | France | 2009 | - |
| Monceau et al. 2018 | Bee-carpet maximum (hornets) | 7 hornets | 2 hives | France | 2009 | Maximum at 7 hornets |
| Monceau et al. 2018 | Honeybees tracking hornets (H1) | 21 instances | 1 hive | France | 2009 | - |
| Monceau et al. 2018 | Honeybees tracking hornets (H2) | 46 instances | 1 hive | France | 2009 | - |
| Monceau et al. 2018 | Balling occurrences (H1) | 2 occurrences | 1 hive | France | 2009 | - |
| Monceau et al. 2018 | Balling occurrences (H2) | 1 occurrence | 1 hive | France | 2009 | - |
| Poidatz et al. 2023 | Flight speed (bees leaving vs entering) | 1.9× faster | 603,259 trajectories | France | - | Bees leaving 1.9× faster than entering |
| Poidatz et al. 2023 | Flight speed (bees vs hornets) | 1.25× faster | 603,259 trajectories | France | - | Bees entering 1.25× faster than hornets |
| Poidatz et al. 2023 | Hovering time (hornets vs bees) | 2.1× more | 603,259 trajectories | France | - | Hornets 2.1× more hovering time than bees |
| Poidatz et al. 2023 | Speed increase (bees entering) | Positive | 603,259 trajectories | France | - | With hornet density |
| Poidatz et al. 2023 | Speed decrease (bees leaving) | Negative | 603,259 trajectories | France | - | With hornet density |
| Requier et al. 2019 | Homing failure effect | Z=-5.37, P<0.001 | 603 observations | France | 2012-2016 | Significantly dependent on flight activity |
| Requier et al. 2019 | Hornet activity period | 9:06-18:08 h | NA | France | 2012-2016 | Daily activity start and end time |
| Requier et al. 2019 | Peak activity period | September-October | NA | France | 2012-2016 | - |
| Poidatz et al. 2023 | Hornet activity peak | 13:00 h (1 pm) | NA | France | - | Peak at 1 pm |
| Poidatz et al. 2023 | Honeybee activity peak | 15:00 h (3 pm) | NA | France | - | Peak at 3 pm |
| Monceau et al. 2017 | Foraging flight peak (Nest A) | 14:00 h | 2 nests | France | 2008-2009 | 14:00 for Nest A |
| Monceau et al. 2017 | Foraging flight peak (Nest B) | 13:00 h | 2 nests | France | 2008-2009 | 13:00 for Nest B |
| Monceau et al. 2017 | Foraging flight seasonal peak | October | 2 nests | France | 2008-2009 | Reached maximum in October |
| Diéguez-Antón et al. 2022 | Daily activity period | 7:00-21:00 h | 2 colonies | Spain | 2020-2021 | 7:00 h - 21:00 h |
| Diéguez-Antón et al. 2022 | Peak months (2020) | September | 2 colonies | Spain | 2020 | Maximum number of hornets |
| Diéguez-Antón et al. 2022 | Peak months (2021) | October | 2 colonies | Spain | 2021 | Exponential increase |
| Diéguez-Antón et al. 2022 | Optimal temperature (hornet activity) | 15-25°C | 2 colonies | Spain | 2020-2021 | - |
| Diéguez-Antón et al. 2022 | Optimal humidity (hornet activity) | >60% | 2 colonies | Spain | 2020-2021 | - |
| Diéguez-Antón et al. 2022 | Hornet-temperature correlation | r=0.368, p<0.01 | 2 colonies | Spain | 2020-2021 | Positive correlation |
| Diéguez-Antón et al. 2022 | Hornet-humidity correlation | r=-0.347, p<0.01 | 2 colonies | Spain | 2020-2021 | Inverse correlation |
| Diéguez-Antón et al. 2025 | Optimal temperature range | 17-26°C | 6 colonies | Spain | 2021-2022 | Most suitable for observing higher number of hornets |
| Perrard et al. 2009 | Activity start time | 6:00 h | 1 captive colony | France | 2007 | Workers' flights |
| Perrard et al. 2009 | Activity end time | 22:00-22:30 h | 1 captive colony | France | 2007 | Dusk between 10:00 pm and 10:30 pm |
| Perrard et al. 2009 | Peak activity time | 15:30-16:30 h | 1 captive colony | France | 2007 | 3:30 pm to 4:30 pm |
| Perrard et al. 2009 | Minimum activity temperature | 10°C | 1 captive colony | France | 2007 | No activity below 10°C |

### 4.5 Economic Impact
**Website**: https://invacost.fr/  
**GitHub Repository**: https://github.com/Farewe/invacost  
**Data Format**: CSV/Excel bestanden, R package

### 4.6 Background data
#### 4.6.1 Invacost


#### 4.6.1 Study Locations
| Country | Number of Studies | Key Findings |
|---------|-------------------|--------------|
| France | [Count] | Highest number of studies, longest invasion history |
| Spain | [Count] | Multiple regions (Galicia, Catalonia, Mallorca) |
| Portugal | [Count] | [Findings] |
| United Kingdom | [Count] | Early detection and eradication efforts |
| Italy | [Count] | [Findings] |
| Other | [Count] | [Findings] |

### 4.6.2 Apiaries and Colonies

| Study | Apiaries | Colonies | Nests | Hornets | Notes |
|-------|----------|----------|-------|---------|-------|
| Arca et al. 2014 | 8 | 95 | Not specified | Variable | Defensive behavior study |
| Monceau et al. 2013 | 2 | 23 | Not specified | 2,810 trapped | Predation pressure |
| Requier et al. 2018 | 75 | 131 | Not specified | 0-20 observed | Foraging paralysis |
| Requier et al. 2020 | 22 | 44 | Not specified | 0-20 observed | Muzzle effectiveness |
| Diéguez-Antón et al. 2022 | 1 | 2 | Not specified | Variable | Photo monitoring |
| Diéguez-Antón et al. 2025 | 3 | 6 | Not specified | 11,406 total | Long-term pressure |
| Rojas-Nossa et al. 2022 | 3 | Variable | Not specified | 4,359 captured | Electric harps |
| Jacques et al. 2017 | 5,798 | Variable | Not applicable | Not applicable | Pan-European study |

### 4.6.3 Hornet Nests Studied

| Study | Nests | Method | Location |
|-------|-------|--------|----------|
| Rome et al. 2021 | 16 | Pellet collection | France |
| Verdasca et al. 2021 | 12 | Metabarcoding | Portugal |
| Herrera et al. 2025 | 7 | Meconium analysis | Spain (Mallorca) |
| Pedersen et al. 2025 | 103 | Larval gut contents | Multiple countries |
| Stainton et al. 2023 | 5 | Larval gut contents | UK |

### 4.7 Notes and biases
### 4.7.1 Study Locations

| Country | Number of Studies | Key Findings |
|---------|-------------------|--------------|
| France | [Count] | Highest number of studies, longest invasion history |
| Spain | [Count] | Multiple regions (Galicia, Catalonia, Mallorca) |
| Portugal | [Count] | [Findings] |
| United Kingdom | [Count] | Early detection and eradication efforts |
| Italy | [Count] | [Findings] |
| Other | [Count] | [Findings] |


### 4.7.2 Methodological Heterogeneity

- Different observation methods (visual, video, photo, trapping)
- Varying time periods and frequencies
- Different sample sizes and study designs
- Geographic and temporal variation
- Inconsistent statistical reporting


## 5. Key Quantitative Findings Summary

### 5.1 Spread

### 5.2 Impact
#### 5.2.1 Predation Pressure
- **Range**: 0-20+ hornets simultaneously at apiaries
- **Peak periods**: July-October (varies by location)
- **Success rate**: 2.4% (video tracking) to 76.4% (inside hive)
- **Honeybee in diet**: 22-98% depending on method and location

#### 5.2.2 Bee Colony Survival
- **Survival rates**: 35-78% depending on protection methods
- **Risk threshold**: ≥5 hornets poses risk to colony survival

#### 5.2.3 _Apis mellifera_ behavior
- **Foraging paralysis**: Complete at ≥12.6 hornets

#### 5.2.3 Economic Impact
**Website**: https://invacost.fr/  
**GitHub Repository**: https://github.com/Farewe/invacost  
**Data Format**: CSV/Excel bestanden, R package

### 5.3 Management responses


## Notes

- This synthesis is based on extracted quantitative data from included studies
- Numbers are reported as found in original studies
- Ranges and means are presented where available
- Statistical significance is noted where reported
- Methodological differences between studies should be considered when interpreting results
- This summary is made with a human in the loop, when you see an error please make an issue.
# Impact of Vespa velutina on Apis mellifera in Europe
Klik [hier]() voor de nederlandse versie.
## Project Status

- **Current Phase:** Data extraction
- **Status:** Work in progress


This repository contains available articles on the impact of *Vespa velutina* (Asian hornet) on honeybees (*Apis mellifera*) in Europe. The aim is to develop an online summary of published data in a monthly updated repository.

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

#### 4.2.2 Prey Composition 

### 4.3 Colony Survival and Loss
#### 4.3.1 Colony Survival

#### 4.3.2 Mortality Factors

### 4.4 Apis mellifera behavior

#### 4.4.1 Foraging Paralysis Thresholds

#### 4.4.2 Activity Reductions

### 4.5 Economic Impact
Invacost

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

### 5.1 Predation Pressure
- **Range**: 0-20+ hornets simultaneously at apiaries
- **Peak periods**: July-October (varies by location)
- **Success rate**: 2.4% (video tracking) to 76.4% (inside hive)
- **Honeybee in diet**: 22-98% depending on method and location

### 5.2 Colony Survival
- **Survival rates**: 35-78% depending on protection methods
- **Risk threshold**: ≥5 hornets poses risk to colony survival

### 5.3 _Apis mellifera_ behavior
- **Foraging paralysis**: Complete at ≥12.6 hornets

### 5.3 Economic Impact
Invacost


## Notes

- This synthesis is based on extracted quantitative data from included studies
- Numbers are reported as found in original studies
- Ranges and means are presented where available
- Statistical significance is noted where reported
- Methodological differences between studies should be considered when interpreting results
- This summary is made with a human in the loop, when you see an error please make an issue.
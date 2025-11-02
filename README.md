# Meta-Analysis: Impact of Vespa velutina on Apis mellifera in Europe

## Project Status

**Current Phase:** Data extraction  
**Status:** Work in progress  
**Last Updated:** [To be updated]

This repository contains the systematic review and meta-analysis quantifying the impact of *Vespa velutina* (Asian hornet) on honeybees (*Apis mellifera*) in Europe. 



Meta-analysis quantifying the impact of Vespa velutina (yellow-legged hornet) predation on Apis mellifera (honeybee) colonies in Europe. PRISMA 2020 compliant systematic review assessing predation effects, colony losses, and economic consequences for beekeeping.

Meta-analysis of Vespa velutina predation impact on Apis mellifera in Europe. PRISMA 2020 systematic review investigating colony losses, foraging activity, and economic impacts on European beekeeping operations.

Systematic review and meta-analysis of Vespa velutina (yellow-legged hornet) predation effects on Apis mellifera colonies in Europe. PRISMA 2020 compliant, assessing predation, colony losses, and beekeeping productivity.





---

## Project Overview

Nearly a quarter century has passed since _Vespa velutina_ arrived by accident in Europe. And this **yellow-legged hornet** with its yellow legs is using her wings to spread over a large part of Europe. For the protein to raise the next generation, they don't make it difficult for themselves. In Europe domesticated bees (_Apis mellifera_) are widely available and easy to catch. So, let's find out what is published about the contribution of the **yellow-legged hornet** to the decline of Western **honeybee** populations.

`*yellow-legged hornet` is to prefer above `Asian hornet`, to avoid confusion with the the Asian `Vespa soror` that also arrived in Europe.

This meta-analysis investigates:

**Primary Objective:**
- Quantify the impact of *Vespa velutina* predation on managed *Apis mellifera* colonies in Europe.

**Secondary Objectives:**
- Assess effects on bee health and beekeeping productivity, including:
  - Colony losses and survival
  - Reduced foraging activity
  - Honey yield reductions
  - Economic consequences for apiculture

## Why?

The Yellow-legged hornet (Vespa velutina) was reported from the Netherlands in 2018 for the second year in a row. This hornet, originally from southeast Asia, is considered an invasive species. As such, it is placed on the European “List of Invasive Alien Species of Union concern” and should be rapidly eradicated.

---

## Data extraction

- What data is available about the predation of _Vespa velutina_ 
- What other data is available about the 

---

## Methods Overview

### Literature Search

**Search Date:** October 30, 2025

**Databases Searched:**
- Lens.org: 767 references
- OpenAlex: 67 articles, 5 preprints
- PubMed: 45 references
- Google Scholar: 2,160 results (screened for additional relevant studies)

**Search Strategy:**
Searches were restricted to:
- *Apis mellifera*
- European Union and United Kingdom
- Free/open-access databases prioritized

Total unique references after deduplication: 612 (from initial 951)

Additional sources:
- Review citations: 33 references from included reviews
- Review references: 39 references from included reviews

### Study Selection

**Inclusion Criteria:**
- **Language:** English, Dutch, German
- **Geographic Scope:** European Union or United Kingdom
- **Study Types:** Observational and experimental studies
- **Primary Focus:** Predation of *Apis mellifera* by *Vespa velutina*, or secondary effects on beekeeping (colony survival, losses, mortality, honey yield, foraging activity, economic impacts)
- **Other Literature:** Reviews and meta-analyses included for citation chasing

**Exclusion Criteria:**
- Duplicates
- Languages other than English, Dutch, or German
- Non-EU and non-UK studies
- Opinion papers without original data
- Theoretical papers (forecasts and models) without linkage to beekeeping, ecological, or economic outcomes
- Studies focusing solely on nest removal efficiency, trap design, or management logistics
- Simulation studies, models, predictions, or laboratory conditions without field validation
- Studies without *Apis mellifera* or *Vespa velutina* data
- Books (excluded from gray literature)

**Screening Process:**
- Phase 1: Title and abstract screening (using ASReview)
- Phase 2: Full-text screening
- Deduplication: Rayyan (951 → 612 unique items)

### Data Extraction

**Extracted Variables:**
- Study ID
- Country
- Population (worker bees, foragers, brood, colonies, drones, queens, not specified)
- *A. mellifera* subspecies (carnica, ligustica, Buckfast bees, *A. m. mellifera*, not specified)
- Impact type (bee health, colony survival, molecular impact on bees, colony endpoints)
- Co-exposures (nutrition, pesticides)
- Endpoints:
  - Colony endpoints: number of adult bees, quantity of capped/uncapped brood and/or eggs, hive production (honey, pollen, nectar combs), hive weight
  - Individual endpoints: mortality rate, behavior (foraging)
  - Molecular endpoints: genetic, cellular
- Study type (field studies only; laboratory studies, models, and predictions excluded)
- Scale of the study

**Current Status:** Data extraction in progress

### Statistical Analysis

**Effect Size Calculations:**
- Primary outcomes: Log risk ratio or hazard ratio for mortality/survival
- Secondary outcomes: Log response ratio or SMD; Fisher z for correlation-based indices

**Planned Analyses:**
- Random-effects meta-analysis (effect size estimation and heterogeneity assessment)
- Meta-regression (moderator analyses)
- Publication bias assessment (Egger's test, funnel plot asymmetry)
- Sensitivity analysis

**Software:**
- R packages: meta, metafor, metaan, tidyverse

---

## Draft Manuscript Sections

*Note: The following sections are drafts and subject to revision as data extraction and analysis progress.*

### Abstract

*[Draft in progress]*

It is time to analyze the impact of the Asian hornet on managed *Apis mellifera* in Europe. Almost a quarter of a century ago *Vespa velutina* started its colonization of Europe and it is accused of contributing to the decline of the western honey bees. Before deciding if and what actions are needed, we should first see if there is solid proof that these accusations hold weight.

### Introduction

*[Draft section to be expanded]*

### Materials and Methods

#### Keywords and Databases

See Methods Overview section above for detailed search strategy and database information.

#### Literature Search

**Phase 1:** Title and abstract screening  
**Phase 2:** Full-text screening using ASReview

See Research Questions and Methods Overview sections for inclusion and exclusion criteria.

**PRISMA Flow Diagram:** [To be added when available]

#### Data Extraction

See Methods Overview section for extracted variables and current status.

#### Calculation of Effect Sizes

*[To be detailed during analysis phase]*

#### Analysis of Effect Size and Heterogeneity

*[To be detailed during analysis phase]*

#### Publication Bias and Sensitivity Analysis

*[To be detailed during analysis phase]*

### Results

*[To be completed following data extraction and analysis]*

### Discussion

*[To be completed following analysis]*

### Conclusions

*[To be completed following analysis]*

---

## Repository Structure

*[Repository structure will be documented once folders are created for PDFs and R code]*

---

## Reproducibility and Transparency

This project adheres to:
- **PRISMA 2020 Statement** for systematic review reporting
- **MOOSE Guidelines** for observational studies in meta-analyses
- **FAIR Principles** for data and research outputs

All search strategies, screening criteria, data extraction protocols, and analytical code will be made available to ensure full reproducibility.


---

## References

*[References will be maintained and updated as the project progresses]*

---

## Methodological Limitations

**Current Limitations:** Only freely available literature databases could be used, and only PDFs that are freely available online or sent after a request to the first author. This meta-analysis is currently being conducted by a single researcher. As such, study screening, data extraction, and quality assessment are performed without independent second-reviewer verification at this stage.

Efforts are ongoing to to obtain the remaining papers that are not freely available and are still missing. And to recruit a second reviewer for independent verification of screening, data extraction, and quality assessments to strengthen the reliability and validity of the review findings.


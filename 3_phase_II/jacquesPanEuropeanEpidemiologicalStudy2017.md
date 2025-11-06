# QUANTITATIVE DATA EXTRACTION - Jacques et al. 2017 (EPILOBEE)

## Template-Relevant Data

### Study Identification
- **Author**: Jacques, A.
- **Publication Year**: 2017
- **Title**: A pan-European epidemiological study reveals honey bee colony survival depends on beekeeper education and disease control
- **Journal**: PLOS ONE
- **DOI**: 10.1371/journal.pone.0172591

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 0 (focus on colony mortality, not direct predation)
- **in_other_spec_predation**: 0
- **in_apis_colony_loss**: 1
- **in_apis_foraging**: 0
- **in_apis_other_behavior**: 0
- **in_honey_yield**: 0
- **in_beekeeping_loss**: 0
- **in_management_costs**: 0

### Observation Types
- **type_observation_visual**: 1
- **type_observation_photo**: 0
- **type_observation_video**: 0
- **type_pellets**: 0
- **type_radio_freq**: 0
- **type_CIO_faeces**: 0
- **type_costs**: 0

### Location and Time
- **country**: 17 European countries (Belgium, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Italy, Latvia, Lithuania, Poland, Portugal, Slovakia, Spain, Sweden, England & Wales)
- **start_year**: 2012
- **end_year**: 2014
- **start_month**: Autumn (V1), Spring (V2), Summer (V3)
- **end_month**: Summer (V3)

### Sample Sizes
- **n_apiaries**: 5,798 total (2,332 year 1, 2,426 year 2 after quality checks)
- **n_beehives**: Not specified (colonies per apiary varied)
- **n_vespa_nests**: Not applicable (general honey bee health study)
- **n_vespa_velutina**: Not applicable
- **distance_hornets_nest**: Not applicable

### Outcomes
- **outcome_apis_predation**: Not directly measured
- **outcome_predation_time_of_the_day**: Not specified
- **outcome_apis_behavior_foraging**: Not specified
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Not specified

## Other Quantitative Data

### Study Details
- **Study period**: Autumn 2012 - Summer 2014 (2 consecutive years)
- **Total apiaries monitored**: 5,798
- **Apiaries retained for analysis**: 2,332 (year 1), 2,426 (year 2)
- **Apiaries excluded**: 721 (year 1), 319 (year 2) due to missing data or inconsistencies
- **Visits per apiary**: 3 (autumn V1, spring V2, summer V3)
- **Countries**: 17 European Member States
- **England & Wales**: Participated year 1 only

### Mortality Rates - Year 1
- **Winter mortality range**: 5.01% (Italy) to 31.73% (Belgium)
- **Seasonal mortality range**: 0.09% (Lithuania) to 9.63% (France)
- **Clusters**:
  - High mortality: Belgium (31.73%), England & Wales
  - Upper middle: Estonia, Finland, Latvia, Poland, Sweden
  - Lowest middle: France (9.63%), Denmark, Germany, Hungary, Portugal, Slovakia, Spain
  - Low: Greece, Italy (5.01%), Lithuania (0.09%)

### Mortality Rates - Year 2
- **Winter mortality range**: 2.16% (Lithuania) to 13.85% (Belgium)
- **Seasonal mortality range**: 0.16% (Lithuania) to 8.06% (France)
- **Clusters**:
  - High mortality: Belgium (13.85%), France (8.06%)
  - Upper middle: Denmark, Estonia, Finland, Latvia, Portugal, Sweden
  - Lowest middle: Greece, Spain
  - Low: Germany, Hungary, Italy, Lithuania (2.16%), Poland, Slovakia

### Link Between Winter and Seasonal Mortality
- **Year 1**: Spearman correlation coefficient = 0.071, P=6×10⁻⁴
- **Year 2**: Spearman correlation coefficient = 0.142, P=2×10⁻¹²
- **Interpretation**: Positive but weak link - high winter losses tend to be followed by high summer losses

### Risk Factors - Winter Mortality
- **Variables analyzed**: 33 variables
- **Year effect**: P=1×10⁻³⁷ (highly significant)
- **Cluster W1 (highest mortality: 14.04%)**:
  - Hobby beekeepers, small apiaries (size 1)
  - Age: >65 years
  - Environment: Farmland, town, or woods
  - Production: Queens
  - No beekeeping training (past 3 years)
  - No apiarist book
  - No qualification
  - Not member of beekeeping organization
  - No cooperative Varroa treatment
  - Experience: 2-5 years
  - Varroosis at autumn visit
- **Cluster W2 (lowest mortality: 8.11%)**:
  - Professional beekeepers
  - Age: 30-45 years
  - Large apiaries and operations (size 3)
  - Environment: Floral
  - Migration: Crops or diverse environment
  - Production: Diverse (honey, queens, pollen)
  - Beekeeping training (past 3 years)
  - Apiarist book used
  - Qualification in beekeeping
  - Member of beekeeping organization
  - Experience: >5 years
  - No disease at autumn visit
- **Mortality difference**: Hobby beekeepers had double the winter mortality (14.04%) compared to professionals (8.11%)

### Risk Factors - Seasonal Mortality
- **Variables analyzed**: 28 variables
- **Year effect**: P=1×10⁻³ (significant)
- **Cluster S1 (highest mortality: 7.81%)**:
  - No beekeeping training (past 3 years)
  - No cooperative Varroa treatment
  - No apiarist book
  - Previous winter mortality: 21-50%
  - No health events before study, but AFB found at spring visit
- **Cluster S2 (lowest mortality: 1.81%)**:
  - Beekeeping training attended
  - Apiarist book used
  - Cooperative Varroa treatment
  - No previous winter mortality
  - Health events before study, but no disease at spring visit

### Statistical Methods
- **Imputation**: Multiple correspondence analysis (MCA) for missing data
- **Models**: Quasi-Poisson generalized linear models (GLM)
- **Variable selection**: P<0.20 threshold
- **Clustering**: MCA and classification using FactoMineR package
- **Synthetic variables**: 7 categories (W1-W7 for winter, S1-S7 for seasonal)
- **Random effects**: Country and year
- **Mixed models**: glmer function from lme4 R package

### Beekeeper Categories
- **Size 1**: Operation <50 colonies, apiary <20 colonies
- **Size 2**: Operation <50 colonies, apiary 21-50 colonies
- **Size 3**: Operation 51-300 colonies, apiary >50 colonies
- **Size 4**: Operation >300 colonies, apiary >50 colonies
- **Age groups**: <30, 30-45, 45-65, >65 years

### Diseases Monitored
- Nosemosis (fungal)
- Varroosis (parasitic)
- American Foulbrood (AFB, bacterial)
- European Foulbrood (EFB, bacterial)
- Chronic Bee Paralysis Virus (CBPV, viral)

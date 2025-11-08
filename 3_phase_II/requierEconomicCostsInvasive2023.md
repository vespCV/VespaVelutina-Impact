# QUANTITATIVE DATA EXTRACTION - Requier et al. 2023

## Template-Relevant Data

### Study Identification
- **Author**: Requier, Fabrice; Fournier, Alice; Pointeau, Sophie; Rome, Quentin; Courchamp, Franck
- **Publication Year**: 2023
- **Title**: Economic costs of the invasive Yellow-legged hornet on honey bees
- **Journal**: Science of the Total Environment
- **DOI**: 10.1016/j.scitotenv.2023.165576

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0 (preprint version, but peer-reviewed publication exists)
- **ex_no_pdf**: 0
- **in_apis_predation**: 0 (indirect - through mortality risk)
- **in_other_spec_predation**: 0
- **in_apis_colony_loss**: 1
- **in_apis_foraging**: 0
- **in_apis_other_behavior**: 0
- **in_honey_yield**: 0
- **in_beekeeping_loss**: 1
- **in_management_costs**: 0

### Observation Types
- **type_observation_visual**: 1 (field observations of hornet nests and predation activity)
- **type_observation_photo**: 0
- **type_observation_video**: 0
- **type_pellets**: 0
- **type_radio_freq**: 0
- **type_CIO_faeces**: 0
- **type_costs**: 1

### Location and Time
- **country**: France
- **start_year**: 2013
- **end_year**: 2017 (fieldwork), 2015 (bee colony data)
- **start_month**: Not specified
- **end_month**: Not specified

### Sample Sizes
- **n_apiaries**: 51 plots (359 observations)
- **n_beehives**: Variable (4-24 colonies per apiary)
- **n_vespa_nests**: 1,260 nests recorded (field observations)
- **n_vespa_velutina**: Variable (1-20 hornets per nest in scenarios)
- **distance_hornets_nest**: Foraging range estimated ca. 1 km (physiologically up to 30 km)

### Outcomes
- **outcome_apis_predation**: Not directly measured, but predation pressure scenarios modeled
- **outcome_predation_time_of_the_day**: Observations between 10am and 5pm
- **outcome_apis_behavior_foraging**: Foraging paralysis included in model (from Requier et al. 2019)
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Included in mortality risk model

## Other Quantitative Data

### Field Data Collection

#### Hornet Nest Monitoring
- **Fieldwork period**: 2013-2017 (5 years)
- **Study areas**: 4 French districts (Pyrénées-Atlantiques, Vendée, Morbihan, Deux-Sèvres)
- **Search method**: 3 km radius circles around randomly selected locations
- **Number of circles**: 90 circles total (17±9 circles per district)
- **Search area**: 28,348 km² (total area of four monitored districts)
- **Nests recorded**: 1,260 nests
- **Nest density**: 1.08 nest/km² (overall density in France)
- **Search timing**: Between fall and spring (after trees shed leaves)
- **Search method**: Driving along public roads, 600-800 km drive per district
- **Observation hours**: 10am-5pm
- **Data verification**: Double-checked by Yellow-legged hornet experts

#### Bee Colony Data
- **Data source**: French Ministry of Agriculture (mandatory beekeeper declarations)
- **Reference year**: 2015
- **Total colonies (France)**: 1,056,314 colonies
- **Townships with colonies**: 23,870 out of 36,571 (65.2% of townships, 77.0% of France's surface)
- **Colonies per township**: Range 0-2,377, mean 28.9 (sd = 67.2)
- **Spatial resolution**: Township level (municipality area)
- **Mean township size**: 1,500 hectares (side length: 3.87 km square, range: 3 to 75,780 hectares)

#### Predation Activity Observations
- **Observation period**: June 1 to November 19, 2017
- **Observation frequency**: Every 15 days
- **Observation duration**: ~1 minute per hive
- **Replicates**: 5 observations per colony over 15-day period
- **Observation hours**: 10am-5pm
- **Total observations**: 359 observations
- **Number of plots**: 51 different plots
- **Colonies per apiary**: 4-24 colonies
- **Survival check**: November 19, 2017 (last observation date)
- **Weather conditions for survival check**: Temperature >20°C, sunshine, no wind

### Spatial Modeling Results

#### Hornet Nest Density Model
- **Model type**: Random forest regression
- **Model accuracy**: R² = 0.443, RMSE = 0.763
- **Mean difference (predicted vs observed)**: 0.187 (sd = 0.356, min = 0, max = 8.16)
- **Model agreement**: 99.9% of exhaustively searched area had similar rounded densities
- **Mean nests per township**: 15.5 (sd = 15.9, min = 0, max = 282)
- **Mean nest density**: 1.08 nest/km² (sd = 0.467, min = 0, max = 36.5)
- **Top predictive variables**:
  - Urban cover: 95.2% of increased node purity
  - Mean temperature of warmest quarter: 79.9%
  - Wind speed: 70.1%
- **Model parameters**: 500 trees per forest, 9 randomly sampled variables per node (out of 39 available)
- **Average prediction uncertainty**: 0.172 (sd = 0.216, min = 0.0215, max = 27.2)
- **Highest nest densities**: South-East and Western parts of France

#### Bee Colony Distribution
- **Mean colonies per township**: 28.9 (sd = 67.2, min = 0, max = 2,377)
- **Highest colony densities**: South-East and Western parts of France
- **Mean ratio (colony density / nest density)**: 1.86 (sd = 3.76, range: 0-136)
- **Colonies subject to predation**: 98.2% (1,017,713 colonies out of 1,056,314)

### Mortality Risk Modeling

#### BEEHAVE Model Simulations
- **Number of simulations**: 1,000
- **Simulation period**: January to May of following year (includes complete winter season)
- **Predation period in model**: Day 240 (August 28) to Day 310 (November 6)
- **Foraging distance parameter**: Decreased from 7,299 km/day (default, unlimited) down to 0 (no foraging)
- **Forager mortality probability**: Increased from 1.00e-05 to 2.00e-05 per second foraging
- **Hornet pressure range**: 0 (no hornets) to 20 hornets simultaneously at colony entrance
- **Mortality thresholds**:
  - Population size <4,000 adult bees during winter
  - Total depletion of honey stock during winter

#### Predation Scenarios
- **Low predation scenario**: 1 hornet/nest predating simultaneously
- **High predation scenario**: 20 hornets/nest predating simultaneously
- **Foraging range assumption**: Hornets can reach all colonies in same township (mean township side: 3.87 km)
- **Physiological foraging range**: Up to 30 km (laboratory tests, Sauvard et al. 2018)
- **Field foraging range**: Estimated ca. 1 km around nest (Kennedy et al. 2018; Poidatz et al. 2018)

#### Predicted Colony Losses

**Low Predation Scenario (1 hornet/nest)**:
- **Total colonies lost**: 27,821 colonies
- **Percentage of national livestock**: 2.6%
- **Average loss per township**: 10.2% (sd = 15.3%)

**High Predation Scenario (20 hornets/nest)**:
- **Total colonies lost**: 308,379 colonies
- **Percentage of national livestock**: 29.2%
- **Average loss per township**: 48.3% (sd = 25.7%)

**Spatial distribution**: Heterogeneous across France (see Fig. S4)

### Economic Cost Estimates

#### Colony Replacement Cost
- **Average replacement price**: €100 per colony lost (Requier et al. 2020a)

#### National Economic Costs

**Low Predation Scenario**:
- **Yearly economic cost**: €2.8 million per year

**High Predation Scenario**:
- **Yearly economic cost**: €30.8 million per year

#### Regional Economic Costs (High Predation Scenario)
- **Average regional cost**: €1.3 million per year
- **Range**: €0.4 million (Corse) to €5.5 million (Occitanie)
- **Number of regions**: 13 administrative regions

#### Honey Production and Revenues
- **National honey production (2015)**: 14,490 tons
- **Honey revenue (national)**: €116 million (at €8/kg average price)
- **Regional honey production**: Range 137-3,188 tons per region
- **Honey price**: €8/kg (average price in France, source: France AgriMer)

#### Economic Impact (Livestock Replacement vs Honey Revenues)

**National Scale**:
- **Low predation scenario**: 2.4% of honey revenues
- **High predation scenario**: 26.6% of honey revenues

**Regional Scale (High Predation Scenario)**:
- **Average impact**: 21.9% of honey revenues
- **Range**: 13.2% (Bourgogne-Franche-Comté) to 96.5% (Normandie)
- **Regional correlation**: No correlation between economic cost and economic impact (Spearman's correlation test: n = 13, S = 390, P = 0.82)

### Model Validation

#### Cross-Validation Results
- **Validation method**: 10-fold cross-validation for RMSE
- **Out-of-bag data**: 10% randomly sampled for each run
- **Variance estimation**: Infinitesimal jackknife procedure (Wager et al. 2014)
- **Field validation**: Predictions and observations of colony survival were concordant (Fig. S2)
- **Validation limitation**: Field data restricted to period before colony overwintering

### Additional Contextual Data

#### Invasion History
- **Introduction to France**: 2004 (from China)
- **Spread to other countries**:
  - Spain: 2011
  - Portugal: 2012
  - Belgium: 2013
  - Italy: 2016
  - Germany: 2015
  - United Kingdom: 2017
  - Netherlands: 2017
  - Luxembourg: 2021
  - Switzerland: 2022

#### Control Costs (from Barbet-Massin et al. 2020)
- **Yearly control cost (France)**: €11.9 million
- **Comparison**: Damage cost (€30.8M) up to 3× higher than control cost

#### Pollination Services Context
- **Global pollination benefit**: €153 billion yearly (Gallai et al. 2009)
- **France pollination benefit**: €2.3-5.3 billion (Beyou et al. 2016)
- **Beekeeper livestock increase**: ~130% each year to compensate high loss rates (Ferrier et al. 2018)

#### Predation Diet Composition (from literature)
- **Honey bees in autumn diet**: 70% of food intake
- **Other insects in autumn diet**: 30% of food intake (including wild pollinators)

### Statistical and Methodological Notes

#### Model Assumptions and Limitations
- **Colony database limitation**: Only declared colonies included (likely underestimates real numbers)
- **Wild colonies**: Excluded from database (but present in Europe)
- **Low predation scenario**: 1 hornet/nest is lower than average observed (mean 2.3, sd = 3.4, min = 0, max = 20 from Requier et al. 2020a)
- **High predation scenario**: 20 hornets/nest is maximum observed value (realistic but extreme)
- **Winter mortality context**: Rarely exceeds 30% in France/Europe (all stress factors combined)
- **Spatial resolution**: Township-level data forced assumption that hornets reach all colonies in same township
- **Nest size variation**: Wide variation in France (Rome et al. 2015), but no data on predators per nest
- **Bioclimatic coverage**: Dataset restricted to Western France, may have uncertainties for other regions (highlands, mountains)

#### Data Availability
- **Public repository**: figshare (DOI: 10.6084/m9.figshare.22328545.v1)

### Funding
- European Community program (grant 797/2004) for French beekeeping (RISQAPI project)
- French National Research Agency (grant ANR-14-CE02-0021)
- AXA Research Fund Chair of Invasion Biology of University Paris-Saclay
- AlienScenario BiodivERsA project (grant BMBF/PT DLR 01LC1807C)


# QUANTITATIVE DATA EXTRACTION - Monceau et al. 2018

## Template-Relevant Data

### Study Identification
- **Author**: Monceau, K.
- **Publication Year**: 2018
- **Title**: How Apis mellifera Behaves with its Invasive Hornet Predator Vespa velutina?
- **Journal**: Journal of Insect Behavior
- **DOI**: 10.1007/s10905-017-9658-5

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 1
- **in_other_spec_predation**: 0
- **in_apis_colony_loss**: 0
- **in_apis_foraging**: 1
- **in_apis_other_behavior**: 1
- **in_honey_yield**: 0
- **in_beekeeping_loss**: 0
- **in_management_costs**: 0

### Observation Types
- **type_observation_visual**: 0
- **type_observation_photo**: 0
- **type_observation_video**: 1
- **type_pellets**: 0
- **type_radio_freq**: 0
- **type_CIO_faeces**: 0
- **type_costs**: 0

### Location and Time
- **country**: France
- **start_year**: 2009
- **end_year**: 2009
- **start_month**: 6
- **end_month**: 11

### Sample Sizes
- **n_apiaries**: 1
- **n_beehives**: 2 (H1 and H2)
- **n_vespa_nests**: 6 nests within 1 km
- **n_vespa_velutina**: Not specified (monitored via video)
- **distance_hornets_nest**: Within 1 km

### Outcomes
- **outcome_apis_predation**: Not specified
- **outcome_predation_time_of_the_day**: Not specified
- **outcome_apis_behavior_foraging**: Number of foragers declined during season and due to increasing hornet predation pressure. Above 10 hornets per hive, number of foragers drops
- **outcome_other_apis_behavior**: Negative relationship between foraging and defence (bee-carpet). Number of honeybees on flight board varied with date and number of hornets. Maximum reached in late August-early September and for 7 hornets. Balling behavior observed: 21 instances for H1, 46 for H2 (tracking), 3 occurrences of balling (2 for H1, 1 for H2)
- **outcome_apis_behavior_paralysis**: Not specified

## All Other Quantitative Data

### Study Details
- **Study period**: June-November 2009
- **Location**: Experimental apiary (INRA, Villenave d'Ornon, France)
- **GPS coordinates**: N 44°47'31.26", W 0°34'29.99"
- **Hive type**: A. mellifera mellifera
- **Hive appearance**: Equivalent visual appearance
- **Colony size**: Unknown but did not differ in number of flying honeybees (Wilcoxon rank sum test: W = 9040.5, P = 0.41, N = 138 for H1, 139 for H2)
- **Bees on flight board**: No difference (W = 10,087, P = 0.45)
- **Hornets at entrance**: No difference (W = 10,204.5, P = 0.35)

### Video Recording Setup
- **Camera type**: Black and white Dragonfly Point Grey
- **Resolution**: 640 × 480
- **Frame rate**: 100 FPS
- **Recording software**: Numeriscope (Viewpoint, France)
- **Recording schedule**: Sunrise to sunset (diurnal insects)
- **Recording period**: 19/06/2009 to 23/11/2009
- **Total footage**: >2000 h of observation per hive

### Video Analysis
- **Analysis start**: 10/07/2009 (first hornet of season spotted)
- **Analysis end**: 25/10/2009 (colonies had no more honeybee activity)
- **Sample days**: 11 sample days (every 10 days, some postponed due to adverse conditions)
- **Total sample points**: 139 per hive (range: 10-14 per day per hive)
- **Analysis software**: VLC software v. 1.1.11
- **Single analyzer**: L.L. (to avoid experimenter bias)

### Hornet Monitoring
- **Monitoring period**: First 5 minutes of each sample point
- **Count method**: Maximum number of hornets in frame at same time (to avoid pseudo-replication)
- **Outlier excluded**: 20 hornets on H2 on 15th September (clearly biased the model)

### Honeybee Monitoring
- **Monitoring period**: First 2 minutes of each sample point
- **Parameters**: 
  - Number of honeybees on hive flight board (colony defensiveness/bee-carpet)
  - Number of honeybees entering hive (foraging activity)
- **Validation**: Number of honeybees leaving and entering similar (Monceau et al. 2013a)

### Statistical Analysis
- **Model type**: Negative Binomial Generalized Linear Models (NBGLM)
- **Effects included**: Date (linear and quadratic), number of hornets (linear and quadratic for bee-carpet analysis)
- **Collinearity check**: Variance inflation factor (VIF, Dormann et al. 2013)
- **Test method**: Binomial tests for anecdotic behaviors
- **Software**: R v. 3.3.1 (R Core Team 2016)
- **Packages**: car (deviance analysis), usdm (collinearity test)

### Relationship Between Foraging and Defence
- **Statistical test**: NBGLM χ² = 9.22, df = 1, P < 0.01
- **Relationship**: Negative (number of honeybees returning to hive negatively related to number on flight board forming bee-carpet)
- **Seasonal effect (linear)**: χ² = 0.77, df = 1, P = 0.38 (not significant)
- **Seasonal effect (quadratic)**: χ² = 14.16, df = 1, P < 0.001
- **Pattern**: Declined during season

### Hornet Predation Pressure and Foraging
- **Seasonal effect (linear)**: χ² = 0.10, df = 1, P = 0.75 (not significant)
- **Seasonal effect (quadratic)**: χ² = 8.85, df = 1, P < 0.01
- **Hornet effect**: χ² = 4.46, df = 1, P = 0.03
- **Pattern**: Number of foragers declined during season and due to increasing hornet predation pressure
- **Threshold**: Above 10 hornets per hive, number of foragers drops

### Hornet Predation Pressure and Defence (Bee-Carpet)
- **Date (linear)**: χ² = 37.38, df = 1, P < 0.0001
- **Date² (quadratic)**: χ² = 87.21, df = 1, P < 0.0001
- **Hornet (linear)**: χ² = 22.30, df = 1, P < 0.0001
- **Hornet² (quadratic)**: χ² = 12.10, df = 1, P < 0.001
- **Maximum timing**: Late August-early September
- **Maximum hornet number**: 7 hornets

### Anecdotic Behaviors
- **Honeybees tracking hornets**: 
  - H1: 21 instances
  - H2: 46 instances
  - Binomial test: P < 0.01 (significant)
- **Balling behavior**: 
  - H1: 2 occurrences
  - H2: 1 occurrence
  - Total: 3 occurrences
  - Binomial test: P > 0.05 (not significant)
- **Balling circumstances**: Hornet flying too close from bee-carpet, was engulfed and killed

### Additional Quantitative Findings
- **V. velutina nests**: 6 nests identified within radius of 1 km from hives
- **Maximum hornets observed**: Up to 20 hornets at same time in this experiment
- **Daily visits estimate**: 360 hornets visiting daily the apiary (six hives) at beginning of summer predation (Monceau et al. 2014b)
- **Colony survival**: H1 passed away first before winter; H2 survived longer but finally died later in winter due to reduction of colony size
- **Hive differences**: H2 adopted more offensive strategy (higher number of hornets tracked by honeybees)

### Funding
- **Funding source**: FranceAgriMer (grant #797/2007-2010)
- **Additional funding**: Fondation pour la Recherche sur la Biodiversité (Wasprey project)
- **Core budgets**: CNRS, IRD, INRA SPE department

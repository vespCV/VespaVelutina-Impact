# QUANTITATIVE DATA EXTRACTION - Monceau et al. 2013 (Native Prey)

## Template-Relevant Data

### Study Identification
- **Author**: Monceau, K.
- **Publication Year**: 2013
- **Title**: Native Prey and Invasive Predator Patterns of Foraging Activity: The Case of the Yellow-Legged Hornet Predation at European Honeybee Hives
- **Journal**: PLOS ONE
- **DOI**: 10.1371/journal.pone.0066492

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
- **in_apis_other_behavior**: 0
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
- **n_vespa_nests**: At least 6 nests within 1 km
- **n_vespa_velutina**: Not specified (monitored via video)
- **distance_hornets_nest**: Within 1 km

### Outcomes
- **outcome_apis_predation**: Maximum captures at 9 hornets per hive. Captures increased from July to mid-September then decreased. Peak at midday (01:00-02:00 pm)
- **outcome_predation_time_of_the_day**: Peak captures between 01:00-02:00 pm. Number of hornets did not vary during day, but capture efficacy increased at midday
- **outcome_apis_behavior_foraging**: Flying activity higher early morning, decreased afternoon/evening. Higher in July, decreased throughout summer until October. Negatively related to number of hornets
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Not specified

## All Other Quantitative Data

### Study Details
- **Study period**: June-November 2009
- **Study year**: 2009 (fourth season after first detection of V. velutina in area)
- **Location**: Experimental apiary (INRA, Villenave d'Ornon, France)
- **GPS coordinates**: N 44°47'31.26", W 0°34'29.99"
- **First hornet observation in area**: 2005
- **Predation period**: Early July to November
- **V. velutina nests**: At least 6 nests detected within 1 km of hives
- **Video recording period**: 19/06/2009 to 23/11/2009
- **Analysis start**: 10/07/2009 (first V. velutina occurrence)
- **Analysis end**: 25/10/2009 (absence of honeybees on hive entrance, presence of hornets inside hives)

### Video Recording Setup
- **Camera type**: Black and white Dragonfly Point Grey
- **Resolution**: 640 × 480
- **Frame rate**: 100 FPS
- **Camera position**: Fixed on mast, 1.50 m above ground, 0.50 m from hive
- **Recording software**: Numeriscope (Viewpoint, France)
- **Recording schedule**: Sunrise to sunset (diurnal insects)
- **Ground preparation**: Homogeneous plywood board below landing board for good detection

### Video Analysis
- **Total footage**: >2000 h of observation per hive
- **Sample days**: 11 sample days (every 10 days, with some postponements)
- **Postponed dates**: Second date (20/07) postponed 5 days (25/07), third date (04/08) postponed 2 days (06/08) due to bad weather
- **Excluded sample points**: 2 points at 08:00 am (05/10 and 15/10) due to poor visibility
- **Total sample points**: 139 per hive (mean = 12.64 per day per hive, range: 10-14)
- **Analysis software**: VLC software v. 1.1.11
- **Single analyzer**: LL (to avoid experimenter bias)

### Hornet Behavior Monitoring
- **Monitoring period**: First 5 minutes of each hour
- **Hornet count method**: Maximum number of hornets present at same time during 5-minute sample point
- **Stationary flight positions**: 
  - Front position: 180° sector toward hive entrance
  - Back position: 180° sector away from hive entrance
- **Position analysis time**: 2:00 pm (maximum activity period)
- **Total time spent analysis**: Pooled by sample points for each hive
- **Comparisons available**: 19 (instead of 22) - 3 sample points had no hornet at 02:00 pm (1 for H1, 2 for H2)

### Honeybee Behavior Monitoring
- **Monitoring period**: First 2 minutes of each hour
- **Parameters**: Number of honeybees flying in and out the hive
- **Activity parameter**: Number of flying honeybees (entering hive)
- **Validation**: No difference between leaving and entering for both H1 and H2 (Wilcoxon tests: H1 Z = 2528, P = 0.26, n = 139; H2 Z = 2809, P = 0.24, n = 139)

### Stationary Flight Position Results
- **Time in front position** (1st quartile, median, 3rd quartile): 10.00, 97.00, 152.50 seconds
- **Time in back position** (1st quartile, median, 3rd quartile): 1.50, 8.00, 13.50 seconds
- **Ratio**: Hornets stayed ~10 times longer in front than in back position
- **Statistical test**: Wilcoxon test Z = 188.5, P < 0.001, n sample points = 19
- **Hornets analyzed**: 51 for H1, 41 for H2

### Prey Location at Catching
- **Statistical test**: GLM Poisson family χ² = 25.81, df = 4, P < 0.0001
- **Hive effect**: χ² = 0.23, df = 1, P = 0.63 (not significant)
- **Hive × location interaction**: χ² = 1.58, df = 4, P = 0.81 (not significant)
- **Difference source**: Flying honeybees returning to hive suffered more predation than those guarding hive entrance
- **Wilcoxon multiple comparison**: P = 0.01 (returning foragers vs guards)
- **Other comparisons**: All P > 0.20 (non-significant)

### Relation Between Hornet Number and Honeybee Captures
- **Hive effect**: χ² = 0.35, df = 1, P = 0.55 (not significant)
- **Linear effect of hornet number**: χ² = 27.04, df = 1, P < 0.0001
- **Quadratic effect of hornet number**: χ² = 17.58, df = 1, P < 0.0001
- **Hive × linear interaction**: χ² = 0.40, df = 1, P = 0.53 (not significant)
- **Hive × quadratic interaction**: χ² = 0.52, df = 1, P = 0.47 (not significant)
- **Maximum captures**: Reached when 9 hornets per hive observed
- **Pattern**: Captures increased with number of chasing hornets, reached maximum at 9 hornets, decreased for higher numbers

### Diurnal and Seasonal Variations - V. velutina Predation Pressure
- **Hive effect**: χ² = 2.45, df = 1, P = 0.12 (not significant)
- **Date (linear)**: χ² = 206.84, df = 1, P < 0.0001
- **Date² (quadratic)**: χ² = 96.27, df = 1, P < 0.0001
- **Hour (linear)**: χ² = 0.42, df = 1, P = 0.52 (not significant)
- **Hour² (quadratic)**: χ² = 0.62, df = 1, P = 0.43 (not significant)
- **All interactions**: Not significant (all P > 0.19)
- **Pattern**: Number of V. velutina increased from July to early October then decreased. Did not vary during day. Small number on 15th October due to unfavourable wind conditions

### Diurnal and Seasonal Variations - A. mellifera Flying Activity
- **Hive effect**: χ² = 1.013, df = 1, P = 0.314 (not significant)
- **Date (linear)**: χ² = 0.530, df = 1, P = 0.467 (not significant)
- **Date² (quadratic)**: χ² = 22.092, df = 1, P < 0.0001
- **Hour (linear)**: χ² = 58.400, df = 1, P < 0.0001
- **Hour² (quadratic)**: χ² = 58.464, df = 1, P < 0.0001
- **All interactions**: Not significant (all P > 0.09)
- **Diurnal pattern**: Higher early morning, decreased afternoon and evening
- **Seasonal pattern**: Higher in July, decreased throughout summer until October

### Diurnal and Seasonal Variations - Number of Honeybee Captures
- **Hive effect**: χ² = 1.551, df = 1, P = 0.213 (not significant)
- **Date (linear)**: χ² = 52.230, df = 1, P < 0.0001
- **Date² (quadratic)**: χ² = 46.798, df = 1, P < 0.0001
- **Hour (linear)**: χ² = 29.185, df = 1, P < 0.0001
- **Hour² (quadratic)**: χ² = 31.862, df = 1, P < 0.0001
- **Hive × Hour interaction**: χ² = 5.289, df = 1, P = 0.021 (significant)
- **Hive × Hour² interaction**: χ² = 5.109, df = 1, P = 0.024 (significant)
- **Other interactions**: Not significant (all P > 0.38)
- **Diurnal pattern**: Increased during morning, maximum between 01:00-02:00 pm, then decreased afternoon
- **Seasonal pattern**: Increased from July to mid-September then decreased
- **Hive differences**: Slight difference between H1 and H2 patterns

### Additional Quantitative Findings
- **Forager load**: Pollen or nectar loads can represent up to 40% extra body mass
- **V. crabro:V. velutina ratio**: 1:40 to 1:70 counted in study area (K. Monceau and D. Thiéry, unpublished data)
- **Capture efficiency**: Hornets more efficient at midday sun (maximum captures while hornet number did not increase and not related to honeybee activity variation)

### Statistical Software
- **R version**: 2.10.1 (R Development Core Team 2008)
- **Packages**: epicalc (overdispersion), dispmod (overdispersed Poisson), car (deviance analysis)

### Funding
- **Funding source**: France AgriMer grant #797/2007-2010
- **Additional funding**: Part of Labex COTE (Continental To coastal Ecosystems)
- **Additional support**: Fondation pour la Recherche sur la Biodiversité (Wasprey project)
- **Core budgets**: CNRS, IRD, INRA SPE department

# QUANTITATIVE DATA EXTRACTION - Monceau et al. 2017 (Daily and Seasonal Extranidal)

## Template-Relevant Data

### Study Identification
- **Author**: Monceau, K.
- **Publication Year**: 2017
- **Title**: Daily and Seasonal Extranidal Behaviour Variations in the Invasive Yellow-Legged Hornet, Vespa velutina
- **Journal**: Journal of Insect Behavior
- **DOI**: 10.1007/s10905-017-9607-3

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 0
- **in_other_spec_predation**: 0
- **in_apis_colony_loss**: 0
- **in_apis_foraging**: 0
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
- **start_year**: 2008 (Nest A), 2009 (Nest B)
- **end_year**: 2008 (Nest A), 2009 (Nest B)
- **start_month**: 8
- **end_month**: 11 (Nest A), 12 (Nest B)

### Sample Sizes
- **n_apiaries**: Not specified
- **n_beehives**: Not specified
- **n_vespa_nests**: 2 (Nest A and Nest B)
- **n_vespa_velutina**: Not specified (monitored via video)
- **distance_hornets_nest**: Not specified

### Outcomes
- **outcome_apis_predation**: Not specified
- **outcome_predation_time_of_the_day**: Not specified
- **outcome_apis_behavior_foraging**: Not specified
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Not specified

## All Other Quantitative Data

### Study Details
- **Study period**: August-November (Nest A: 2008), August-December (Nest B: 2009)
- **Location**: Sergeac (Dordogne, France)
- **GPS coordinates**: 45°00'11.3"N, 1°07'09.0"E
- **Altitude**: 88 m
- **Nest collection**: Two undamaged nests collected in southwest France
- **Nest placement**: Inside building with free and unlimited outside access
- **Nest A monitoring**: 2008
- **Nest B monitoring**: 2009
- **Nest B size**: Larger than Nest A (more advanced in development)

### Video Recording Setup
- **Camera type**: Dragonfly Point Grey
- **Resolution**: 640 × 480
- **Frame rate**: 100 FPS
- **Recording software**: Numeriscope (Viewpoint, France)
- **Recording schedule**: Sunrise to sunset (diurnal insects)
- **Filming area**: Only side including nest entrance

### Video Analysis
- **Analysis start**: 8th August for both nests
- **Nest A analysis end**: 25th November (activity completely ceased)
- **Nest B analysis end**: 11th December
- **Nest A sample days**: 23 sample days
- **Nest B sample days**: 22 sample days
- **Sampling frequency**: One sample day every 5 ± 1 days
- **Sample points**: Beginning of each hour, every hour for 5 min during daylight
- **Time range**: Max 08:00 to 20:00 (varies with season)
- **Nest A total sample points**: 195
- **Nest B total sample points**: 215
- **Analysis software**: VLC software v. 2.0.0
- **Single analyzer**: AT (to avoid experimenter effect)

### Activities Monitored
- **Activity 1**: Nest maintenance (working at nest)
- **Activity 2**: Patrolling (getting out nest, walking on nest, returning inside without other activity)
- **Activity 3**: Foraging flight (flying to or out the nest)

### Statistical Analysis
- **Distribution**: Negative binomial (count data)
- **Entrance-exit correlation**: Spearman's rank correlation test
- **Model type**: Negative Binomial Generalized Linear Models (NBGLM)
- **Effects included**: Hour (daily), Date (seasonal), both as simple and quadratic effects
- **Nest identity**: Included as control
- **Test method**: Likelihood ratio-based χ²-statistics for unbalanced design
- **Post-hoc tests**: Wilcoxon pairwise multiple comparison with Benjamini and Hochberg's correction
- **Software**: R v. 3.1.2 (R Core Team 2014)

### Entrance-Exit Correlation
- **Nest A**: ρ = 0.85, P < 0.0001
- **Nest B**: ρ = 0.96, P < 0.0001
- **Analysis**: Only exits considered in subsequent analyses

### Activity Repartition
- **Nest difference**: χ² = 825.82, df = 1, P < 0.0001 (Nest B more numerous)
- **Activity difference**: χ² = 1,140.26, df = 2, P < 0.0001
- **Foraging flight**: More hornets leaving nest in flight compared to nest maintenance and patrolling (post-hoc P < 0.0001 both cases)
- **Nest × Activity interaction**: χ² = 135.07, df = 2, P < 0.0001
  - Nest A: No difference between patrolling and nest maintenance (P = 0.52)
  - Nest B: More individuals in nest maintenance than patrolling (P < 0.0001)

### Nest Maintenance - Daily and Seasonal Variations
- **Date (linear)**: χ² = 155.07, df = 1, P < 0.0001
- **Date² (quadratic)**: χ² = 242.04, df = 1, P < 0.0001
- **Hour (linear)**: χ² = 8.93, df = 1, P < 0.01
- **Hour² (quadratic)**: χ² = 8.53, df = 1, P < 0.01
- **Nest**: χ² = 393.95, df = 1, P < 0.0001
- **Date:Nest**: χ² = 4.84, df = 1, P < 0.05
- **Date²:Nest**: χ² = 7.56, df = 1, P < 0.01
- **Hour:Nest**: χ² = 0.14, df = 1, P = 0.71 (not significant)
- **Hour²:Nest**: χ² = 0.09, df = 1, P = 0.76 (not significant)
- **Daily pattern**: Increased through morning until 14:00, then decreased during afternoon
- **Seasonal pattern**: Increased during summer to reach peak in late September, then decreased during autumn
- **Peak timing difference**: Reached slightly sooner in Nest B than Nest A

### Patrolling - Daily and Seasonal Variations
- **Date (linear)**: χ² = 39.45, df = 1, P < 0.0001
- **Date² (quadratic)**: χ² = 19.06, df = 1, P < 0.0001
- **Hour (linear)**: χ² = 6.04, df = 1, P < 0.05
- **Hour² (quadratic)**: χ² = 5.78, df = 1, P < 0.05
- **Nest**: χ² = 76.67, df = 1, P < 0.0001
- **Date:Nest**: χ² = 10.62, df = 1, P < 0.01
- **Date²:Nest**: χ² = 13.08, df = 1, P < 0.001
- **Hour:Nest**: χ² = 5.12, df = 1, P < 0.05
- **Hour²:Nest**: χ² = 3.96, df = 1, P < 0.05
- **Daily pattern**: Increased through morning until midday, then decreased through afternoon
- **Pattern shift**: Slightly shifted in time for Nest A and B
- **Seasonal pattern**: Increased through summer and autumn
- **Nest A**: Reached peak in early October then decreased
- **Nest B**: Increased through season until late November then decreased

### Foraging Flight - Daily and Seasonal Variations
- **Date (linear)**: χ² = 894.04, df = 1, P < 0.0001
- **Date² (quadratic)**: χ² = 710.47, df = 1, P < 0.0001
- **Hour (linear)**: χ² = 25.84, df = 1, P < 0.0001
- **Hour² (quadratic)**: χ² = 28.4, df = 1, P < 0.0001
- **Nest**: χ² = 2,504.27, df = 1, P < 0.0001
- **Date:Nest**: χ² = 35.37, df = 1, P < 0.0001
- **Date²:Nest**: χ² = 15.07, df = 1, P < 0.001
- **Hour:Nest**: χ² = 6.11, df = 1, P < 0.05
- **Hour²:Nest**: χ² = 5.72, df = 1, P < 0.05
- **Daily pattern**: Increased through morning, reaching peak at mid-day, then decreased during afternoon
- **Peak timing**: 14:00 for Nest A, 13:00 for Nest B
- **Seasonal pattern**: Increased during summer to reach maximum in October
- **Peak timing difference**: Reached earlier in Nest A than Nest B

### Additional Quantitative Findings
- **Colony growth**: Dramatically from June to November
- **Predation period**: Mid-July to late October (Monceau et al. 2013b, c, 2015)
- **Activity similarity**: Both nests showed similar patterns despite different size and monitoring years
- **Time shifts**: Slight shifts in time probably due to environmental (seasonal) variation in weather conditions
- **Activity increase**: All activities increased through summer, reaching peak in early autumn, then decreased until end of colony
- **Nest maintenance decline**: Started decreasing in late September
- **Patrolling continuation**: Continued through November in Nest B (attributed to late emerging individuals)

### Funding
- **Funding source**: Fondation pour la Recherche sur la Biodiversité (FRB, Wasprey project)
- **Additional funding**: France AgriMer (grant #797/2007-2010)
- **Core budgets**: CNRS, IRD, INRA SPE department

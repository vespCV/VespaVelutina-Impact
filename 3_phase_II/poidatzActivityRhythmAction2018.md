# QUANTITATIVE DATA EXTRACTION - Poidatz et al. 2018

## Template-Relevant Data

### Study Identification
- **Author**: Poidatz, J.
- **Publication Year**: 2018
- **Title**: Activity rhythm and action range of workers of the invasive hornet predator of honeybees Vespa velutina, measured by radio frequency identification tags
- **Journal**: Ecology and Evolution
- **DOI**: 10.1002/ece3.4182

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 0 (focus on hornet activity/foraging range, not direct predation)
- **in_other_spec_predation**: 0
- **in_apis_colony_loss**: 0
- **in_apis_foraging**: 1 (indirect - hornet foraging activity)
- **in_apis_other_behavior**: 0
- **in_honey_yield**: 0
- **in_beekeeping_loss**: 0
- **in_management_costs**: 0

### Observation Types
- **type_observation_visual**: 0
- **type_observation_photo**: 0
- **type_observation_video**: 0
- **type_pellets**: 0
- **type_radio_freq**: 1
- **type_CIO_faeces**: 0
- **type_costs**: 0

### Location and Time
- **country**: France
- **start_year**: 2016
- **end_year**: 2016
- **start_month**: 4 (nest collection), monitoring period not specified
- **end_month**: Not specified

### Sample Sizes
- **n_apiaries**: Not applicable (nest study)
- **n_beehives**: Not applicable (nest study)
- **n_vespa_nests**: 1
- **n_vespa_velutina**: 318 individuals released for homing experiment, 71 individuals for activity monitoring
- **distance_hornets_nest**: Release distances: 0, 500, 1000, 2000, 3000, 4000, 5000 m

### Outcomes
- **outcome_apis_predation**: Not directly measured, but foraging range estimated at ~1000 m around nest
- **outcome_predation_time_of_the_day**: Activity peak 2:00-3:00 pm
- **outcome_apis_behavior_foraging**: Not specified
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Not specified

## Other Quantitative Data

### Study Details
- **Nest collection location**: St Médard-en-Jalles (Aquitaine, France)
- **GPS coordinates**: 44°53′35.8″N 0°44′51.4″W (collection), 44°47′30.4″N 0°34′36.9″W (study site)
- **Nest diameter**: 15 cm at collection (28 April 2016)
- **Cage dimensions**: 2 m × 1.5 m × 2 m stainless steel grid cabin

### Homing Ability Experiment
- **Total individuals released**: 318
- **Individuals returning**: 112 (4 excluded from analysis)
- **Homing rate by distance**:
  - 0 m: 83.78% (n=71)
  - 500 m: 90.91% (n=32) - NE: 100%, NW: 75%, SE: 12.5%, SW: 100%
  - 1000 m: 43.75% (n=32) - NE: 37.5%, NW: 50%, SE: 25%, SW: 62.5%
  - 2000 m: 50.00% (n=32) - NE: 62.5%, NW: 37.5%, SE: 62.5%, SW: 37.5%
  - 3000 m: 14.06% (n=64) - NE: 12.5%, NW: 12.5%, SE: 18.8%, SW: 12.5%
  - 4000 m: 21.88% (n=64) - NE: 18.8%, NW: 25%, SE: 25%, SW: 18.8%
  - 5000 m: 4.69% (n=64) - NE: 6.25%, NW: 6.25%, SE: 0%, SW: 6.25%
- **Homing time (mean ± SD)**:
  - 0 m: 2.40 ± 2.01 hr
  - 500 m: 3.91 ± 6.73 hr
  - 1000 m: 8.02 ± 19.17 hr
  - 2000 m: 16.75 ± 12.21 hr
  - 3000 m: 80.11 ± 53.23 hr
  - 4000 m: 77.53 ± 53.34 hr
  - 5000 m: 176.17 ± 118.3 hr
- **Homing speed (mean ± SD, m/hr)**:
  - 500 m: 484.8 ± 596.64
  - 1000 m: 862.17 ± 691.25
  - 2000 m: 375.27 ± 451.97
  - 3000 m: 56.60 ± 39.68
  - 4000 m: 92.17 ± 73.03
  - 5000 m: 36.53 ± 18.53
- **Statistical tests**:
  - Distance effect on return probability: Cox proportional hazard model, χ²=161.69, df=6, P<0.0001
  - Body condition effect: χ²=2.82, df=1, P=0.09 (not significant)
  - Orientation effect: χ²=2.97, df=3, P=0.39 (not significant)
- **Body condition**: Returning hornets lighter (median 284.1 mg, 95% CI: 273.3-294.1) than non-returning (295.8 mg, 95% CI: 286.8-299.9), Wilcoxon rank sum test: W=12,934.5, P=0.01

### Individual Flight Activity (71 individuals)
- **Total trips recorded**: 4,467 trips
- **Activity period**: 4.98 ± 4.44 days per individual (mean ± SD, range: 1-26 days)
- **Trips per day**: 12.62 ± 10.97 trips per day per individual (mean ± SD)
- **Activity hours**: 98% of trips between 7:00 am and 8:00 pm
- **Night trips**: 72 trips excluded from analysis
- **Peak activity time**: 2:00-3:00 pm (Poisson GLM: hours χ²=17.61, df=1, P<0.0001; hours² χ²=15.94, df=1, P<0.0001)
- **Weather effect**: Number of trips increased with higher temperature and lower humidity (NBGLMM: estimate ± SD = 0.15 ± 0.04, Wald test: χ²=13.15, df=1, P<0.001)
- **Individual variation**: Significant differences among individuals (Poisson GLM: χ²=353.85, df=70, P<0.0001)
- **Day effect**: No significant effect (days: χ²=2.53, df=1, P=0.11; days²: χ²=0.55, df=1, P=0.46)

### Trip Duration
- **Short trips (<1 hr)**: 96.4% of trips
- **Short trip duration**: 949.7 ± 750.46 s (mean ± SD, ~15 min 50 ± 12 min 30, range: 68 s to 3,597 s)
- **Long trips (>1 hr)**: 3.60% of trips (range: >1 hr to ~22 hr)
- **Long trip duration**: 84% lasted 60-250 min (mean 99 ± 75 min), 16% lasted average 886 ± 193 min
- **Body mass effect on trip duration**: Not significant (F=0.34, df=1,24, P=0.57)
- **Long trip individuals**: 29 individuals (40% of 71) made at least one long trip
  - 24 individuals: 1-4 long trips
  - 2 individuals: 5-14 long trips
  - 3 individuals: >15 long trips (38, 33, and 23 long trips respectively)

### Foraging Range Estimation
- **Estimated foraging range**: ~1000 m around nest (based on homing ability and trip patterns)
- **Probable territory range**: ~500 m (based on homing rates and activity patterns)

# QUANTITATIVE DATA EXTRACTION - Requier et al. 2019

## Template-Relevant Data

### Study Identification
- **Author**: Requier, F.
- **Publication Year**: 2019
- **Title**: Predation of the invasive Asian hornet affects foraging activity and survival probability of honey bees in Western Europe
- **Journal**: Journal of Pest Science
- **DOI**: 10.1007/s10340-018-1063-0

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 1
- **in_other_spec_predation**: 0
- **in_apis_colony_loss**: 1
- **in_apis_foraging**: 1
- **in_apis_other_behavior**: 1
- **in_honey_yield**: 0
- **in_beekeeping_loss**: 0
- **in_management_costs**: 0

### Observation Types
- **type_observation_visual**: 1
- **type_observation_photo**: 0
- **type_observation_video**: 1
- **type_pellets**: 0
- **type_radio_freq**: 0
- **type_CIO_faeces**: 0
- **type_costs**: 0

### Location and Time
- **country**: France
- **start_year**: 2012
- **end_year**: 2016
- **start_month**: 7
- **end_month**: 12

### Sample Sizes
- **n_apiaries**: 75
- **n_beehives**: 131 colonies
- **n_vespa_nests**: Not specified
- **n_vespa_velutina**: 0-20 hornets observed simultaneously at beehive entrances
- **distance_hornets_nest**: Not specified

### Outcomes
- **outcome_apis_predation**: Hornet loads 0-20 at beehive entrances. Complete foraging paralysis expected for ≥12.6 hornets. Homing failure (HF) dependent on flight activity
- **outcome_predation_time_of_the_day**: Hornet activity 9:06-18:08 (video surveillance)
- **outcome_apis_behavior_foraging**: Foraging paralysis (FP) - flight activity negatively impacted by hornet loads (Z=-20.65, P<0.001). Complete FP at ≥12.6 hornets
- **outcome_other_apis_behavior**: Foraging paralysis behavioral response
- **outcome_apis_behavior_paralysis**: Yes - foraging paralysis (FP) observed

## Other Quantitative Data

### Study Details
- **Visual observations**: 603 observations from 2012-2016
- **Observation duration**: 17 min per observation (15 min hornet monitoring, 2 min bee activity)
- **Video surveillance**: 90 hours total (10 consecutive days, 9-18h daily, October 16-25, 2015)
- **Video location**: La Rochelle (46°8′N, 1°8′W), 200 km from introduction point
- **Video slots**: 255 slots of 15 min
- **Trajectories extracted**: 603,259 total trajectories
- **Hornet trajectories**: 5,181
- **Predator-prey interactions**: Video segments with both hornet and bee present
- **Successful predation events**: 126 recorded

### Visual Survey Methodology (Foraging Paralysis Assessment)
- **Observation protocol**: 17 min visual observation per colony
- **Observer distance**: 3-5 m from beehive entrances
- **Single observer**: All observations carried out by one person to mitigate observer effect
- **First 15 minutes**: Record maximum number of hornets hovering in front of beehive at the same time
- **Last 2 minutes**: Count number of returning bees (flight activity assessment)
- **Hornet counting method**: Maximum number of hornets visible simultaneously (to avoid pseudo-replication)
- **Total colonies observed**: 131 colonies across 75 apiaries
- **Observation period**: July to December (2012-2016), during complete hornet predation period
- **Foraging paralysis calculation**: Relative flight activity compared to maximum level of flight activity

### Video Surveillance Methodology (Homing Failure Assessment)
- **Camera type**: Stereovision camera (G3 Evo 3, TYZX®)
- **Camera position**: 50 cm above flight board of beehive
- **Camera rationale**: Non-trivial trade-off between device intrusiveness, image definition (at least 8 pixels per bee), and observed volume (must include at least 50 cm wide flight board)
- **Recording period**: October 16-25, 2015 (peak predation period)
- **Daily recording**: 9:00-18:00 h (diurnal insects), 10 consecutive days without interruption
- **Total recording time**: 90 hours
- **Analysis unit**: 15-min slots (n = 255 slots)
- **Trajectory extraction**: All insects flying in front of beehive tracked using RGB-D images
- **Trajectory classification**: Bees vs hornets distinguished using clustering approach based on flight dynamics (e.g., max speed) and appearance features (e.g., body size)
- **Predation detection**: Each video slot with both hornet(s) and honey bee(s) manually reviewed twice
- **Predation success criteria**: Hornet catches bee and flies away with caught prey within video screen limit (about 1.5 m² around beehive entrance)
- **Unclear events**: Excluded from analysis
- **Homing failure calculation**: Ratio of number of bees caught to total number of incoming bee trajectories per 15-min slot

### Foraging Paralysis (FP)
- **Hornet load range**: 0-20 hornets simultaneously hovering
- **Peak period**: August 28 - November 6 (hornets >5 only during this period)
- **Statistical model**: GLMM with Poisson error structure
- **Effect**: Negative impact on flight activity (Z=-20.65, P<0.001)
- **Complete FP threshold**: ≥12.6 hornets (95% CI prediction)
- **FP expression**: Percent flight activity relative to maximum value

### Homing Failure (HF)
- **Dependence**: Significantly dependent on flight activity (Z=-5.37, P<0.001)
- **Pattern**: Maximal under very low flight activity, decreases with increased flight activity
- **Video surveillance**: HF probability estimated as ratio of bees caught to total incoming bee trajectories per 15-min slot

### BEEHAVE Model Simulations
- **Total simulations**: 1,000
- **Simulations excluded**: 7 (reached endpoint before hornet impact period)
- **Remaining simulations**: 993
- **Collapse rate**: 55.3% (549/993) reached endpoint
- **Collapse during predation period**: 24 colonies (2.5%)
- **Collapse during winter**: January 13 - May 1
- **Impact period**: Day 240 (August 28) to day 310 (November 6)
- **Parameters varied**:
  - Maximal foraging distance: 7299 km/day (default) down to 0
  - Forager mortality rate: 1.00e-05 (default) to 2.00e-05 per second

### Low Hornet Loads (<13.3 hornets)
- **Simulations**: 657 (high food storage availability >0.5 g per bee)
- **Path analysis**: Fisher's C=1.68, k=32, P=0.432 (consistent causal links)
- **Mechanism**: HF decreases adult population size → winter mortality by depopulation
- **Key effects**:
  - Negative effect of hornet loads on honey reserve and adult population
  - Honey and pollen stores negatively affected by adult population increase
  - Larvae population positively affected by adult population increase
  - Winter survival: Direct effect of adult population size (larger = better survival)
  - Pollen storage at end of impact period positively correlated with winter survival

### High Hornet Loads (>13.3 hornets)
- **Simulations**: 336 (reduced food storage availability <0.5 g per bee)
- **Path analysis**: Fisher's C=2.45, k=32, P=0.293 (consistent causal links)
- **Mechanism**: FP increases population size → food reserve depletion → winter mortality
- **Key effects**:
  - Positive effect of hornet loads on adult population, larvae population, pollen storage
  - Negative effect on honey reserves
  - Increase in adult population → negative effect on honey and pollen reserves
  - Increase in adult population → negative effect on larvae population
  - Larvae population positively correlated with pollen and honey reserves
  - Winter survival: Improved by honey reserves, negatively affected by hornet loads

### Risk Profiles (Conditional Inference Tree)
- **Profile A (n=27, χ²=28.78, P<0.001)**: Larvae population <5 individuals → 100% winter mortality
- **Profile B (n=288, χ²=72.32, P<0.001)**: Larvae >5, adult population <9950 → 80.5-96.8% mortality
- **Profile C (n=66, χ²=11.72, P=0.004)**: Larvae >5, adult >9950, honey reserve ≤21 kg → 100% mortality
- **Profile A changes**: Larvae population decreased, adult population increased (+4874), honey reserves decreased (-26.8 kg)
- **Profile B changes**: Larvae decreased, adult population decreased (-19,732), honey reserves increased (+12.3 kg)
- **Profile C changes**: Intermediary population and reserve trajectories

### Temporal Patterns
- **Hornet activity period**: July to December
- **Peak activity**: September-October
- **Daily activity**: 9:06-18:08 (video surveillance)
- **Hornet trajectories per day**: 0-152 tracked flight trajectories

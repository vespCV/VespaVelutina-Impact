# QUANTITATIVE DATA EXTRACTION - Requier et al. 2020

## Template-Relevant Data

### Study Identification
- **Author**: Requier, F.
- **Publication Year**: 2020
- **Title**: A biodiversity-friendly method to mitigate the invasive Asian hornet's impact on European honey bees
- **Journal**: Journal of Pest Science
- **DOI**: 10.1007/s10340-019-01159-9

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
- **type_observation_video**: 0
- **type_pellets**: 0
- **type_radio_freq**: 0
- **type_CIO_faeces**: 0
- **type_costs**: 0

### Location and Time
- **country**: France
- **start_year**: 2013
- **end_year**: 2016
- **start_month**: 7
- **end_month**: 12

### Sample Sizes
- **n_apiaries**: 22 sites
- **n_beehives**: 44 colonies (22 pairs: 22 muzzle-equipped, 22 control)
- **n_vespa_nests**: Not specified
- **n_vespa_velutina**: 0-20 hornets observed simultaneously
- **distance_hornets_nest**: Not specified

### Outcomes
- **outcome_apis_predation**: Hornet loads 0-20. Muzzle did not reduce HF, but drastically reduced FP
- **outcome_predation_time_of_the_day**: Observations 9:30 am to 6:30 pm
- **outcome_apis_behavior_foraging**: FP reduced up to 41% with muzzle. Muzzle-equipped: 84-76% of baseline activity (16-24% FP). Control: 100-35% (0-65% FP)
- **outcome_other_apis_behavior**: Foraging paralysis (FP) behavioral response
- **outcome_apis_behavior_paralysis**: Yes - foraging paralysis observed, reduced by muzzle

## Other Quantitative Data

### Study Details
- **Study period**: 2013-2016
- **Sites**: 22 sites with confirmed hornet presence (≥4 years)
- **Apiary size**: 2-10 colonies per apiary
- **Colony selection**: Similar structure (population, honey reserve), same hive type (Dadant), same color
- **Colony distance**: ≥5 m apart or at both ends of apiary
- **Muzzle installation**: 2 weeks before first observation
- **Total observations**: 388 (194 muzzle-equipped, 194 control)
- **Observation duration**: 17 min (15 min hornet monitoring, 2 min bee activity)
- **Observation distance**: 3-5 m from beehive entrance
- **Observation times**: Random during daily flight activity (9:30 am - 6:30 pm)
- **Paired observations**: Both colonies observed within same hour

### Beehive Muzzle Specifications
- **Material**: Metal wire mesh, 6 mm square shape
- **Backing**: Plywood
- **Protection distance**: 25 cm in front of hive
- **Function**: Bees can crawl through mesh, hornets cannot
- **Cost**: <15 € per homemade muzzle (material + construction time)
- **Installation period**: Start of predation period (mid-August in France) to before spring

### Foraging Paralysis (FP) Results
- **Statistical model**: GLMM with Poisson error structure
- **Muzzle effect**: Estimate=-0.177, SE=0.021, Z=-8.310, P<0.001
- **Hornet effect**: Estimate=-0.043, SE=0.005, Z=-11.537, P<0.001
- **Muzzle × Hornet interaction**: Estimate=0.047, SE=0.006, Z=7.964, P<0.001
- **FP reduction**: Up to 41% with muzzle
- **Muzzle-equipped colonies**: 84-76% of baseline activity (16-24% FP) with 0-20 hornets
- **Control colonies**: 100-35% of baseline activity (0-65% FP) with 0-20 hornets
- **95% CI prediction**: Control colonies can reach up to 76% FP

### Homing Failure (HF) Results
- **Statistical model**: Binomial GLMM with logit-link function
- **Muzzle effect**: Estimate=-0.115, SE=0.148, Z=0.778, P=0.436 (not significant)
- **Bee activity effect**: Estimate=-0.147, SE=0.009, Z=-15.930, P<0.001
- **Muzzle × Bee activity interaction**: Estimate=0.001, SE=0.013, Z=0.108, P=0.914 (not significant)
- **Conclusion**: Muzzle did not affect HF. HF maximal under low flight activity, decreases with increased flight activity, independently of muzzle

### BEEHAVE Model Simulations
- **Total simulations**: 200 (100 muzzle-equipped, 100 control)
- **Simulations excluded**: 3 (collapsed before hornet impact period)
- **Remaining simulations**: 197
- **Collapse during impact period**: 0 colonies
- **Collapse during winter**: January 13 - May 1
- **Impact period**: Day 240 (August 28) to day 310 (November 6)
- **Muzzle parameterization**:
  - Maximal daily foraging distance: 2900 km/day (84% of default 3450) down to 2000 km/day (76%)
  - Forager mortality probability: 1.00e-05 (default) to 1.35e-05 per second
- **Control parameterization**:
  - Maximal daily foraging distance: Default down to 1.7 km/day (minimal without complete stop)
  - Forager mortality probability: 1.00e-05 to 1.35e-05 per second
- **Hornet levels simulated**: 0-20 hornets simultaneously predating

### Survival Probability Results
- **Muzzle-equipped survival rate**: 55%
- **Control survival rate**: 35%
- **Statistical test**: Linear model, F=14.38, R²=0.43, P=0.001
- **Survival increase**: Up to 51% in context of high hornet abundance (>5 hornets)
- **Low hornet loads (<5)**: Muzzle survival marginally lower than control
- **High hornet loads (>5)**: Muzzle significantly increases survival probability

### Statistical Power Analysis
- **Honey bee coefficient of variation**: 70.9%
- **Hornet coefficient of variation**: 87.3%
- **Sample size**: 194 observations per treatment
- **Detectable effect sizes**: 20% (honey bees), 25% (hornets) with power 1-β=0.8

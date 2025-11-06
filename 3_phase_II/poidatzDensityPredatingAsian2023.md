# QUANTITATIVE DATA EXTRACTION - Poidatz et al. 2023

## Template-Relevant Data

### Study Identification
- **Author**: Poidatz, J.
- **Publication Year**: 2023
- **Title**: Density of predating Asian hornets at hives disturbs the 3D flight performance of honey bees and decreases predation success
- **Journal**: Ecology and Evolution
- **DOI**: 10.1002/ece3.9902

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
- **start_year**: Not specified
- **end_year**: Not specified
- **start_month**: Not specified
- **end_month**: Not specified

### Sample Sizes
- **n_apiaries**: 1
- **n_beehives**: 1
- **n_vespa_nests**: Not specified
- **n_vespa_velutina**: Variable (monitored via video)
- **distance_hornets_nest**: Not specified

### Outcomes
- **outcome_apis_predation**: Predation success 2.4% of recorded interactions (126 successful events out of 5,175 interactions). Success 4x higher for bees entering hive (69.46%) vs leaving (15.27%). Peak success at ~8 hornets, then decreases
- **outcome_predation_time_of_the_day**: Peak hornet activity at 1 pm, peak honey bee activity at 3 pm
- **outcome_apis_behavior_foraging**: Flight speed and curvature affected by hornet density. Bees entering hive: speed and curvature increase with hornet density. Bees leaving hive: speed decreases with hornet density
- **outcome_other_apis_behavior**: Flight performance changes with hornet density. Hovering behavior differs between bees entering/leaving and hornets
- **outcome_apis_behavior_paralysis**: Not explicitly stated, but reduced foraging activity suggested

## Other Quantitative Data

### Study Details
- **Total trajectories extracted**: 603,259
- **Predator-prey interactions**: 5,175
- **Successful predation events**: 126 (2.4% of interactions)
- **Video analysis**: Automated 3D trajectory analysis using stereo vision
- **Observation hours**: 90 hours reduced to scenes of interest

### Daily Activity Patterns
- **Hornet activity peak**: 1 pm (GAM: F=22.9, P<0.001)
- **Honey bee activity peak**: 3 pm (GAM: F=25.95, P<0.001)
- **Activity pattern**: Nonlinear, quadratic patterns for both species

### Flight Performance - Speed
- **Honey bees leaving hive**: 1.9x faster than bees entering hive
- **Honey bees entering hive**: 1.25x faster than hornets
- **Statistical test**: Kruskal-Wallis χ²=78,018, df=2, P<0.001; Pairwise Wilcoxon test, P<0.001
- **Daily pattern**: 
  - Hornets: Increase until 11 am (GAM: F=7.297, P<0.001)
  - Bees entering: Increase until 2 pm (GAM: F=2.327, P<0.001)
  - Bees leaving: Increase until 2 pm (GAM: F=16.34, P<0.001)

### Flight Performance - Curvature
- **Bees leaving hive**: Straighter trajectories than bees entering
- **Bees entering hive**: Straighter than hornets
- **Statistical test**: Kruskal-Wallis χ²=41,384, df=2, P<0.001; Pairwise Wilcoxon test, P<0.001
- **Daily pattern**:
  - Bees entering: Increase until 2 pm (GAM: F=12.29, P<0.001)
  - Hornets: Positive trend (GAM: F=9.263, P=0.003)
  - Bees leaving: Positive trend (GAM: F=17.03, P<0.001)

### Flight Performance - Hovering
- **Hornets**: 2.1x more hovering time than bees entering hive
- **Statistical test**: Pairwise Wilcoxon test, P<0.001; Kruskal-Wallis χ²=27,949, df=2, P<0.001
- **Hovering categories** (hornets, threshold 2 = 10 mm displacement):
  - Small group: ~10% of flight time hovering
  - Large group: ~90% of flight time hovering
- **Daily pattern**:
  - Hornets: Decrease until 2 pm, then increase (GAM: F=6.19, P<0.001)
  - Bees entering: Variable (GAM: F=13.56, P<0.001)
  - Bees leaving: Increase over day (GAM: F=58.01, P<0.001)

### Predation Success
- **Overall success rate**: 2.4% (126/5,175 interactions)
- **Success by bee direction**:
  - Bees entering hive: 69.46%
  - Bees leaving hive: 15.27%
  - Neither category: 15.27%
- **Peak success**: ~8 hornets (quadratic relationship)
- **Statistical model**: Binomial GLMM
  - Number of hornets (linear): estimate=0.432±0.248, Z=1.743, P=0.0813
  - Number of hornets² (quadratic): estimate=-0.036±0.008, Z=-4.65, P<0.001
  - Multimodel average: hornets estimate=0.492±0.045, hornets² estimate=-0.035±0.001, relative importance=0.781
- **Non-significant factors**: Time, number of honey bees, interactions

### Flight Performance vs Predation Success
- **Hornet flight speed**: No difference between successful/unsuccessful (Kruskal-Wallis χ²=0.44, df=2, P=0.80)
- **Hornet hovering**: No difference (Kruskal-Wallis χ²=0.32, df=2, P=0.85)
- **Hornet curvature**: No difference (Kruskal-Wallis χ²=1.71, df=2, P=0.43)
- **Bee flight speed**: No difference (Kruskal-Wallis χ²=2.26, df=2, P=0.32)
- **Bee hovering**: No difference (Kruskal-Wallis χ²=0.93, df=2, P=0.63)
- **Bee curvature**: Significantly lower in successful predation (Kruskal-Wallis χ²=11.10, df=2, P=0.005) - straighter trajectories more vulnerable

### Impact of Hornet Density on Flight Performance
- **Bees entering hive - Speed**: Positive effect (LM: estimate=0.0483±0.011, F=19.36, P<0.001)
- **Bees entering hive - Curvature**: Positive effect (LM: estimate=0.1888±0.024, F=59.74, P<0.001)
- **Bees entering hive - Hovering**: No significant effect (LM: estimate=0.0064±0.009, F=0.484, P=0.4873)
- **Bees leaving hive - Speed**: Negative effect (LM: estimate=-0.061±0.029, F=4.617, P=0.0324)
- **Bees leaving hive - Curvature**: No significant effect (LM: estimate=-0.030±0.370, F=0.007, P=0.9356)
- **Bees leaving hive - Hovering**: Marginally non-significant (LM: estimate=0.021±0.012, F=3.167, P=0.0761)
- **Hornets - Speed**: No significant effect (LM: estimate=0.020±0.033, F=0.352, P=0.5532)
- **Hornets - Curvature**: No significant effect (LM: estimate=-0.693±0.6116, F=1.285, P=0.2580)
- **Hornets - Hovering**: No significant effect (LM: estimate=0.0007±0.028, F=0.0006, P=0.9798)
- **Variance reduction**: Hornet density strongly reduced variance in all parameters for bees and hornets

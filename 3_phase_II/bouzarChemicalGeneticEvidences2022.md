# QUANTITATIVE DATA EXTRACTION - Bouzar et al. 2022

## Template-Relevant Data

### Study Identification
- **Author**: Bouzar, C.
- **Publication Year**: 2022
- **Title**: Chemical and genetic evidences that multiple hornet colonies attack honeybee colonies
- **Journal**: Insectes Sociaux
- **DOI**: 10.1007/s00040-022-00853-9

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 1 (indirect - study of hornet colonies attacking apiaries)
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
- **type_observation_video**: 0
- **type_pellets**: 0
- **type_radio_freq**: 0
- **type_CIO_faeces**: 0
- **type_costs**: 0

### Location and Time
- **country**: France (Indre-et-Loire department)
- **start_year**: 2015
- **end_year**: 2016
- **start_month**: 5 (May)
- **end_month**: 10 (October)

### Sample Sizes
- **n_apiaries**: 4 apiaries (second campaign)
- **n_beehives**: Not specified
- **n_vespa_nests**: 27 nests (first campaign)
- **n_vespa_velutina**: 188 hornets collected from 4 apiaries (171 in final dataset after exclusions)
- **distance_hornets_nest**: 1.5-4 km between apiaries

### Outcomes
- **outcome_apis_predation**: Not directly measured (study focuses on hornet colony identification)
- **outcome_predation_time_of_the_day**: Not specified
- **outcome_apis_behavior_foraging**: Not specified
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Not specified

## Other Quantitative Data

### Genetic Analysis
- **Microsatellite markers**: 13 markers (10 used after exclusions)
- **Excluded markers**: D2-142, R1-77 (monomorphic), R4-26 (unreadable)
- **Total individuals genotyped**: 315 hornets
- **Multiplex assays**: 3-plex
  - Multiplex 1: R1-36, D2-185, R1-75, R1-169
  - Multiplex 2: R4-114, R4-26, D2-142, R4100, D3-15
  - Multiplex 3: R1-80, R1-77, R4-33, R1-137

### Chemical Analysis
- **CHC compounds detected**: 71 compounds
- **Main compounds analyzed**: 18 compounds (relative abundance ≥1%)
- **Extraction method**: Washing in 1 ml heptane for 2 × 1 min
- **Internal standard**: n-C20 (10 μg/ml, n-eicosane)
- **GC system**: CPG Agilent Technologies 7820A with FID
- **Column**: HP-5 Agilent Technology (30 m × 0.32 mm × 0.25 μm)

### Statistical Analysis
- **Distance metric**: Nei distance (modified for CHC)
- **Clustering**: K-means clustering
- **Software**: R v. 3.3.3
- **Packages**: FactoMineR, Rcmdr, factoextra, ggplot2, adegenet
- **Structure analysis**: Structure Harvester v. 0.6.94
- **MCMC simulations**: 100,000 (burn-in: 10,000)

### Results
- **Chemical variation**: At least 2 chemically homogeneous groups per apiary
- **Dissimilarity levels**:
  - Within apiaries: Intermediate
  - Within colonies: Lower
  - Between colonies: Higher
- **Genetic diversity**: Low at population level (as expected for introduced species)
- **Genetic dissimilarity**: Mirrored chemical results (intermediate within apiaries)

## Other Quantitative Data

### DNA Extraction
- **Tissue used**: Two antennae and right mesothoracic leg
- **Method**: Wizard® Genomic Purification Kit (Promega)
- **Grinding**: Pestle after immersion in liquid nitrogen

### PCR Conditions
- **Taq DNA polymerase**: 0.5 U
- **dNTP**: 6 pmol
- **MgCl₂**: 37.5 pmol
- **DNA dilution**: 1/5
- **Primers**: 1 μl
- **Fluorochromes**: 6-FAM, NED, VIC, PET
- **Thermocycling**:
  - Initial denaturation: 95°C for 10 min
  - 40 cycles: 95°C for 30s, 50°C for 30s, 72°C for 1 min
  - Final extension: 72°C for 10 min

### Sequencing
- **System**: ABI 3730XL (Applied Biosystems)
- **Size standard**: GeneScan™ 500LIZ®
- **Genotyping software**: Geneious 9.4

### GC Temperature Program
- **Step 1**: 50-200°C at 8°C/min
- **Step 2**: 200-315°C at 5°C/min
- **Step 3**: 315°C hold for 5 min
- **Carrier gas**: Helium (1.7 ml/min)

### Sampling Period Rationale
- **Second campaign timing**: September-October (period of significant predation activity)
- **Nest density**: Usually peaks in autumn
- **Predation intensity**: Greatly intensifies between early August and early November

### Analysis Methods
- **PCA**: Principal component analysis
- **DAPC**: Discriminant analysis of principal components
- **Structure analysis**: Admixture model
- **Optimal K**: Calculated using Evanno method

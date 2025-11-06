# Quantitative Data: Pedersen et al. 2025

## Template-Relevant Data

### Study Design
- **Countries**: Jersey (Channel Islands), France (Aquitaine), Spain (Galicia), United Kingdom
- **Start year**: 2020
- **End year**: 2022
- **Number of nests**: 103 nests
- **Number of larval samples**: 1,545 samples
- **Average larvae per nest**: 15 (range: 1-30)
- **Nest distribution**:
  - Jersey: 68 nests
  - Aquitaine: 25 nests
  - Galicia: 8 nests
  - UK: 2 nests

### DNA Sequencing
- **Sequencing platform**: Illumina NovaSeq 6000
- **Target gene**: COI (cytochrome c oxidase subunit I)
- **Primers**: mlCOIintF and HCO2198
- **Total reads obtained**: 129 million reads
- **Average reads per sample**: 84,000 reads
- **Total OTUs detected**: 1,449 OTUs
- **Species-level identification**: 55.1% of OTUs (86.3% of reads)

### Prey Diversity
- **Total orders detected**: 26 orders
- **Arthropod orders**: 7 orders accounted for 86.7% of all OTUs
  - Diptera: 561 OTUs (most diverse)
  - Hymenoptera: 252 OTUs
  - Lepidoptera: 169 OTUs
  - Coleoptera: 137 OTUs
  - Hemiptera: 84 OTUs
  - Orthoptera: 70 OTUs
  - Araneae: 53 OTUs

### Prey Prevalence by Order
- **Hymenoptera**: Average prevalence 99.5%
- **Diptera**: Average prevalence 94.0%
- **Coleoptera**: Average prevalence 40.3%
- **Lepidoptera**: Average prevalence 38.9%
- **Araneae**: Average prevalence 27.3%
- **Hemiptera**: Average prevalence 26.1%
- **Orthoptera**: Average prevalence 9.5%

### Most Frequently Predated Species
- **Apis mellifera**: Found in every nest, average prevalence 98.1%
- **Vespula vulgaris**: Found in 75.7% of nests, average prevalence 52.2%
- **Calliphora vicina**: Found in 77.7% of nests, average prevalence 51.7%

### Functional Groups
- **Top 50 prey species**: 43 were potential pollinators (flowervisitors as adults)
- **Crop pollinators**: 3 of the most dominant European crop pollinators (A. mellifera, Bombus terrestris, Bombus lapidarius)
- **Crop pests**: 4 well-known crop plant pests identified
- **Recyclers**: 17 of top 50 species were recyclers (saprophages or sarcophages)

### IUCN Red List
- **Species compared**: 749 arthropods identified to species level
- **Matches with IUCN Red List**: 20 species
- **Near threatened**: 2 species (Epeolus cruciger, Platycheirus fasciculatus)
- **Data deficient**: 1 species
- **Least concern**: 17 species

### Larval Gut Richness
- **Range**: 1-71 OTUs per larva
- **Mode**: 15 OTUs
- **Mean**: 16.4 OTUs
- **Regional differences**: Galicia and Aquitaine had higher richness than Jersey and UK
- **Year differences**: 2021 had higher richness than 2020 and 2022

### Apiary Proximity Analysis (Jersey only)
- **Number of apiaries within 500m**: Correlated with honeybee RRA (tau = 0.145, p < 0.001)
- **Distance to nearest apiary**: Correlated with honeybee RRA (tau = 0.07, significant)

## Other Quantitative Data

### Nest Stages
- **Embryo nests**: 11 nests
- **Small nests**: 44 nests
- **Large nests**: 37 nests
- **Unassigned**: 11 nests

### Land Cover Analysis
- **Radius analyzed**: 500 m around each nest
- **Land cover classes**: 8 classes (tree cover, shrubland, grassland, cropland, built-up areas, bare ground, water bodies, wetland)
- **Nests without GPS data**: 6 nests (4 from Aquitaine, 2 from Galicia)

### Statistical Models
- **GLMM**: Generalized linear mixed model with Poisson distribution
- **Samples included**: 1,346 larvae from 89 nests (14 nests excluded due to missing data)
- **db-RDA**: Distance-based redundancy analysis
- **Significant factors**: Region, month, year, built-up land cover, nest stage, head width

### Seasonal Patterns
- **Early season**: April, May, June
- **Mid-season**: July, August, September
- **Late season**: October, November
- **Peak activity month**: September (used for regional comparisons)

### Geographic Variation
- **Species richness**: Higher in southern latitudes (Galicia, Aquitaine)
- **Dietary composition**: Varied significantly by region, month, year, and built-up land cover

### Nest Attributes
- **Head width**: Used as age proxy for larvae
- **Interaction**: Nest stage × head width interaction significant for prey diversity

### Mock Community
- **Species included**: 13 species
- **Detection**: All 13 species detected in every positive control
- **Contamination**: One unidentified mite detected in two samples

### Data Quality Control
- **Samples discarded**: Those with ≤15,000 reads
- **OTU filtering**: OTUs with <50 reads in entire dataset removed
- **Negative controls**: Used to set minimum read thresholds

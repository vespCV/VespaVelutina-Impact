# Quantitative Data: Bouzar et al. 2022

## Template-Relevant Data

### Study Design
- **Country**: France (Indre-et-Loire department)
- **Sampling campaigns**: 2 campaigns
- **First campaign**: May-October 2015
- **Second campaign**: September-October 2016

### Sample Collection
- **First campaign - Nests collected**: 27 nests
- **First campaign - Population level**: 27 individuals (1 per nest)
- **First campaign - Colony level**: 5 entire colonies, 20 workers per colony (100 individuals)
- **Second campaign - Hornets collected**: 188 hornets from 4 apiaries
- **Second campaign - Hornets per apiary**: 47 per apiary
- **Final dataset**: 171 hornets (17 excluded: 9 triploid, 8 with amplification issues)
- **Final distribution**: Apiary 1: 46, Apiary 2: 42, Apiary 3: 41, Apiary 4: 42

### Geographic Distribution
- **Apiary distances**: 1.5-4 km between apiaries
- **Location**: Indre-et-Loire department, France

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

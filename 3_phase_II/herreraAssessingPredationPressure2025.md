# QUANTITATIVE DATA EXTRACTION - Herrera et al. 2025

## Template-Relevant Data

### Study Identification
- **Author**: Herrera, C.
- **Publication Year**: 2025
- **Title**: Assessing predation pressure of Vespa velutina on wild pollinators through DNA metabarcoding of meconium
- **Journal**: Journal of Zoology
- **DOI**: 10.1111/jzo.70033

### Exclusion/Inclusion Criteria
- **ex_editorial**: 0
- **ex_review**: 0
- **ex_no_data**: 0
- **ex_gray**: 0
- **ex_no_pdf**: 0
- **in_apis_predation**: 1 (Apis mellifera found in diet)
- **in_other_spec_predation**: 1 (diverse prey species identified)
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
- **type_CIO_faeces**: 1 (meconium analysis)
- **type_costs**: 0

### Location and Time
- **country**: Spain (Mallorca, Balearic Islands)
- **start_year**: 2016
- **end_year**: 2016
- **start_month**: Not specified
- **end_month**: Not specified

### Sample Sizes
- **n_apiaries**: Not applicable (study of hornet nests)
- **n_beehives**: Not applicable
- **n_vespa_nests**: 7 nests
- **n_vespa_velutina**: Not specified
- **distance_hornets_nest**: Not specified

### Outcomes
- **outcome_apis_predation**: Yes - Apis mellifera identified in prey composition (22.55% of Apidae family)
- **outcome_predation_time_of_the_day**: Not specified
- **outcome_apis_behavior_foraging**: Not specified
- **outcome_other_apis_behavior**: Not specified
- **outcome_apis_behavior_paralysis**: Not specified

## Other Quantitative Data

### DNA Sequencing
- **Sequencing platform**: Illumina MiSeq V3
- **Target gene**: COI (cytochrome c oxidase subunit I)
- **Primers**: ZBJ-ArtF1c, ZBJ-ArtR2c, ApisF, Vespa_blockR
- **Total samples sequenced**: 97 (90 meconium, 4 duplicates, 2 blanks, 1 negative control)
- **Total reads after filtering**: 79,844 reads
- **Average reads per sample**: 918 reads (range: 64-2,884)
- **Distinct COI sequences**: 338 sequences

### Prey Identification
- **Total OTUs identified**: 102 OTUs
- **Taxonomic levels**:
  - 7 orders
  - 29 families
  - 27 genera
  - 19 species
- **OTUs per sample**: 1-15 OTUs
- **Total OTUs per nest**: 16-31 OTUs

### Prey Composition
- **Shared OTUs across all nests**: 2 OTUs (1.96% of total)
  - Apis mellifera
  - Calliphora vicina
- **Uniqueness by nest**: 32.1-50.0% (average 24.4%)
- **Shared between 2+ nests**: At least 50% of each nest's OTU content

### Relative Abundance by Family
- **Apidae**: 22.55% (range: 14.86-29.27%)
- **Calliphoridae**: 21.85% (range: 11.29-32.14%)
- **Vespidae**: 8.15% (range: 0.00-21.43%)
- **Muscidae**: 7.90% (range: 2.50-13.51%)
- **Sarcophagidae**: 4.97% (range: 1.79-11.67%)
- **Diptera + Hymenoptera**: 76.37% of all OTUs (44.43% Diptera, 31.94% Hymenoptera)

### Diversity Indices
- **Species richness per nest**: Mean 4.44 ± 0.99 (range: 3.33-6.17)
- **Shannon index per nest**: Mean 1.35 ± 0.27 (range: 1.01-1.72)
- **Levins' niche breadth**: Mean 0.37 ± 0.07 (range: 0.26-0.49)
- **Niche overlap (Pianka's index)**: Mean 0.78 ± 0.08 (range: 0.594-0.881)

### Functional Roles
- **Pollinators**: 28.95%
- **Nectarivores**: 21.30%
- **Detritivores**: 21.30%
- **Predators**: 11.61%
- **Herbivores**: 4.59%
- **Parasitoids**: 3.83%

### Functional Role Composition
- **Pollinators**: Apidae (37.00%), Calliphoridae (36.56%), Muscidae (14.54%)
- **Nectarivores**: Apidae (50.30%), Muscidae (19.76%), Vespidae (19.16%)
- **Detritivores**: Calliphoridae (49.70%), Muscidae (19.76%), Sarcophagidae (11.98%), Anthomyiidae (7.78%)
- **Predators**: Vespidae (36.17%), Muscidae (36.26%), Gomphidae (17.58%)
- **Herbivores**: Anthomyiidae (most frequently detected)

### Statistical Analysis
- **PERMANOVA**: All factors significant (nest, season, tree species, presence of males)
- **Nest factor**: 7% of community variation (P < 0.001)
- **Season factor**: 5% of community variation (P < 0.001)
- **Jensen-Shannon divergence (duplicates)**: 0.035-0.296

## Other Quantitative Data

### Sample Collection Details
- **Meconium definition**: Intestinal content expelled during transition from larval to pupal stage
- **Larval stage duration**: Approximately 15 days
- **Collection method**: From base of peripheral cells (newly formed cells with single meconium)
- **Storage**: Absolute ethanol at -20°C

### DNA Extraction
- **Kit**: ISOLATE Fecal DNA Kit (Bioline)
- **RNA removal**: 60 μg RNase A (Promega)
- **Blanks**: 2 blank DNA extractions for contamination monitoring

### Bioinformatics
- **Package**: DADA2 R package
- **Filtering**: maxN = 0 (sequences with Ns discarded)
- **Chimera removal**: removeBimeraDenovo (consensus method)
- **Clustering**: VSEARCH v2.27.0 (97% similarity)
- **BLAST database**: GenBank
- **Identity thresholds**:
  - <85%: Class level only
  - 85-90%: Order level
  - 90-95%: Family level
  - >95%: Genus or species level

### Contamination Control
- **Blanks**: Agrotis ipsilon, Culex pipiens, unidentified Tachinidae detected and removed
- **Negative control**: Tachinidae OTU detected and removed from all samples

### Geographic Context
- **Location**: Mallorca (Westernmost Mediterranean Archipelago)
- **Invasion year**: 2015
- **Nest removal**: Part of eradication efforts

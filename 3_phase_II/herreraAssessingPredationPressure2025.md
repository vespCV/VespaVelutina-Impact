# Quantitative Data: Herrera et al. 2025

## Template-Relevant Data

### Study Design
- **Country**: Spain (Mallorca, Balearic Islands)
- **Year**: 2016
- **Number of nests**: 7 nests
- **Number of meconium samples**: 90 samples (approximately 13 per nest)
- **Sample collection**: From peripheral cells of combs

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

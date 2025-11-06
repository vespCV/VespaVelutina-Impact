# Quantitative Data: Verdasca et al. 2022

## Template-Relevant Data

### Study Design
- **Country**: Portugal
- **Start year**: 2018
- **Start month**: July
- **End month**: November
- **Number of nests**: 12 V. velutina nests
- **Sample collection period**: July-November 2018
- **Time between nest treatment and collection**: 1 day to 4 weeks (5 nests with no information)

### Sample Collection
- **Faecal pellets collected**: 12 (one per nest)
- **Workers collected**: 12 (one per nest)
- **Jaws analyzed**: 10 (2 discarded due to poor conditions)
- **Stomachs analyzed**: 10 (2 discarded due to poor conditions)
- **Total samples analyzed**: 32 (12 faecal pellets, 10 jaws, 10 stomachs)
- **PCR replicates per sample**: 3
- **Total DNA libraries**: 96 (32 samples × 3 replicates)

### DNA Sequencing
- **Sequencing platform**: Illumina MiSeq
- **Kit used**: MiSeq Reagent Nano Kit v2 (500 cycles; 2 × 250 bp)
- **Platform usage**: 30% of a MiSeq run
- **COI region amplified**: 210 bp
- **Final read numbers after threshold**: 108,979 reads
- **Average reads per replicate**: 1,265 reads/replicate
- **Average reads in faecal pellets**: 1,709 reads/replicate
- **Average reads in jaws**: 933 reads/replicate
- **Average reads in stomachs**: 786 reads/replicate

### Prey Identification
- **Taxonomic levels identified**: 4 orders, 9 families, 6 genera, 1 species
- **Threshold applied**: 0.02% of total reads
- **Honeybee reads**: 79,143 (75% of total reads)
- **Honeybee reads in faecal pellets**: 50,549 (84% of 60,518 total reads)
- **Honeybee reads in jaws**: 20,458 (74% of 27,546 total reads)
- **Honeybee reads in stomachs**: 8,136 (39% of 20,915 total reads)

### Detection Rates
- **Honeybee detection in faecal pellets**: 100% (all replicates of all samples)
- **Honeybee detection in jaws**: 70% of samples
- **Honeybee detection in stomachs**: 40% of samples
- **Concordance between jaws and stomachs**: 37.5%
- **Honeybee detection in workers**: All colonies except location 10
- **Rarefaction plateau**: 400 reads per sample for honeybee detection

### Sample Size Requirements
- **Minimum jaws needed for honeybee detection**: 6 workers (0.1% false negative probability)
- **Minimum stomachs needed for honeybee detection**: 13 workers

### DNA Persistence
- **Honeybee DNA persistence in faecal pellets**: At least 28 days (maximum known period)

## Other Quantitative Data

### Primer Design
- **COI fragment length**: ~160 bp
- **Blocking primer concentrations tested**: 0.5x, 1x, 2x, 5x
- **PCR conditions**: Touchdown PCR (5 cycles: 95°C 15min, 56°C-0.5°C/cycle 30s, 72°C 30s; 32 cycles: 95°C 30s, 54°C 30s, 72°C 30s; final extension 60°C 10min)

### Bioinformatic Analysis
- **Alignment score threshold**: <40 removed
- **OTU target size**: 135-165 bp
- **MEGABLAST parameters**: minScore=100.0, topPercent=5.0, minSupportPercent=0.0, minSupport=1

### Prey Diversity
- **Orders identified**: Hymenoptera, Diptera, Lepidoptera, Orthoptera
- **Families identified**: 9 families
- **Genera identified**: 6 genera
- **Species identified**: 1 species (Apis mellifera)

### Statistical Analysis
- **Mann-Whitney U test**: Used to compare honeybee reads between faecal pellets/jaws and faecal pellets/stomachs
- **Paired T-test**: Used to compare jaws and stomachs from same worker

### Other Prey Groups
- **Lepidoptera detection**: 33% of faecal samples
- **Vespa genus detection in jaws**: 50% frequency of occurrence
- **Vespa genus detection in stomachs**: 90% frequency of occurrence
- **Vespa genus detection in faecal pellets**: 0%

### Methodological Notes
- **DNA extraction kit**: E.Z.N.A. Tissue DNA Kit (Omega BIO-TEK)
- **Library normalization**: 10 nM
- **Size distribution analysis**: TapeStation 2200 using HS D1000 kit
- **Quantitative PCR**: BIORAD C1000 Real Time Thermocycler using KAPA Library Quantification kit

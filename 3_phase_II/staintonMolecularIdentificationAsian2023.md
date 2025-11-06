# Quantitative Data: Stainton et al. 2023

## Template-Relevant Data

### Study Design
- **Country**: United Kingdom (including Channel Islands)
- **Number of nests**: 5 nests
- **Nest locations**: 
  - Alderney, Channel Islands (October 2016)
  - Tetbury, Gloucestershire (September 2016)
  - Woolacombe, Devon (September 2017)
  - Jersey, Channel Islands (August 2019)
  - Gosport, Hampshire (September 2020)
- **Coordinates**: 
  - Jersey: 49.2, -2.1
  - Tetbury: 51.64, -2.15
  - Alderney: 49.71, -2.20
  - Gosport: 50.79, -1.14
  - Woolacombe: 51.17, -4.21

### Sample Collection
- **Larvae sampled per nest**: 10 (attempted)
- **Successfully sequenced samples**: 
  - Jersey: 9 samples
  - Tetbury: 10 samples
  - Alderney: 6 samples (4 failed)
  - Gosport: 3 samples (7 failed)
  - Woolacombe: 10 samples
- **Total larval samples analyzed**: 38 samples
- **Storage temperature**: -15°C (short term) or -50°C (long term)

### Sequencing Results
- **Jersey nest (Flongle)**:
  - Samples: 9
  - Mean reads per sample: 5,827
  - Species per nest: 26
  - Most abundant taxon: Blow fly (16.5% of reads)
  - Honey bee: 20.5% of reads
- **Tetbury nest (MinION)**:
  - Samples: 10
  - Mean reads per sample: 15,497
  - Species per nest: 20
  - Most abundant taxon: Wasp (34.3% of reads)
  - Honey bee: 0.33% of reads
- **Alderney nest (MinION)**:
  - Samples: 6
  - Mean reads per sample: 22,194
  - Species per nest: 15
  - Most abundant taxon: Wasp (66.6% of reads)
  - Honey bee: 0% of reads
- **Gosport nest (MinION)**:
  - Samples: 3
  - Mean reads per sample: 17,433
  - Species per nest: 16
  - Most abundant taxon: Wasp (65.9% of reads)
  - Honey bee: 0.98% of reads
- **Woolacombe nest (MinION)**:
  - Samples: 10
  - Mean reads per sample: 18,699
  - Species per nest: 15
  - Most abundant taxon: Spider (35.1% of reads)
  - Honey bee: 7.3% of reads

### Sequencing Platform Details
- **MinION dataset** (Tetbury, Woolacombe, Gosport, Alderney):
  - Flow cell: R10.3
  - Sequencing duration: 48 hours
  - Total reads: 885,593
  - Total data: ~631 Mb
  - Average quality score: 11.6 (~6.9% error rate)
  - Median read length: 705 bp
  - PCR negative: 128 reads
  - Barcode negative: 61 reads
- **Flongle dataset** (Jersey):
  - Flow cell: R9.4.1
  - Sequencing duration: 48 hours
  - Total reads: 70,375
  - Total data: ~56 Mb
  - Average quality score: 10.2 (~9.5% error rate)
  - Median read length: 758 bp

### Prey Species Detection
- **Total species range per nest**: 15-26 species
- **Average species per gut**: 6.7
- **Maximum species in single gut**: 13 (Gosport nest)
- **Minimum species in single gut**: 1 (Dryomyza anilis in Tetbury)
- **Honey bee detection**: Present in 25 of 38 larvae (65.8%)
- **Honey bee detection by nest**: 4 of 5 nests (absent in Alderney)

### Prey Composition
- **Vespula spp. (wasps)**: Most abundant prey in all nests
  - Present in: 26 of 38 samples
  - Found in: All 5 nests
- **Blow flies (Calliphoridae)**: Common across all nests
- **Spiders**: Present in 4 of 5 nests
  - Species: Araneus diadematus, Metellina segmentata, Zygiella spp.
  - Contributed ≥10% of reads in 2 nests
- **Hoverflies (Syrphidae)**: Present in 3 nests
  - Species: Eristalis spp., Scaeva pyrastri, Sericomyia silentis, Eumerus strigatus, Syrphus vitripennis

### DNA Extraction and PCR
- **Extraction kit**: Qiagen Blood and Tissue Kit
- **COI fragment length**: ~650 bp
- **Primers used**: 
  - Jersey: LCO22me & HCO700dy, CI-J-2183 & L2-N-3014
  - Others: LC01490 & HC02198
- **PCR volume**: 20 µL
- **DNA volume**: 1-10 µL
- **BSA concentration**: 0.5 µL of 20 mg/mL

### Bioinformatics
- **Base calling**: Guppy version 5.0.11 (high accuracy mode)
- **Read trimming**: Cutadapt
- **Read length filters**: 550-750 bp
- **Quality score filters**: 
  - MinION: ≥10
  - Flongle: ≥7
- **BLAST parameters**: 
  - Percentage identity: ≥85%
  - Alignment length: ≥80%
  - Bit score: Within 3% of highest scoring hit
- **LCA threshold**: 75% agreement
- **Read count threshold**: 1% of highest taxon per sample

## Other Quantitative Data

### Nest Characteristics
- **Typical nest population**: 3,500+ individuals
- **Samples per nest**: Up to 10 larvae (representing <0.3% of nest population)

### Prey Abundance by Nest
- **Jersey**: Blow flies dominant (32.7% Calliphora, 15.3% Lucilia)
- **Tetbury**: Dryomyza anilis prominent (23.2% in one sample, 21,574 reads)
- **Alderney**: Wasp dominant (66.6%)
- **Gosport**: Wasp dominant (65.9%)
- **Woolacombe**: Spider dominant (35.1% Araneus diadematus)

### Contamination
- **Host DNA contamination**: 
  - Tetbury: 1 sample exclusively V. velutina, 3 others with small amounts
  - Alderney: 2 samples with small amounts
  - Woolacombe: 1 sample with small amounts

### Methodological Limitations
- **Success rate by nest**: 
  - Jersey: 100% (9/9)
  - Tetbury: 100% (10/10)
  - Woolacombe: 100% (10/10)
  - Alderney: 60% (6/10)
  - Gosport: 30% (3/10)
- **Failure causes**: Poor initial storage or repeated freeze-thaw cycles

### Prey Groups Identified
- **Diptera families**: Calliphoridae, Muscidae, Syrphidae, Tachinidae, Scathophagidae, Sarcophagidae, Drosophilidae
- **Hymenoptera**: Vespula spp., Apis mellifera, V. velutina (host contamination)
- **Araneae**: Araneus diadematus, Metellina segmentata, Zygiella spp.
- **Lepidoptera**: Phlogophora meticulosa
- **Orthoptera**: Acrididae spp.
- **Other**: Oniscus asellus (woodlouse), Erinaceus europaeus (hedgehog - likely carrion), Monodus spp. (algae)

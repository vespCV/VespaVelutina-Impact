# Instructions for Updating Data Extraction and README After Adding New Studies

## Overview
When a new PDF article has been added to the `pdf included` folder and quantitative data has been extracted into a markdown file (following `_update_phase_II.md`), follow these steps to:
1. Update the master dataset CSV file (`_pdf_phase_II.csv`)
2. Update the README.md with new quantitative findings
3. Regenerate visualizations if needed

## Step-by-Step Instructions

### Part 1: Update the Master Dataset CSV

#### 1.1 Locate the New Markdown File
- Find the newly created markdown file in `3_phase_II/` folder
- Note the filename (should match PDF name without .pdf extension)
- Read the markdown file to extract all relevant data

#### 1.2 Extract CSV-Relevant Data from Markdown
From the markdown file, extract the following information to populate CSV columns:

**Basic Information:**
- **Number**: Next sequential number (check last entry in CSV)
- **Author**: First author surname (from markdown header)
- **Publication Year**: Year from markdown
- **Title**: Full title from markdown
- **Journal**: Journal name
- **DOI**: DOI from markdown (format: 10.xxxx/xxxxx)

**Exclusion/Inclusion Flags:**
- **ex_editorial**: 0 or 1 (1 if editorial)
- **ex_review**: 0 or 1 (1 if review article)
- **ex_no_data**: 0 or 1 (1 if no quantifiable data)
- **ex_gray**: 0 or 1 (1 if gray literature)
- **ex_no_pdf**: 0 or 1 (1 if PDF not available)

**Inclusion Criteria (1 = yes, 0 = no):**
- **in_apis_predation**: Does study measure Apis mellifera predation?
- **in_other_spec_predation**: Does study measure predation on other species?
- **in_apis_colony_loss**: Does study measure colony loss/mortality?
- **in_apis_foraging**: Does study measure foraging behavior changes?
- **in_apis_other_behavior**: Does study measure other behavioral changes?
- **in_honey_yield**: Does study measure honey production/yield?
- **in_beekeeping_loss**: Does study measure economic/beekeeping losses?
- **in_management_costs**: Does study measure management/control costs?

**Observation/Data Collection Types (1 = yes, 0 = no):**
- **type_observation_visual**: Visual observations
- **type_observation_photo**: Photo documentation
- **type_observation_video**: Video monitoring
- **type_pellets**: Pellet analysis
- **type_radio_freq**: Radio frequency tracking
- **type_CIO_faeces**: DNA metabarcoding/faecal analysis
- **type_costs**: Economic cost analysis

**Geographic and Temporal Data:**
- **country**: Country where study conducted
- **start_year**: Study start year
- **end_year**: Study end year
- **start_month**: Start month (if specified)
- **end_month**: End month (if specified)

**Sample Sizes:**
- **n_apiaries**: Number of apiaries
- **n_beehives**: Number of beehives/colonies
- **n_vespa_nests**: Number of hornet nests studied
- **n_vespa_velutina**: Number of hornets observed/counted
- **distance_hornets_nest**: Distance measurements or foraging ranges

**Outcomes (Text summaries):**
- **outcome_apis_predation**: Summary of predation findings
- **outcome_foraging_behavior**: Summary of foraging behavior findings
- **outcome_other_apis_behavior**: Summary of other behavioral findings
- **outcome_predation_time_of_the_day**: Temporal patterns of predation

#### 1.3 Add Entry to CSV
- Open `3_phase_II/_pdf_phase_II.csv`
- Add a new row at the end (before the summary row)
- Fill all columns with extracted data
- Use semicolon (;) as delimiter
- Leave empty cells blank (not "N/A" or "0" unless appropriate)
- For text fields, keep summaries concise but informative

#### 1.4 Update Summary Row
- The last row contains summary statistics
- Update counts if needed (though this is usually automatic)

### Part 2: Update README.md

#### 2.1 Update Study Count
- Find section "## 4 Data Extraction"
- Update the count: "extracted from X studies (Y included, Z excluded)"
- Update if new study changes inclusion/exclusion numbers

#### 2.2 Update Relevant Data Sections

**Section 4.2: Predation Data**
If the new study contains predation data:
- **4.2.1 Predation Rates and Success**: Add key metrics to the summary table
- **4.2.2 Prey Composition**: Add findings to appropriate tables
- Include study location, key numbers, and brief context

**Section 4.3: Colony Survival and Loss**
If the new study contains survival/mortality data:
- **4.3.1 Colony Survival**: Add survival rates to summary table
- **4.3.2 Mortality Factors**: Add risk thresholds or mortality profiles
- Include sample sizes and study context

**Section 4.4: Apis mellifera Behavior**
If the new study contains behavioral data:
- **4.4.1 Foraging Paralysis Thresholds**: Add thresholds to summary table
- **4.4.2 Activity Reductions**: Add behavioral findings
- Include statistical significance where reported

**Section 4.5: Economic Impact**
If the new study contains economic data:
- Add economic costs, impacts, or comparisons
- Include currency, time period, and geographic scope
- Compare with existing economic data if relevant

**Section 4.6: Background Data**
- **4.6.2 Apiaries and Colonies**: Add study to the table
- **4.6.3 Hornet Nests Studied**: Add if nest data available
- Update country counts in 4.6.1 if new country

#### 2.3 Update Summary Section (Section 5)

**Section 5.2: Impact Summary**
- Update key quantitative findings if new study provides:
  - New predation rates or ranges
  - New survival percentages
  - New behavioral thresholds
  - New economic impact data

**Format for Updates:**
- Use consistent formatting with existing entries
- Include study citation (Author et al. Year)
- Include location/country
- Include sample sizes where relevant
- Preserve existing data structure

#### 2.4 Update Executive Summary (Top of README)
If the new study significantly changes key findings:
- Review numbers in "Key Findings" section
- Update ranges if new data extends beyond current ranges
- Update recommendations if new evidence supports changes
- Update "Last updated" date

**Only update if:**
- New study provides more recent data
- New study significantly changes ranges or averages
- New study provides data for previously missing categories
- New study changes risk thresholds or recommendations

### Part 3: Regenerate Visualizations (If Needed)

#### 3.1 Check if Visualizations Need Updating
Visualizations should be regenerated if:
- New study adds a new country (updates `study_locations.jpg`)
- New study changes temporal distribution (updates `study_timeline.jpg`)
- New study adds new outcome types (updates `outcome_types.jpg`)
- New study uses new observation methods (updates `observation_methods.jpg`)

#### 3.2 Regenerate Visualizations
- Navigate to `5_visualisation_reporting/` folder
- Run: `python3 create_visualizations.py`
- Verify new images are created correctly
- Check that all visualizations reflect new data

### Part 4: Update Data Summary Report

#### 4.1 Update `5_visualisation_reporting/data_summary_report.md`
- Update study count in header
- Add new findings to relevant sections
- Update "Study Characteristics" if new country/method
- Update "Key Findings" if significant new data
- Update "Data Quality Assessment" if needed

## Quality Checks

Before completing the update, verify:

### CSV Update Checks
- ✓ New entry added with correct sequential number
- ✓ All required fields populated (Author, Year, DOI, Title)
- ✓ Inclusion/exclusion flags correctly set
- ✓ Outcome summaries are clear and complete
- ✓ CSV file still opens correctly in spreadsheet software

### README Update Checks
- ✓ Study count updated
- ✓ New data added to appropriate sections
- ✓ Tables maintain consistent formatting
- ✓ Citations follow format: "Author et al. Year (Location)"
- ✓ Numbers match those in markdown file
- ✓ Executive summary updated if significant changes

### Visualization Checks
- ✓ All four visualization files regenerated
- ✓ New study appears in relevant visualizations
- ✓ Image files are readable and properly formatted
- ✓ File sizes are reasonable (<500KB each)

## Formatting Guidelines

### CSV Formatting
- Use semicolon (;) as delimiter
- No quotes around text fields unless they contain semicolons
- Dates: YYYY format for years, numeric for months (1-12)
- Numbers: Use exact values, include ranges as "min-max"
- Text summaries: Keep concise, use semicolons to separate multiple points

### README Formatting
- Use markdown tables for structured data
- Use bullet points for lists
- Use **bold** for key numbers and metrics
- Include study citation: (Author et al. Year)
- Include location in parentheses: (Location)
- Preserve existing table structure when adding rows

### Citation Format
- Inline: (Author et al. Year)
- In tables: Author et al. Year | Location
- Full citations: Not needed in README (use DOI reference)

## Example: Adding a New Study

**Scenario**: New study "Smith et al. 2024" on predation rates in Germany

**Steps:**
1. Extract data from `smithPredationRatesGermany2024.md`
2. Add CSV entry with:
   - Number: 35 (next sequential)
   - Author: Smith
   - Year: 2024
   - Country: Germany
   - in_apis_predation: 1
   - outcome_apis_predation: "Predation rate 3.2% (n=150 interactions)..."
3. Update README section 4.2.1:
   - Add row to predation rates table
   - Include: "Smith et al. 2024 (Germany): 3.2% success rate..."
4. Update README section 4.6.1:
   - Add Germany to country table if first study
5. Update study count: "35 studies (31 included, 4 excluded)"
6. Regenerate visualizations (new country = update locations chart)
7. Update data_summary_report.md study count

## Important Notes

- **Preserve existing data**: Never remove or modify existing entries unless correcting errors
- **Maintain consistency**: Follow existing formatting and structure
- **Verify numbers**: Cross-check all numbers between markdown, CSV, and README
- **Update dates**: Update "Last updated" date in README when making changes
- **Document changes**: Consider noting significant updates in commit messages

## Reference Files

- **Master dataset**: `3_phase_II/_pdf_phase_II.csv`
- **Data extraction template**: `3_phase_II/_update_phase_II.md`
- **Visualization script**: `5_visualisation_reporting/create_visualizations.py`
- **Summary report**: `5_visualisation_reporting/data_summary_report.md`
- **Main README**: `README.md`

## Troubleshooting

**CSV won't open correctly:**
- Check semicolon delimiters
- Verify no unescaped quotes in text fields
- Check for extra semicolons at end of rows

**README formatting broken:**
- Check markdown table syntax (pipes and alignment)
- Verify no broken links
- Check for unclosed bold/italic formatting

**Visualizations not updating:**
- Verify CSV was saved correctly
- Check Python script can read CSV
- Verify matplotlib is installed
- Check file permissions in output directory


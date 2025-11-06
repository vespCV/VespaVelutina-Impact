# Instructions for Extracting Quantitative Data from New PDF Articles

## Overview
When a new PDF article is added to the `pdf included` folder, follow these steps to extract and structure all quantitative data into a Markdown file.

## Step-by-Step Instructions

### 1. Locate the New PDF
- Find the new PDF file in the `pdf included` folder
- Note the exact filename (without .pdf extension) - this will be used for the output filename

### 2. Extract Text from PDF
- Use Python to extract text from the PDF:
  - Try `pdfplumber` first (preferred method)
  - Fall back to `PyPDF2` if `pdfplumber` fails
- If extraction tools are not available, read the PDF content directly if possible

### 3. Read the Code Template
- Read the file: `3_phase_II/_code_template.md`
- This contains the CSV column headers that define what "template-relevant data" means
- Understand the structure of data categories (study design, observations, outcomes, etc.)

### 4. Extract Quantitative Data
Extract ALL quantitative data from the PDF, organizing it into two main sections:

#### A. Template-Relevant Data
Extract data that matches the categories in `_code_template.md`:
- **Study Design**: Country, years, months, number of apiaries/colonies/nests, locations, coordinates
- **Hornet Monitoring**: Traps, counts, frequencies, methods
- **Predation Observations**: Types of observations, frequencies, methods
- **Colony Performance**: Measurements, counts, percentages, statistical results
- **Outcomes**: Predation rates, behavior changes, losses, etc.

#### B. Other Quantitative Data
Extract ALL other quantitative data found in the paper that doesn't fit the template:
- Additional measurements
- Statistical values (means, SDs, ranges, p-values, χ², etc.)
- Sample sizes
- Percentages and proportions
- Temporal data
- Spatial data
- Any other numerical information

**Important**: Include ALL quantitative data, even if it doesn't fit the current template. This data might be added to the template later.

### 5. Create the Markdown File
- **Filename**: Use the PDF filename (without .pdf) + `.md`
- **Location**: Save in `3_phase_II/` folder
- **Structure**:
  ```markdown
  # Quantitative Data: [Author et al. Year]
  
  ## Template-Relevant Data
  
  [Organize data by categories from template]
  
  ## Other Quantitative Data
  
  [All other quantitative data found in the paper]
  ```

### 6. Formatting Guidelines
- Use clear section headers (## for main sections, ### for subsections)
- Use bullet points for lists
- Include units for all measurements
- Include statistical values (means, SDs, ranges, p-values, etc.)
- Include sample sizes (n = X)
- Include confidence intervals where available
- Preserve precision of numbers as reported in the paper
- Use **bold** for key terms and labels
- Include context for all numbers (what they represent)

### 7. Data Extraction Priorities
1. **First priority**: Extract template-relevant data (matching `_code_template.md` structure)
2. **Second priority**: Extract all other quantitative data comprehensively
3. **Include**: All numbers, measurements, counts, percentages, statistical results
4. **Include**: Ranges, means, standard deviations, sample sizes
5. **Include**: P-values, confidence intervals, statistical test results
6. **Include**: Geographic coordinates, dates, time periods
7. **Include**: Dimensions, weights, distances, temperatures, etc.

### 8. Quality Checks
Before finishing, verify:
- ✓ All quantitative data from the PDF has been extracted
- ✓ Data is organized clearly with appropriate headers
- ✓ Units are included for all measurements
- ✓ Statistical values include context (what test, what comparison)
- ✓ Sample sizes are included where relevant
- ✓ The file follows the same structure as existing files in `3_phase_II/`

### 9. Example Structure
Refer to existing files like `perrardObservationsColonyActivity2009.md` for reference on structure and detail level.

## Important Notes

- **Comprehensiveness**: Extract ALL quantitative data, not just what fits the template
- **Precision**: Preserve exact numbers as reported in the paper
- **Context**: Always include context for numbers (what they measure, when, where)
- **Statistics**: Include all statistical test results, p-values, confidence intervals
- **Ranges**: Include ranges, means, and standard deviations where available
- **Sample sizes**: Always note sample sizes (n = X) for any measurements

## Template Categories Reference

The `_code_template.md` file contains CSV headers that indicate template-relevant categories:
- Study identification (Author, Year, Title)
- Exclusion criteria flags
- Study type (observation methods, data types)
- Geographic and temporal data
- Sample sizes (apiaries, beehives, nests)
- Outcomes and measurements
- Statistical results

Match extracted data to these categories in the "Template-Relevant Data" section, and put everything else in "Other Quantitative Data".


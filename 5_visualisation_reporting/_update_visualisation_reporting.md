# Instructions for Updating Visualizations and Reporting Files

## Overview
When the master dataset CSV (`3_phase_II/_pdf_phase_II.csv`) has been updated with new studies (following `4_data_extraction/_update_dataextraction.md`), follow these steps to:
1. Regenerate visualizations to reflect new data
2. Update the data summary report with new findings
3. Verify all visualizations and reports are current and accurate

## Step-by-Step Instructions

### Part 1: Determine if Visualizations Need Updating

#### 1.1 Check What Changed
Review the CSV updates to determine which visualizations are affected:

**Visualizations that need regeneration if:**
- **study_locations.jpg**: New study adds a new country or changes country distribution
- **study_timeline.jpg**: New study has a different publication year
- **outcome_types.jpg**: New study adds new outcome types (predation, colony loss, foraging, etc.)
- **observation_methods.jpg**: New study uses new observation/data collection methods

**Always regenerate all visualizations** when:
- New study added (included entry)
- Study status changed (excluded to included or vice versa)
- Multiple studies added in one update

#### 1.2 Quick Check Script
Run this check to see what changed:
```python
# Compare old and new CSV to identify changes
# Check: new countries, new years, new outcome types, new methods
```

### Part 2: Regenerate Visualizations

#### 2.1 Prerequisites
- Ensure `3_phase_II/_pdf_phase_II.csv` is up to date
- Verify Python environment has required packages:
  - `matplotlib`
  - `numpy`
- Check that CSV file is readable and properly formatted

#### 2.2 Run Visualization Script
1. Navigate to `5_visualisation_reporting/` directory
2. Run the visualization script:
   ```bash
   python3 create_visualizations.py
   ```
3. Verify output messages indicate successful creation:
   - "Processing X included studies" (should match current count)
   - "Created: study_locations.jpg"
   - "Created: study_timeline.jpg"
   - "Created: outcome_types.jpg"
   - "Created: observation_methods.jpg"
   - "All visualizations created successfully!"

#### 2.3 Verify Generated Visualizations

**Check each visualization file:**

**study_locations.jpg:**
- ✓ All countries with studies are represented
- ✓ Bar heights match study counts per country
- ✓ New country appears if added
- ✓ Total matches number of included studies

**study_timeline.jpg:**
- ✓ All publication years are shown
- ✓ Line/points reflect study counts per year
- ✓ New year appears if added
- ✓ X-axis includes all relevant years

**outcome_types.jpg:**
- ✓ All outcome types are listed
- ✓ Bar lengths match counts from CSV
- ✓ New outcome types appear if added
- ✓ Total should sum to more than study count (studies can have multiple outcomes)

**observation_methods.jpg:**
- ✓ All observation methods are listed
- ✓ Bar lengths match counts from CSV
- ✓ New methods appear if added
- ✓ Methods with 0 counts may not appear (this is normal)

#### 2.4 Troubleshooting Visualization Issues

**If script fails:**
- Check CSV file path in script (should be `'3_phase_II/_pdf_phase_II.csv'`)
- Verify CSV delimiter is semicolon (;)
- Check for encoding issues (should be UTF-8)
- Verify all required Python packages are installed

**If visualizations look incorrect:**
- Verify CSV was saved correctly after updates
- Check that exclusion flags are correct (ex_editorial, ex_review, etc.)
- Ensure included studies are properly identified
- Re-run script after fixing CSV issues

**If file sizes are too large:**
- Check DPI setting in script (currently 300, can reduce to 150 if needed)
- Verify images are JPG format (not PNG)
- Check for excessive data points

### Part 3: Update Data Summary Report

#### 3.1 Update Header Information
Edit `data_summary_report.md`:

**Update these fields:**
- **Report Date**: Current date (YYYY-MM-DD format)
- **Total Studies Included**: Count from CSV (included entries)
- **Total Studies Excluded**: Count from CSV (excluded entries)

#### 3.2 Update Key Findings Section

**Section 1: Predation Pressure**
- Review new studies for predation data
- Update ranges if new data extends beyond current ranges
- Add new metrics if significant findings
- Format: Use bullet points, include ranges, cite studies

**Section 2: Colony Survival**
- Update survival rates if new data available
- Add new risk thresholds if identified
- Update ranges if extended
- Include sample sizes and study context

**Section 3: Behavioral Impacts**
- Update thresholds if new data changes them
- Add new behavioral findings
- Include statistical significance where reported

**Section 4: Economic Impact**
- Add new economic data if available
- Update ranges or add new countries
- Include currency, time period, geographic scope

#### 3.3 Update Study Characteristics Section

**Geographic Distribution:**
- Update country counts
- Add new countries if applicable
- Update percentages if distribution changed significantly

**Temporal Distribution:**
- Update "Latest study" year if new
- Update "Peak publication years" if pattern changed
- Add note if temporal trends are significant

**Observation Methods:**
- Update counts for each method
- Add new methods if introduced
- Note any methodological trends

**Outcome Types Measured:**
- Update counts for each outcome type
- Add new outcome types if introduced
- Note any emerging research areas

#### 3.4 Update Data Quality Assessment

**Strengths:**
- Add new strengths if new studies address previous limitations
- Update if coverage improved (new countries, longer timeframes)

**Limitations:**
- Update if new limitations identified
- Note if previous limitations have been addressed
- Add new limitations if discovered

**Recommendations:**
- Update if new evidence supports different recommendations
- Add new recommendations based on latest findings
- Update priorities if research gaps have changed

#### 3.5 Update References Section
- Note that all studies are in CSV
- Update if reference format changed
- Add note about data availability if relevant

### Part 4: Quality Checks

#### 4.1 Visualization Quality Checks
Before completing, verify:

**File Existence:**
- ✓ All four JPG files exist in `5_visualisation_reporting/`
- ✓ File names match expected names exactly
- ✓ Files are readable (not corrupted)

**Content Accuracy:**
- ✓ Study counts match CSV counts
- ✓ Countries match CSV countries
- ✓ Years match CSV publication years
- ✓ Outcome types match CSV inclusion flags
- ✓ Methods match CSV type flags

**Visual Quality:**
- ✓ Text is readable (not too small)
- ✓ Colors are distinct and accessible
- ✓ Labels are clear and complete
- ✓ Charts are properly scaled
- ✓ Legends are present where needed

#### 4.2 Report Quality Checks

**Content Accuracy:**
- ✓ Study counts match CSV
- ✓ Numbers match README.md summaries
- ✓ Dates are current
- ✓ All sections are updated if relevant

**Formatting:**
- ✓ Markdown formatting is correct
- ✓ Tables are properly formatted
- ✓ Bullet points are consistent
- ✓ Headers follow hierarchy (##, ###)

**Completeness:**
- ✓ All new significant findings are included
- ✓ Key metrics are updated
- ✓ Recommendations reflect latest evidence
- ✓ Data source references are correct

### Part 5: Additional Reporting (Optional)

#### 5.1 Create New Visualizations (If Needed)
If new types of visualizations would be valuable:

1. **Identify need**: What question does it answer?
2. **Design visualization**: Choose appropriate chart type
3. **Add to script**: Modify `create_visualizations.py`
4. **Test**: Verify it works with current data
5. **Document**: Add to this instruction file

**Potential new visualizations:**
- Predation rates over time
- Survival rates by protection method
- Economic costs by country
- Study sample sizes distribution

#### 5.2 Update README Visualizations Section
If visualizations are referenced in README:
- Update any embedded image references
- Update captions if content changed
- Add new visualization references if created

## Formatting Guidelines

### Visualization Files
- **Format**: JPG (not PNG, to reduce file size)
- **Resolution**: 300 DPI (or 150 DPI if file size is concern)
- **Naming**: Descriptive, lowercase with underscores
- **Size**: Aim for <500KB per file
- **Colors**: Use accessible color palettes, avoid red-green combinations

### Report Markdown
- **Date format**: YYYY-MM-DD
- **Numbers**: Use consistent precision (e.g., one decimal place for percentages)
- **Ranges**: Format as "X-Y" or "X to Y"
- **Citations**: Use "Author et al. Year" format
- **Sections**: Use ## for main sections, ### for subsections

## Example: Updating After Adding New Study

**Scenario**: New study "Smith et al. 2024" from Germany on predation rates

**Steps:**
1. **Check CSV**: Verify entry 35 (Smith et al. 2024) is in CSV
2. **Determine updates needed**:
   - New country (Germany) → Update study_locations.jpg
   - New year (2024) → Update study_timeline.jpg
   - Predation data → May affect outcome_types.jpg
3. **Regenerate visualizations**:
   ```bash
   cd 5_visualisation_reporting
   python3 create_visualizations.py
   ```
4. **Verify outputs**:
   - Check Germany appears in study_locations.jpg
   - Check 2024 appears in study_timeline.jpg
   - Verify study count increased by 1
5. **Update data_summary_report.md**:
   - Update header: "Total Studies Included: 31"
   - Update date: "Report Date: 2025-11-08"
   - Add Germany to Geographic Distribution
   - Update "Latest study: 2024"
   - Add predation findings if significant
6. **Quality check**: Verify all files are updated correctly

## Automation Notes

### When to Automate
- Visualizations can be fully automated (script reads CSV directly)
- Report updates require manual review and judgment
- Some report sections need human interpretation

### Script Maintenance
- Update `create_visualizations.py` if CSV structure changes
- Update script if new visualization types are added
- Test script after major CSV format changes

## Important Notes

- **Always regenerate all visualizations** when CSV is updated (even if only one study added)
- **Review report manually** - automation cannot judge significance of findings
- **Keep visualizations current** - outdated visualizations can mislead users
- **Verify numbers** - Cross-check visualization counts with CSV counts
- **Update dates** - Always update report date when making changes
- **Document changes** - Note significant updates in commit messages

## Reference Files

- **Visualization script**: `5_visualisation_reporting/create_visualizations.py`
- **Data summary report**: `5_visualisation_reporting/data_summary_report.md`
- **Master dataset**: `3_phase_II/_pdf_phase_II.csv`
- **Data extraction instructions**: `4_data_extraction/_update_dataextraction.md`
- **Main README**: `README.md`

## Troubleshooting

**Visualizations not updating:**
- Check CSV path in script is correct
- Verify CSV was saved after updates
- Check Python environment and packages
- Verify file permissions

**Report numbers don't match:**
- Cross-check with CSV counts
- Verify inclusion/exclusion flags
- Check for typos in manual updates
- Compare with README.md numbers

**Visualization quality issues:**
- Check matplotlib version compatibility
- Verify DPI settings
- Check for font issues
- Verify color settings

**File size too large:**
- Reduce DPI from 300 to 150
- Check image format (should be JPG)
- Verify no unnecessary data duplication


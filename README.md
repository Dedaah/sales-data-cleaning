# Sales Data Cleaning and Business Analysis

## Project Overview
This project uses Python and pandas to clean a sales dataset stored in a CSV file and perform basic business analysis. It demonstrates how raw sales data can be prepared for analysis and used to explore revenue by product and region.

## Objectives
- Load and inspect a CSV dataset using pandas.
- Identify missing values, duplicate records, and inconsistent data.
- Standardize customer names and region labels.
- Convert quantity and unit-price columns to numeric data types.
- Calculate sales revenue for individual orders.
- Analyse total revenue by product and region.
- Export the cleaned dataset to a new CSV file.

## Tools and Technologies
- **Python**
- **pandas**
- **CSV files**
- **Visual Studio Code**
- **GitHub**

## Dataset
The project uses a practice sales dataset containing the following fields:

- `Order_ID`
- `Order_Date`
- `Customer`
- `Region`
- `Product`
- `Quantity`
- `Unit_Price`

The dataset includes intentional data-quality issues for cleaning practice, such as missing values, inconsistent capitalization and spacing, and values requiring numeric conversion.

## Data Cleaning Process
The project includes the following steps:

1. Loaded the original CSV file into a pandas DataFrame.
2. Inspected the dataset's structure, columns, and data types.
3. Checked for missing values and duplicate records.
4. Standardized customer names and region labels.
5. Converted quantity and unit-price values to numeric types.
6. Filtered out records with missing quantities or unit prices before calculating sales.
7. Created a `Sales` column using the formula:

   `Sales = Quantity × Unit_Price`

## Business Analysis
The project calculates and examines:

- Total revenue across the retained sales records.
- Revenue by product.
- Revenue by region.

These summaries can help illustrate how sales performance differs across products and regions.

## Project Files
- `sales_data.csv` — Original practice dataset.
- `sales_data_cleaning.py` — Python script used for cleaning and analysis.
- `cleaned_sales_data.csv` — Exported dataset after the cleaning steps.

## How to Run the Project
1. Install Python.
2. Install pandas by running `pip install pandas` in your terminal.
3. Place the original CSV file in the same folder as the Python script.
4. Run the script:

   `python sales_data_cleaning.py`

5. The script processes the dataset and exports `cleaned_sales_data.csv`.

## Learning Outcomes
This project provided practical experience with pandas DataFrames, data inspection, missing-value checks, conditional filtering, data standardization, numeric conversion, grouping, aggregation, and CSV export.

## Notes and Limitations
This is a learning project using practice data. Rows with missing quantities or unit prices were excluded from the cleaned dataset used for revenue calculations. The analysis is limited to the fields available in the dataset and does not establish causes for differences in sales performance.

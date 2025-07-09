# Tesla Stock Exploratory Data Analysis (EDA)

## Overview
This project performs an exploratory data analysis (EDA) on historical Tesla stock data using Python. The goal is to clean, analyze, and visualize the data to extract insights and prepare it for further analysis or dashboarding in Power BI.

## Dataset
- **File:** Tasla_Stock_Updated_V2.csv
- **Columns:** Date, Open, High, Low, Close, Volume
- **Description:** Daily stock prices and trading volume for Tesla over several years.

## Steps Performed

### 1. Data Loading & Inspection
- Loaded the dataset using pandas.
- Displayed the first few rows and checked data types and missing values.

### 2. Data Cleaning
- Removed unnecessary index columns (if present).
- Converted the 'Date' column to datetime and set it as the index.
- Ensured all price and volume columns are numeric.
- Removed duplicate rows.
- Dropped rows with missing values.

### 3. Feature Engineering
- Calculated **Daily Returns** (percentage change in closing price).
- Computed **7-day** and **30-day Moving Averages** of the closing price.

### 4. Exploratory Visualizations
- **Time Series Plots:** Closing price and trading volume over time.
- **Correlation Heatmap:** Relationships between numerical columns.
- **Distribution Plots:** Histograms of closing price, trading volume, and daily returns.
- **Boxplots:** For open, high, low, and close prices to detect outliers.
- **Moving Averages Plot:** Visualizes trends and smoothing.
- **Scatter Plot:** Volume vs. closing price.

### 5. Export for Power BI
- The cleaned and feature-enriched dataset is exported as `Tesla_Stock_Cleaned.csv` for easy import into Power BI or other BI tools.

## Outcomes & Insights
- **Data Quality:** The dataset was cleaned of duplicates, missing values, and unnecessary columns, ensuring reliability for analysis.
- **Trends:** Time series and moving averages reveal long-term trends and short-term fluctuations in Tesla's stock price.
- **Volatility:** Daily returns histogram shows the distribution and volatility of price changes.
- **Volume Analysis:** Volume trends and its relationship with price are visualized.
- **Outliers:** Boxplots help identify unusual price movements.
- **Correlation:** The heatmap highlights relationships between price and volume.

## How to Use
1. Run the `lab_work.py` script or the Jupyter notebook to perform EDA and export the cleaned data.
2. Use `Tesla_Stock_Cleaned.csv` as a data source in Power BI for dashboarding and further analysis.

## Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

Install requirements with:
```bash
pip install pandas matplotlib seaborn numpy
```

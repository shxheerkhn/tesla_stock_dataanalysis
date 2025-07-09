import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(r'C:\Users\PC\OneDrive\Documents\Data Analytics Work\Tasla_Stock_Updated_V2.csv')

# Display first few rows

pd.display(df.head())

# Data info
df.info()

print('Missing values per column:')
print(df.isnull().sum())

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as index
df.set_index('Date', inplace=True)

# Basic statistics
print(df.describe())

# Plot closing price over time
plt.figure(figsize=(12, 6))
plt.plot(df['Close'])
plt.title('Tesla Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()

# Volume over time
plt.figure(figsize=(12, 4))
plt.plot(df['Volume'], color='orange')
plt.title('Tesla Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# --- Data Cleaning ---
# Remove unnamed index column if present
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Remove duplicates
df = df.drop_duplicates()

# Check for missing values and drop rows with any missing data
print('Missing values per column after cleaning:')
print(df.isnull().sum())
df = df.dropna()

# Ensure correct data types
for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# --- Feature Engineering ---
# Daily returns
df['Daily_Return'] = df['Close'].pct_change()
# 7-day and 30-day moving averages
df['MA_7'] = df['Close'].rolling(window=7).mean()
df['MA_30'] = df['Close'].rolling(window=30).mean()

# Distribution of Close prices
plt.figure(figsize=(10, 5))
sns.histplot(df['Close'], bins=50, kde=True)
plt.title('Distribution of Closing Prices')
plt.xlabel('Close Price')
plt.ylabel('Frequency')
plt.show()

# Distribution of Volume
plt.figure(figsize=(10, 5))
sns.histplot(df['Volume'], bins=50, kde=True, color='orange')
plt.title('Distribution of Trading Volume')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.show()

# Boxplots for price columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Open', 'High', 'Low', 'Close']])
plt.title('Boxplot of Price Columns')
plt.show()

# Moving averages plot
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close', alpha=0.5)
plt.plot(df['MA_7'], label='7-Day MA')
plt.plot(df['MA_30'], label='30-Day MA')
plt.title('Close Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Daily returns histogram
plt.figure(figsize=(10, 5))
sns.histplot(df['Daily_Return'].dropna(), bins=50, kde=True, color='green')
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Volume vs. Close
plt.figure(figsize=(10, 6))
plt.scatter(df['Volume'], df['Close'], alpha=0.5)
plt.title('Volume vs. Close Price')
plt.xlabel('Volume')
plt.ylabel('Close Price')
plt.show()

# --- Export Cleaned Data for Power BI ---
df.to_csv('Tesla_Stock_Cleaned.csv')
print('Cleaned data exported to Tesla_Stock_Cleaned.csv')


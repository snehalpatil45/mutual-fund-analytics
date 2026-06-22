import pandas as pd
import os

# Load dataset
file_path = os.path.join("data", "raw", "01_fund_master.csv")

df = pd.read_csv(file_path)

print("="*50)
print("FUND MASTER DATASET ANALYSIS")
print("="*50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFund Houses:")
print(df['fund_house'].value_counts())

print("\nCategories:")
print(df['category'].value_counts())

print("\nSub Categories:")
print(df['sub_category'].value_counts())

print("\nRisk Categories:")
print(df['risk_category'].value_counts())

print("\nTop 10 Fund Managers:")
print(df['fund_manager'].value_counts().head(10))
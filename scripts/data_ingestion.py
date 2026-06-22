import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to raw data folder
folder = os.path.join(BASE_DIR, "data", "raw")

print("Data Ingestion Started...")
print(f"Reading files from: {folder}")

# Check if folder exists
if not os.path.exists(folder):
    print("Error: data/raw folder not found!")
    exit()

# Read all CSV files
for file in os.listdir(folder):
    if file.endswith(".csv"):
        file_path = os.path.join(folder, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "=" * 50)
            print(f"File Name: {file}")
            print(f"Shape: {df.shape}")

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")

print("\nData Ingestion Completed Successfully!")
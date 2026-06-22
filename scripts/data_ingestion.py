# data_ingestion.py

import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder, file))

        print("\n", "="*50)
        print(file)
        print("Shape:", df.shape)
        print("Data Types:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())
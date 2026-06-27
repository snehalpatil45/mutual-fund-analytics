import pandas as pd

df = pd.read_csv('data/raw/02_nav_history.csv')
print("BEFORE CLEANING:", df.shape)
print(df.head(3))

# 1. Parse date to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 2. Sort by amfi_code + date
df = df.sort_values(['amfi_code', 'date']).reset_index(drop=True)

# 3. Forward-fill missing NAV for holidays/weekends
df['nav'] = df.groupby('amfi_code')['nav'].ffill()

# 4. Remove duplicates
before = len(df)
df = df.drop_duplicates(subset=['amfi_code', 'date'])
print(f"Duplicates removed: {before - len(df)}")

# 5. Validate NAV > 0
df = df[df['nav'] > 0]

# 6. Standardise date format
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

print("AFTER CLEANING:", df.shape)
df.to_csv('data/processed/nav_history_clean.csv', index=False)
print("✅ Saved → data/processed/nav_history_clean.csv")
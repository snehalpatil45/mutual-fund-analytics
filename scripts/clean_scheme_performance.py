import pandas as pd

df = pd.read_csv('data/raw/07_scheme_performance.csv')
print("BEFORE CLEANING:", df.shape)

# 1. Validate all return columns are numeric  ← correct column names
return_cols = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct',
               'benchmark_3yr_pct', 'alpha', 'beta',
               'sharpe_ratio', 'sortino_ratio']
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 2. Flag anomalies (return > 200% or < -100%)
df['anomaly_flag'] = df[['return_1yr_pct','return_3yr_pct','return_5yr_pct']].apply(
    lambda row: 1 if any(row > 200) or any(row < -100) else 0, axis=1
)
print(f"Anomalies flagged: {df['anomaly_flag'].sum()}")

# 3. Validate expense_ratio range (0.1 - 2.5)  ← correct column name
invalid_exp = df[~df['expense_ratio_pct'].between(0.1, 2.5)]
print(f"Invalid expense_ratio rows: {len(invalid_exp)}")
if len(invalid_exp) > 0:
    print(invalid_exp[['scheme_name','expense_ratio_pct']])

print("AFTER CLEANING:", df.shape)
df.to_csv('data/processed/scheme_performance_clean.csv', index=False)
print("✅ Saved → data/processed/scheme_performance_clean.csv")
import pandas as pd

# ── 03_aum_by_fund_house.csv ─────────────────────────────────────
df = pd.read_csv('data/raw/03_aum_by_fund_house.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['date'] = df['date'].dt.strftime('%Y-%m-%d')
df = df.dropna()
df.to_csv('data/processed/aum_by_fund_house_clean.csv', index=False)
print(f"✅ aum_by_fund_house_clean.csv → {df.shape}")

# ── 04_monthly_sip_inflows.csv ───────────────────────────────────
df = pd.read_csv('data/raw/04_monthly_sip_inflows.csv')
df['month'] = pd.to_datetime(df['month'], format='%Y-%m', errors='coerce')
# yoy_growth_pct has 12 nulls — forward fill
df['yoy_growth_pct'] = df['yoy_growth_pct'].ffill()
df['month'] = df['month'].dt.strftime('%Y-%m')
df.to_csv('data/processed/monthly_sip_inflows_clean.csv', index=False)
print(f"✅ monthly_sip_inflows_clean.csv → {df.shape}")

# ── 05_category_inflows.csv ──────────────────────────────────────
df = pd.read_csv('data/raw/05_category_inflows.csv')
df['month'] = pd.to_datetime(df['month'], format='%Y-%m', errors='coerce')
df['month'] = df['month'].dt.strftime('%Y-%m')
df = df[df['net_inflow_crore'].notna()]
df.to_csv('data/processed/category_inflows_clean.csv', index=False)
print(f"✅ category_inflows_clean.csv → {df.shape}")

# ── 06_industry_folio_count.csv ──────────────────────────────────
df = pd.read_csv('data/raw/06_industry_folio_count.csv')
df['month'] = pd.to_datetime(df['month'], format='%Y-%m', errors='coerce')
df['month'] = df['month'].dt.strftime('%Y-%m')
df.to_csv('data/processed/industry_folio_count_clean.csv', index=False)
print(f"✅ industry_folio_count_clean.csv → {df.shape}")

# ── 09_portfolio_holdings.csv ────────────────────────────────────
df = pd.read_csv('data/raw/09_portfolio_holdings.csv')
df['portfolio_date'] = pd.to_datetime(df['portfolio_date'], errors='coerce')
df['portfolio_date'] = df['portfolio_date'].dt.strftime('%Y-%m-%d')
df = df[df['weight_pct'] > 0]
df = df[df['market_value_cr'] > 0]
df.to_csv('data/processed/portfolio_holdings_clean.csv', index=False)
print(f"✅ portfolio_holdings_clean.csv → {df.shape}")

# ── 10_benchmark_indices.csv ─────────────────────────────────────
df = pd.read_csv('data/raw/10_benchmark_indices.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.sort_values(['index_name', 'date'])
df = df.drop_duplicates(subset=['index_name', 'date'])
df = df[df['close_value'] > 0]
df['date'] = df['date'].dt.strftime('%Y-%m-%d')
df.to_csv('data/processed/benchmark_indices_clean.csv', index=False)
print(f"✅ benchmark_indices_clean.csv → {df.shape}")

# ── 01_fund_master.csv ───────────────────────────────────────────
df = pd.read_csv('data/raw/01_fund_master.csv')
df['launch_date'] = pd.to_datetime(df['launch_date'], errors='coerce')
df['launch_date'] = df['launch_date'].dt.strftime('%Y-%m-%d')
df = df[df['expense_ratio_pct'].between(0.1, 2.5)]
df.to_csv('data/processed/fund_master_clean.csv', index=False)
print(f"✅ fund_master_clean.csv → {df.shape}")

print("\n🎉 All files cleaned!")
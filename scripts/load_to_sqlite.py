import pandas as pd
from sqlalchemy import create_engine, text
import sqlite3

engine = create_engine('sqlite:///bluestock_mf.db')

# Apply schema
with open('sql/schema.sql', 'r') as f:
    schema = f.read()
conn = sqlite3.connect('bluestock_mf.db')
conn.executescript(schema)
conn.close()
print("✅ Schema applied")

# Load all cleaned files
tables = {
    'dim_fund':               'data/processed/fund_master_clean.csv',
    'fact_nav':               'data/processed/nav_history_clean.csv',
    'fact_transactions':      'data/processed/investor_transactions_clean.csv',
    'fact_performance':       'data/processed/scheme_performance_clean.csv',
    'fact_aum':               'data/processed/aum_by_fund_house_clean.csv',
    'fact_portfolio_holdings':'data/processed/portfolio_holdings_clean.csv',
    'fact_benchmark':         'data/processed/benchmark_indices_clean.csv',
}

for table, path in tables.items():
    df = pd.read_csv(path)
    df.to_sql(table, engine, if_exists='replace', index=False)
    print(f"✅ {table:30s} → {len(df)} rows loaded")

# Verify row counts match source
print("\n=== VERIFICATION: DB vs Processed CSV ===")
with engine.connect() as con:
    for table in tables.keys():
        count = con.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
        print(f"  {table:30s}: {count} rows in DB")
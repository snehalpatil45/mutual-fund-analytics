import pandas as pd

files = {
    'fund_master':          'data/raw/01_fund_master.csv',
    'nav_history':          'data/raw/02_nav_history.csv',
    'aum_by_fund_house':    'data/raw/03_aum_by_fund_house.csv',
    'monthly_sip_inflows':  'data/raw/04_monthly_sip_inflows.csv',
    'category_inflows':     'data/raw/05_category_inflows.csv',
    'industry_folio_count': 'data/raw/06_industry_folio_count.csv',
    'scheme_performance':   'data/raw/07_scheme_performance.csv',
    'investor_transactions':'data/raw/08_investor_transactions.csv',
    'portfolio_holdings':   'data/raw/09_portfolio_holdings.csv',
    'benchmark_indices':    'data/raw/10_benchmark_indices.csv',
}

for name, path in files.items():
    try:
        df = pd.read_csv(path)
        print(f"\n{'='*60}")
        print(f"FILE : {path}")
        print(f"Shape: {df.shape}")
        print(f"Cols : {list(df.columns)}")
        print(f"Head :\n{df.head(2)}")
        print(f"Nulls: {df.isnull().sum().to_dict()}")
    except Exception as e:
        print(f"❌ {path} → {e}")
import pandas as pd
from datetime import date

files = {
    'fund_master_clean':          'data/processed/fund_master_clean.csv',
    'nav_history_clean':          'data/processed/nav_history_clean.csv',
    'investor_transactions_clean':'data/processed/investor_transactions_clean.csv',
    'scheme_performance_clean':   'data/processed/scheme_performance_clean.csv',
    'aum_by_fund_house_clean':    'data/processed/aum_by_fund_house_clean.csv',
    'monthly_sip_inflows_clean':  'data/processed/monthly_sip_inflows_clean.csv',
    'category_inflows_clean':     'data/processed/category_inflows_clean.csv',
    'industry_folio_count_clean': 'data/processed/industry_folio_count_clean.csv',
    'portfolio_holdings_clean':   'data/processed/portfolio_holdings_clean.csv',
    'benchmark_indices_clean':    'data/processed/benchmark_indices_clean.csv',
}

# Business definitions for every column
col_definitions = {
    # fund_master
    'amfi_code':            'Unique AMFI scheme code assigned by AMFI India',
    'fund_house':           'Name of the Asset Management Company (AMC)',
    'scheme_name':          'Full official name of the mutual fund scheme',
    'category':             'Broad category — Equity / Debt / Hybrid',
    'sub_category':         'Detailed category — Large Cap / Mid Cap / ELSS etc.',
    'plan':                 'Regular or Direct plan',
    'launch_date':          'Date when the scheme was launched',
    'benchmark':            'Index used to compare fund performance (e.g. NIFTY 100)',
    'expense_ratio_pct':    'Annual fee charged by AMC as % of AUM (valid range: 0.1–2.5%)',
    'exit_load_pct':        'Fee charged on redemption before specified period',
    'min_sip_amount':       'Minimum monthly SIP investment amount in INR',
    'min_lumpsum_amount':   'Minimum one-time investment amount in INR',
    'fund_manager':         'Name of the fund manager handling the scheme',
    'risk_category':        'Risk level — Low / Moderate / High / Very High',
    'sebi_category_code':   'SEBI assigned category code for the scheme',

    # nav_history
    'date':                 'Date of NAV in YYYY-MM-DD format',
    'nav':                  'Net Asset Value per unit on that date (must be > 0)',

    # investor_transactions
    'investor_id':          'Unique identifier for each investor',
    'transaction_date':     'Date when the transaction was executed (YYYY-MM-DD)',
    'transaction_type':     'Type of transaction — SIP / Lumpsum / Redemption',
    'amount_inr':           'Transaction amount in Indian Rupees (must be > 0)',
    'state':                'Indian state where the investor is located',
    'city':                 'City of the investor',
    'city_tier':            'City classification — Tier 1 / Tier 2 / Tier 3',
    'age_group':            'Age bracket of the investor (e.g. 25-34)',
    'gender':               'Gender of the investor — Male / Female / Other',
    'annual_income_lakh':   'Annual income of investor in lakhs INR',
    'payment_mode':         'Payment method — UPI / Cheque / Net Banking etc.',
    'kyc_status':           'KYC verification status — Verified / Pending / Rejected',

    # scheme_performance
    'return_1yr_pct':       '1-year absolute return percentage',
    'return_3yr_pct':       '3-year CAGR return percentage',
    'return_5yr_pct':       '5-year CAGR return percentage',
    'benchmark_3yr_pct':    '3-year benchmark index return for comparison',
    'alpha':                'Excess return over benchmark (risk-adjusted)',
    'beta':                 'Sensitivity of fund to market movements',
    'sharpe_ratio':         'Return per unit of total risk taken',
    'sortino_ratio':        'Return per unit of downside risk taken',
    'std_dev_ann_pct':      'Annualised standard deviation of returns (volatility)',
    'max_drawdown_pct':     'Maximum peak-to-trough decline in fund value',
    'aum_crore':            'Assets Under Management in crore INR',
    'morningstar_rating':   'Morningstar star rating (1–5)',
    'risk_grade':           'Risk classification — Low / Moderate / High',
    'anomaly_flag':         'Derived flag: 1 = anomalous return detected, 0 = normal',

    # aum_by_fund_house
    'aum_lakh_crore':       'Total AUM of fund house in lakh crore INR',
    'num_schemes':          'Total number of schemes offered by the fund house',

    # monthly_sip_inflows
    'month':                'Month in YYYY-MM format',
    'sip_inflow_crore':     'Total SIP inflow across industry in crore INR',
    'active_sip_accounts_crore': 'Number of active SIP accounts in crore',
    'new_sip_accounts_lakh':'New SIP accounts registered in lakh',
    'sip_aum_lakh_crore':   'Total SIP AUM in lakh crore INR',
    'yoy_growth_pct':       'Year-on-year growth % of SIP inflows (forward-filled for missing)',

    # category_inflows
    'net_inflow_crore':     'Net inflow into the category in crore INR',

    # industry_folio_count
    'total_folios_crore':   'Total investor folios across industry in crore',
    'equity_folios_crore':  'Equity category folios in crore',
    'debt_folios_crore':    'Debt category folios in crore',
    'hybrid_folios_crore':  'Hybrid category folios in crore',
    'others_folios_crore':  'Other category folios in crore',

    # portfolio_holdings
    'stock_symbol':         'NSE/BSE ticker symbol of the stock',
    'stock_name':           'Full name of the stock/company',
    'sector':               'Industry sector of the stock',
    'weight_pct':           'Portfolio allocation % to this stock (must be > 0)',
    'market_value_cr':      'Current market value of holding in crore INR',
    'current_price_inr':    'Current stock price in INR',
    'portfolio_date':       'Date of portfolio snapshot (YYYY-MM-DD)',

    # benchmark_indices
    'index_name':           'Name of the benchmark index (e.g. NIFTY50, SENSEX)',
    'close_value':          'Closing value of the index on that date (must be > 0)',
}

# Source file labels
source_labels = {
    'fund_master_clean':           '01_fund_master.csv',
    'nav_history_clean':           '02_nav_history.csv',
    'aum_by_fund_house_clean':     '03_aum_by_fund_house.csv',
    'monthly_sip_inflows_clean':   '04_monthly_sip_inflows.csv',
    'category_inflows_clean':      '05_category_inflows.csv',
    'industry_folio_count_clean':  '06_industry_folio_count.csv',
    'scheme_performance_clean':    '07_scheme_performance.csv',
    'investor_transactions_clean': '08_investor_transactions.csv',
    'portfolio_holdings_clean':    '09_portfolio_holdings.csv',
    'benchmark_indices_clean':     '10_benchmark_indices.csv',
}

# Build markdown
lines = []
lines.append("# Data Dictionary — Bluestock MF Analytics")
lines.append(f"\n**Project:** Capstone Project I – Mutual Fund Analytics")
lines.append(f"**Created:** {date.today().strftime('%d %B %Y')}")
lines.append(f"**Total Files:** {len(files)}")
lines.append("\n---\n")
lines.append("## Table of Contents\n")

for i, name in enumerate(files.keys(), 1):
    lines.append(f"{i}. [{name}](#{name.replace('_','-')})")

lines.append("\n---\n")

for name, path in files.items():
    try:
        df = pd.read_csv(path)
        source = source_labels.get(name, 'Unknown')

        lines.append(f"## {name}")
        lines.append(f"\n**Source File:** `data/raw/{source}`")
        lines.append(f"**Cleaned File:** `data/processed/{name}.csv`")
        lines.append(f"**Rows:** {len(df):,} &nbsp; **Columns:** {len(df.columns)}")
        lines.append("\n| Column | Data Type | Sample Value | Business Definition |")
        lines.append("|--------|-----------|--------------|---------------------|")

        for col in df.columns:
            dtype    = str(df[col].dtype)
            sample   = str(df[col].dropna().iloc[0]) if len(df[col].dropna()) > 0 else 'N/A'
            # truncate long samples
            if len(sample) > 40:
                sample = sample[:37] + '...'
            definition = col_definitions.get(col, 'No definition provided')
            lines.append(f"| `{col}` | {dtype} | {sample} | {definition} |")

        lines.append("\n---\n")
        print(f"✅ Done: {name} ({len(df.columns)} columns)")

    except FileNotFoundError:
        lines.append(f"## {name}")
        lines.append(f"\n⚠️ File not found: `{path}`\n")
        lines.append("\n---\n")
        print(f"⚠️  Skipped (file not found): {path}")

# Write the file
with open('data_dictionary.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("\n🎉 data_dictionary.md created successfully!")
print("📄 Location: data_dictionary.md")
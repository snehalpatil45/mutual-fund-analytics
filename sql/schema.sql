CREATE TABLE IF NOT EXISTS dim_fund (
    fund_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code          INTEGER UNIQUE NOT NULL,
    fund_house         TEXT,
    scheme_name        TEXT,
    category           TEXT,
    sub_category       TEXT,
    plan               TEXT,
    launch_date        TEXT,
    benchmark          TEXT,
    expense_ratio_pct  REAL,
    exit_load_pct      REAL,
    min_sip_amount     REAL,
    min_lumpsum_amount REAL,
    fund_manager       TEXT,
    risk_category      TEXT,
    sebi_category_code TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    date       TEXT UNIQUE NOT NULL,
    year       INTEGER,
    month      INTEGER,
    quarter    INTEGER,
    day        INTEGER,
    is_weekend INTEGER
);

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER REFERENCES dim_fund(amfi_code),
    date      TEXT,
    nav       REAL CHECK(nav > 0)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    txn_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id      TEXT,
    transaction_date TEXT,
    amfi_code        INTEGER REFERENCES dim_fund(amfi_code),
    transaction_type TEXT CHECK(transaction_type IN ('SIP','Lumpsum','Redemption')),
    amount_inr       REAL CHECK(amount_inr > 0),
    state            TEXT,
    city             TEXT,
    city_tier        TEXT,
    age_group        TEXT,
    gender           TEXT,
    annual_income_lakh REAL,
    payment_mode     TEXT,
    kyc_status       TEXT
);

CREATE TABLE IF NOT EXISTS fact_performance (
    perf_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code          INTEGER REFERENCES dim_fund(amfi_code),
    scheme_name        TEXT,
    return_1yr_pct     REAL,
    return_3yr_pct     REAL,
    return_5yr_pct     REAL,
    benchmark_3yr_pct  REAL,
    alpha              REAL,
    beta               REAL,
    sharpe_ratio       REAL,
    sortino_ratio      REAL,
    std_dev_ann_pct    REAL,
    max_drawdown_pct   REAL,
    aum_crore          REAL,
    expense_ratio_pct  REAL,
    morningstar_rating INTEGER,
    risk_grade         TEXT,
    anomaly_flag       INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    date           TEXT,
    fund_house     TEXT,
    aum_lakh_crore REAL,
    aum_crore      REAL,
    num_schemes    INTEGER
);

CREATE TABLE IF NOT EXISTS fact_portfolio_holdings (
    holding_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code         INTEGER REFERENCES dim_fund(amfi_code),
    stock_symbol      TEXT,
    stock_name        TEXT,
    sector            TEXT,
    weight_pct        REAL,
    market_value_cr   REAL,
    current_price_inr REAL,
    portfolio_date    TEXT
);

CREATE TABLE IF NOT EXISTS fact_benchmark (
    benchmark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date         TEXT,
    index_name   TEXT,
    close_value  REAL
);
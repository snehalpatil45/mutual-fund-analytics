# Data Dictionary — Bluestock MF Analytics

**Project:** Capstone Project I – Mutual Fund Analytics
**Created:** 27 June 2026
**Total Files:** 10

---

## Table of Contents

1. [fund_master_clean](#fund-master-clean)
2. [nav_history_clean](#nav-history-clean)
3. [investor_transactions_clean](#investor-transactions-clean)
4. [scheme_performance_clean](#scheme-performance-clean)
5. [aum_by_fund_house_clean](#aum-by-fund-house-clean)
6. [monthly_sip_inflows_clean](#monthly-sip-inflows-clean)
7. [category_inflows_clean](#category-inflows-clean)
8. [industry_folio_count_clean](#industry-folio-count-clean)
9. [portfolio_holdings_clean](#portfolio-holdings-clean)
10. [benchmark_indices_clean](#benchmark-indices-clean)

---

## fund_master_clean

**Source File:** `data/raw/01_fund_master.csv`
**Cleaned File:** `data/processed/fund_master_clean.csv`
**Rows:** 40 &nbsp; **Columns:** 15

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `amfi_code` | int64 | 119551 | Unique AMFI scheme code assigned by AMFI India |
| `fund_house` | str | SBI Mutual Fund | Name of the Asset Management Company (AMC) |
| `scheme_name` | str | SBI Bluechip Fund - Regular Plan - Gr... | Full official name of the mutual fund scheme |
| `category` | str | Equity | Broad category — Equity / Debt / Hybrid |
| `sub_category` | str | Large Cap | Detailed category — Large Cap / Mid Cap / ELSS etc. |
| `plan` | str | Regular | Regular or Direct plan |
| `launch_date` | str | 2006-02-14 | Date when the scheme was launched |
| `benchmark` | str | NIFTY 100 TRI | Index used to compare fund performance (e.g. NIFTY 100) |
| `expense_ratio_pct` | float64 | 1.54 | Annual fee charged by AMC as % of AUM (valid range: 0.1–2.5%) |
| `exit_load_pct` | float64 | 1.0 | Fee charged on redemption before specified period |
| `min_sip_amount` | int64 | 500 | Minimum monthly SIP investment amount in INR |
| `min_lumpsum_amount` | int64 | 1000 | Minimum one-time investment amount in INR |
| `fund_manager` | str | Sohini Andani | Name of the fund manager handling the scheme |
| `risk_category` | str | Moderate | Risk level — Low / Moderate / High / Very High |
| `sebi_category_code` | str | EC01 | SEBI assigned category code for the scheme |

---

## nav_history_clean

**Source File:** `data/raw/02_nav_history.csv`
**Cleaned File:** `data/processed/nav_history_clean.csv`
**Rows:** 46,000 &nbsp; **Columns:** 3

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `amfi_code` | int64 | 100016 | Unique AMFI scheme code assigned by AMFI India |
| `date` | str | 2022-01-03 | Date of NAV in YYYY-MM-DD format |
| `nav` | float64 | 520.4608 | Net Asset Value per unit on that date (must be > 0) |

---

## investor_transactions_clean

**Source File:** `data/raw/08_investor_transactions.csv`
**Cleaned File:** `data/processed/investor_transactions_clean.csv`
**Rows:** 32,778 &nbsp; **Columns:** 13

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `investor_id` | str | INV003054 | Unique identifier for each investor |
| `transaction_date` | str | 2024-01-01 | Date when the transaction was executed (YYYY-MM-DD) |
| `amfi_code` | int64 | 119092 | Unique AMFI scheme code assigned by AMFI India |
| `transaction_type` | str | SIP | Type of transaction — SIP / Lumpsum / Redemption |
| `amount_inr` | int64 | 1834 | Transaction amount in Indian Rupees (must be > 0) |
| `state` | str | Telangana | Indian state where the investor is located |
| `city` | str | Hyderabad | City of the investor |
| `city_tier` | str | T30 | City classification — Tier 1 / Tier 2 / Tier 3 |
| `age_group` | str | 56+ | Age bracket of the investor (e.g. 25-34) |
| `gender` | str | Female | Gender of the investor — Male / Female / Other |
| `annual_income_lakh` | float64 | 77.1 | Annual income of investor in lakhs INR |
| `payment_mode` | str | UPI | Payment method — UPI / Cheque / Net Banking etc. |
| `kyc_status` | str | Verified | KYC verification status — Verified / Pending / Rejected |

---

## scheme_performance_clean

**Source File:** `data/raw/07_scheme_performance.csv`
**Cleaned File:** `data/processed/scheme_performance_clean.csv`
**Rows:** 40 &nbsp; **Columns:** 20

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `amfi_code` | int64 | 119551 | Unique AMFI scheme code assigned by AMFI India |
| `scheme_name` | str | SBI Bluechip Fund - Regular Plan - Gr... | Full official name of the mutual fund scheme |
| `fund_house` | str | SBI Mutual Fund | Name of the Asset Management Company (AMC) |
| `category` | str | Large Cap | Broad category — Equity / Debt / Hybrid |
| `plan` | str | Regular | Regular or Direct plan |
| `return_1yr_pct` | float64 | 12.42 | 1-year absolute return percentage |
| `return_3yr_pct` | float64 | 12.36 | 3-year CAGR return percentage |
| `return_5yr_pct` | float64 | 14.45 | 5-year CAGR return percentage |
| `benchmark_3yr_pct` | float64 | 11.49 | 3-year benchmark index return for comparison |
| `alpha` | float64 | 0.87 | Excess return over benchmark (risk-adjusted) |
| `beta` | float64 | 0.89 | Sensitivity of fund to market movements |
| `sharpe_ratio` | float64 | 0.88 | Return per unit of total risk taken |
| `sortino_ratio` | float64 | 1.29 | Return per unit of downside risk taken |
| `std_dev_ann_pct` | float64 | 14.0 | Annualised standard deviation of returns (volatility) |
| `max_drawdown_pct` | float64 | -21.7 | Maximum peak-to-trough decline in fund value |
| `aum_crore` | int64 | 14288 | Assets Under Management in crore INR |
| `expense_ratio_pct` | float64 | 1.54 | Annual fee charged by AMC as % of AUM (valid range: 0.1–2.5%) |
| `morningstar_rating` | int64 | 4 | Morningstar star rating (1–5) |
| `risk_grade` | str | Moderate | Risk classification — Low / Moderate / High |
| `anomaly_flag` | int64 | 0 | Derived flag: 1 = anomalous return detected, 0 = normal |

---

## aum_by_fund_house_clean

**Source File:** `data/raw/03_aum_by_fund_house.csv`
**Cleaned File:** `data/processed/aum_by_fund_house_clean.csv`
**Rows:** 90 &nbsp; **Columns:** 5

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `date` | str | 2022-03-31 | Date of NAV in YYYY-MM-DD format |
| `fund_house` | str | SBI Mutual Fund | Name of the Asset Management Company (AMC) |
| `aum_lakh_crore` | float64 | 6.05 | Total AUM of fund house in lakh crore INR |
| `aum_crore` | int64 | 605000 | Assets Under Management in crore INR |
| `num_schemes` | int64 | 186 | Total number of schemes offered by the fund house |

---

## monthly_sip_inflows_clean

**Source File:** `data/raw/04_monthly_sip_inflows.csv`
**Cleaned File:** `data/processed/monthly_sip_inflows_clean.csv`
**Rows:** 48 &nbsp; **Columns:** 6

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `month` | str | 2022-01 | Month in YYYY-MM format |
| `sip_inflow_crore` | int64 | 11517 | Total SIP inflow across industry in crore INR |
| `active_sip_accounts_crore` | float64 | 4.91 | Number of active SIP accounts in crore |
| `new_sip_accounts_lakh` | float64 | 9.1 | New SIP accounts registered in lakh |
| `sip_aum_lakh_crore` | float64 | 4.8 | Total SIP AUM in lakh crore INR |
| `yoy_growth_pct` | float64 | 20.31 | Year-on-year growth % of SIP inflows (forward-filled for missing) |

---

## category_inflows_clean

**Source File:** `data/raw/05_category_inflows.csv`
**Cleaned File:** `data/processed/category_inflows_clean.csv`
**Rows:** 144 &nbsp; **Columns:** 3

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `month` | str | 2024-04 | Month in YYYY-MM format |
| `category` | str | Large Cap | Broad category — Equity / Debt / Hybrid |
| `net_inflow_crore` | float64 | 2413.0 | Net inflow into the category in crore INR |

---

## industry_folio_count_clean

**Source File:** `data/raw/06_industry_folio_count.csv`
**Cleaned File:** `data/processed/industry_folio_count_clean.csv`
**Rows:** 21 &nbsp; **Columns:** 6

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `month` | str | 2022-01 | Month in YYYY-MM format |
| `total_folios_crore` | float64 | 13.26 | Total investor folios across industry in crore |
| `equity_folios_crore` | float64 | 9.28 | Equity category folios in crore |
| `debt_folios_crore` | float64 | 1.86 | Debt category folios in crore |
| `hybrid_folios_crore` | float64 | 0.8 | Hybrid category folios in crore |
| `others_folios_crore` | float64 | 1.33 | Other category folios in crore |

---

## portfolio_holdings_clean

**Source File:** `data/raw/09_portfolio_holdings.csv`
**Cleaned File:** `data/processed/portfolio_holdings_clean.csv`
**Rows:** 322 &nbsp; **Columns:** 8

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `amfi_code` | int64 | 119551 | Unique AMFI scheme code assigned by AMFI India |
| `stock_symbol` | str | POWERGRID | NSE/BSE ticker symbol of the stock |
| `stock_name` | str | Power Grid Corporation | Full name of the stock/company |
| `sector` | str | Utilities | Industry sector of the stock |
| `weight_pct` | float64 | 13.85 | Portfolio allocation % to this stock (must be > 0) |
| `market_value_cr` | float64 | 737.09 | Current market value of holding in crore INR |
| `current_price_inr` | float64 | 6011.08 | Current stock price in INR |
| `portfolio_date` | str | 2025-12-31 | Date of portfolio snapshot (YYYY-MM-DD) |

---

## benchmark_indices_clean

**Source File:** `data/raw/10_benchmark_indices.csv`
**Cleaned File:** `data/processed/benchmark_indices_clean.csv`
**Rows:** 8,050 &nbsp; **Columns:** 3

| Column | Data Type | Sample Value | Business Definition |
|--------|-----------|--------------|---------------------|
| `date` | str | 2022-01-03 | Date of NAV in YYYY-MM-DD format |
| `index_name` | str | BSE_SMALLCAP | Name of the benchmark index (e.g. NIFTY50, SENSEX) |
| `close_value` | float64 | 26554.6 | Closing value of the index on that date (must be > 0) |

---

-- Q1: Top 5 funds by AUM (crore)
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC LIMIT 5;

-- Q2: Average NAV per month
SELECT SUBSTR(date,1,7) AS month, ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month ORDER BY month;

-- Q3: SIP YoY growth
SELECT SUBSTR(transaction_date,1,4) AS year,
       COUNT(*) AS sip_count,
       ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year ORDER BY year;

-- Q4: Transactions by state
SELECT state, COUNT(*) AS txn_count, ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state ORDER BY txn_count DESC;

-- Q5: Funds with expense_ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- Q6: Top 10 funds by 1-year return
SELECT f.scheme_name, p.return_1yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
WHERE p.anomaly_flag = 0
ORDER BY p.return_1yr_pct DESC LIMIT 10;

-- Q7: Monthly redemption trend
SELECT SUBSTR(transaction_date,1,7) AS month,
       ROUND(SUM(amount_inr),2) AS redemption_amount
FROM fact_transactions
WHERE transaction_type = 'Redemption'
GROUP BY month ORDER BY month;

-- Q8: Investors by KYC status
SELECT kyc_status, COUNT(DISTINCT investor_id) AS investor_count
FROM fact_transactions GROUP BY kyc_status;

-- Q9: Average expense ratio by category
SELECT category, ROUND(AVG(expense_ratio_pct),3) AS avg_expense
FROM dim_fund GROUP BY category ORDER BY avg_expense;

-- Q10: Anomalous schemes
SELECT scheme_name, return_1yr_pct, return_3yr_pct
FROM fact_performance WHERE anomaly_flag = 1;
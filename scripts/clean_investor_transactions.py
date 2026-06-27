import pandas as pd

df = pd.read_csv('data/raw/08_investor_transactions.csv')
print("BEFORE CLEANING:", df.shape)
print("Unique transaction_type:", df['transaction_type'].unique())
print("Unique kyc_status:", df['kyc_status'].unique())

# 1. Standardise transaction_type
type_map = {
    'sip': 'SIP', 'SIP': 'SIP',
    'lumpsum': 'Lumpsum', 'Lumpsum': 'Lumpsum', 'LUMPSUM': 'Lumpsum',
    'redemption': 'Redemption', 'Redemption': 'Redemption',
    'REDEMPTION': 'Redemption'
}
df['transaction_type'] = df['transaction_type'].str.strip().map(type_map)
print(f"Unmapped transaction types: {df['transaction_type'].isnull().sum()}")
df = df.dropna(subset=['transaction_type'])

# 2. Validate amount_inr > 0  ← correct column name
df = df[df['amount_inr'] > 0]

# 3. Fix date format
df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
df['transaction_date'] = df['transaction_date'].dt.strftime('%Y-%m-%d')

# 4. Standardise KYC status  ← your data has 'Verified' not 'VERIFIED'
df['kyc_status'] = df['kyc_status'].str.strip().str.title()
valid_kyc = ['Verified', 'Pending', 'Rejected']
invalid = df[~df['kyc_status'].isin(valid_kyc)]
print(f"Invalid KYC rows removed: {len(invalid)}")
df = df[df['kyc_status'].isin(valid_kyc)]

print("AFTER CLEANING:", df.shape)
df.to_csv('data/processed/investor_transactions_clean.csv', index=False)
print("✅ Saved → data/processed/investor_transactions_clean.csv")
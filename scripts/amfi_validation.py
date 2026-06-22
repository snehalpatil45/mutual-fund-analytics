import pandas as pd
import os

# Base path
base_path = os.path.join("data", "raw")

# Load datasets
fund_master = pd.read_csv(os.path.join(base_path, "01_fund_master.csv"))
nav_history = pd.read_csv(os.path.join(base_path, "02_nav_history.csv"))
scheme_performance = pd.read_csv(os.path.join(base_path, "07_scheme_performance.csv"))

# Extract unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])
performance_codes = set(scheme_performance["amfi_code"])

# Validation
missing_in_nav = fund_codes - nav_codes
missing_in_performance = fund_codes - performance_codes

print("=" * 50)
print("AMFI CODE VALIDATION REPORT")
print("=" * 50)

print(f"\nTotal Fund Master Codes: {len(fund_codes)}")
print(f"Total NAV Codes: {len(nav_codes)}")
print(f"Total Performance Codes: {len(performance_codes)}")

print("\nMissing Codes in NAV History:")
print(missing_in_nav)

print("\nMissing Codes in Scheme Performance:")
print(missing_in_performance)

if len(missing_in_nav) == 0:
    print("\n✓ All Fund Master AMFI codes exist in NAV History")

if len(missing_in_performance) == 0:
    print("✓ All Fund Master AMFI codes exist in Scheme Performance")
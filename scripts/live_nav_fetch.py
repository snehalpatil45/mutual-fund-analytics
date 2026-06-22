import requests
import pandas as pd
import os

# SBI Bluechip Fund AMFI Code
amfi_code = 119551

url = f"https://api.mfapi.in/mf/{amfi_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data['data'])

    # Create output folder if not exists
    os.makedirs("../data/raw", exist_ok=True)

    nav_df.to_csv("../data/raw/live_nav.csv", index=False)

    print("Live NAV data saved successfully!")
    print(nav_df.head())

else:
    print("Failed to fetch data")
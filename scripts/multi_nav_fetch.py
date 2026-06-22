import requests
import pandas as pd
import os

# AMFI Codes of selected schemes
scheme_codes = {
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

# Output folder
output_folder = "../data/raw/nav_files"
os.makedirs(output_folder, exist_ok=True)

for code, name in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data['data'])

            filename = f"{output_folder}/{name}.csv"

            nav_df.to_csv(filename, index=False)

            print(f"Saved: {name}.csv")

        else:
            print(f"Failed for {code}")

    except Exception as e:
        print(f"Error for {code}: {e}")

print("\nAll NAV files downloaded successfully!")
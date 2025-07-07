import pandas as pd
import json
import random
import string
import re
import argparse
import os

def generate_random_id():
    return ''.join(random.choices(string.digits, k=12))

# Argument parser
parser = argparse.ArgumentParser(description="Convert sensor data to NGSI-LD observations")
parser.add_argument("-f", "--file", required=True, help="Path to the CSV or Excel file")
args = parser.parse_args()
file_path = args.file

# Detect file extension and load accordingly
ext = os.path.splitext(file_path)[-1].lower()
if ext == '.csv':
    df = pd.read_csv(file_path)
elif ext in ['.xls', '.xlsx']:
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except ImportError:
        raise ImportError("You must install 'openpyxl' to read Excel files. Run: pip install openpyxl")
else:
    raise ValueError("Unsupported file format. Use .csv, .xls, or .xlsx")

# First column is always 'dateModified'
date_column = df.columns[0]
date_series = df[date_column].astype(str).replace(["nan", "NaT", "None"], "").str.strip()

# Loop through each observation column (excluding the first)
for col in df.columns[1:]:
    clean_col = col.strip().replace("_", " ")

    # Try to extract name and unit (if unit in parentheses or brackets)
    match = re.match(r'^(.*?)\s*[\[\(]\s*([^\[\]\(\)]+)\s*[\]\)]$', clean_col, re.IGNORECASE)
    if match:
        obs_name = match.group(1).strip()
        unit = match.group(2).strip()
    else:
        obs_name = clean_col
        unit = ""

    obs_id = f"urn:ngsi-ld:Observation:obs-{generate_random_id()}"
    observations = []

    for i, value in df[col].items():
        try:
            value = float(value)
        except:
            value = str(value) if pd.notnull(value) else ""

        if value == "":
            continue

        # Get the date, or fallback to generated timestamp
        date_modified = date_series[i]
        if not date_modified or date_modified.lower() in ["nan", "none"]:
            date_modified = ""  # fallback timestamp

        observation = {
            "@context": "https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/context.json",
            "id": obs_id,
            "type": "Observation",
            "name": {
                "type": "Property",
                "value": obs_name
            },
            "category": {
                "type": "Property",
                "value": ""
            },
            "dateModified": {
                "type": "Property",
                "value": date_modified
            },
            "measurement": {
                "type": "Property",
                "value": value,
                "measurementUnit": {
                    "type": "Property",
                    "value": unit
                }
            },
            "measurementType": {
                "type": "Property",
                "value": ""
            },
            "externalLink": {
                "type": "Property",
                "value": ""
            }
        }

        observations.append(observation)

    if not observations:
        print(f"⚠️  No valid observations found for column '{col}'")
        continue

    # Sanitize filename
    safe_obs_name = obs_name.lower().replace(" ", "_").replace("/", "_")
    output_file = f"observations_{safe_obs_name}.ngsild.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(observations, f, ensure_ascii=False, indent=2)

    print(f"✅ NGSI-LD observations written to '{output_file}'")

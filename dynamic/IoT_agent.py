"""
IoT_agent.py
------------
Convert sensor data from CSV or Excel into NGSI-LD Observation entities.

Usage:
    python IoT_agent.py -f "path/to/your/file.csv"

Expected column format:
    observation_name(unit),measurementType,category
    - Unit is optional and extracted from () or []
    - measurementType must be 'physical' or 'virtual' if present
    - category is optional
    - Columns with only observation_name are also accepted
"""

import pandas as pd
import json
import random
import string
import re
import argparse
import os
from datetime import datetime

def generate_random_id():
    return ''.join(random.choices(string.digits, k=12))

def extract_metadata(col_name_raw):
    parts = [p.strip() for p in col_name_raw.split(',')]
    name, unit, measurement_type, category = "", "", "", ""

    obs_part = parts[0]
    name_match = re.match(r'^(.*?)\s*[\(\[]\s*([^\)\]]+)\s*[\)\]]$', obs_part)
    if name_match:
        name = name_match.group(1).strip()
        unit = name_match.group(2).strip()
    else:
        name = obs_part.strip()

    if len(parts) == 2:
        p = parts[1].strip().lower()
        if p in ['virtual', 'physical']:
            measurement_type = p
        else:
            category = p
    elif len(parts) == 3:
        mtype = parts[1].strip().lower()
        if mtype in ['virtual', 'physical']:
            measurement_type = mtype
            category = parts[2].strip()
        else:
            category = parts[1].strip()
            measurement_type = parts[2].strip().lower()

    return name, unit, measurement_type, category

# Parse file argument
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
        raise ImportError("You must install 'openpyxl'. Run: pip install openpyxl")
else:
    raise ValueError("Unsupported file format. Use .csv, .xls, or .xlsx")

# Extract first column as dateModified
date_column = df.columns[0]
date_series = df[date_column].astype(str).replace(["nan", "NaT", "None"], "").str.strip()

# Process each observation column
for col in df.columns[1:]:
    name, unit, measurement_type, category = extract_metadata(col)
    obs_id = f"urn:ngsi-ld:Observation:obs-{generate_random_id()}"
    observations = []

    for i, value in df[col].items():
        try:
            value = float(value)
        except:
            value = str(value) if pd.notnull(value) else ""

        if str(value).strip().lower() in ["", "none", "nan"]:
            continue

        date_modified = date_series[i]
        if not date_modified or date_modified.lower() in ["nan", "none", ""]:
            date_modified = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        obs_entity = {
            "@context": "https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/context.json",
            "id": obs_id,
            "type": "Observation",
            "name": {
                "type": "Property",
                "value": name
            },
            "dateModified": {
                "type": "Property",
                "value": date_modified
            }
        }

        # Add measurement if value is valid
        if value not in ["", "nan", "NaN", None]:
            measurement_property = {
                "type": "Property",
                "value": value
            }
            if unit:
                measurement_property["measurementUnit"] = {
                    "type": "Property",
                    "value": unit
                }
            obs_entity["measurement"] = measurement_property

        # Optional fields
        if measurement_type:
            obs_entity["measurementType"] = {
                "type": "Property",
                "value": measurement_type
            }
        if category:
            obs_entity["category"] = {
                "type": "Property",
                "value": category
            }

        # Add externalLink only if non-empty (placeholder for now)
        external_link = ""
        if external_link:
            obs_entity["externalLink"] = {
                "type": "Property",
                "value": external_link
            }

        observations.append(obs_entity)

    if observations:
        safe_name = name.lower().replace(" ", "_").replace("/", "_")
        output_file = f"observations_{safe_name}.ngsild.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(observations, f, ensure_ascii=False, indent=2)
        print(f"✅ NGSI-LD observations written to '{output_file}'")
    else:
        print(f"⚠️  No valid data in column '{col}'")

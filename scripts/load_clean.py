import pandas as pd
import numpy as np
import re
from pathlib import Path

# File paths (input and output in the same folder)
RAW = Path(r"C:\Users\Admin\Downloads\project 2\agriculture_dashboard\data\ICRISAT-District Level Data - ICRISAT-District Level Data.csv")
OUT = RAW.parent / "ICRISAT-District Level Data_clean.csv"  # save cleaned file in same folder

# Function to clean column names
def clean_colname(c):
    c = c.strip()
    c = c.replace('(', '').replace(')', '')
    c = re.sub(r'[^0-9A-Za-z_]+', ' ', c)  # replace special chars with space
    c = '_'.join(c.split()).lower()        # convert to snake_case
    return c

# Load CSV
df = pd.read_csv(RAW, low_memory=False)

# Clean column names
df.columns = [clean_colname(c) for c in df.columns]

# Fix whitespace + proper case for names
if 'state_name' in df.columns:
    df['state_name'] = df['state_name'].astype(str).str.strip().str.title()

if 'dist_name' in df.columns:
    df['dist_name'] = df['dist_name'].astype(str).str.strip().str.title()

# Convert numeric columns (area, production, yield)
num_cols = [c for c in df.columns if re.search(r'(area|production|yield)', c)]
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# Recalculate rice yield (safety check)
if 'rice_area_1000_ha' in df.columns and 'rice_production_1000_tons' in df.columns:
    mask = (df['rice_area_1000_ha'] > 0) & df['rice_production_1000_tons'].notna()
    df.loc[mask, 'rice_yield_kg_per_ha_calc'] = (
        (df.loc[mask, 'rice_production_1000_tons'] * 1000) / df.loc[mask, 'rice_area_1000_ha']
    )

# Drop rows missing year or state
df = df.dropna(subset=['year', 'state_name'])

# Save cleaned CSV (same folder as RAW)
df.to_csv(OUT, index=False)

print("✅ Cleaned CSV saved to:", OUT)
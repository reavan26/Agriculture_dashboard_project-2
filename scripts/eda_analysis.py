# eda_plots.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === File Path ===
CSV_PATH = r"C:\Users\Admin\Downloads\project 2\agriculture_dashboard\data\ICRISAT-District Level Data_clean.csv"

# === Output folder for plots ===
PLOTS_DIR = r"C:\Users\Admin\Downloads\project 2\agriculture_dashboard\plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

# === Load Data ===
df = pd.read_csv(CSV_PATH)
print(f"📂 Loaded CSV with {df.shape[0]} rows and {df.shape[1]} columns")

# Convert numeric columns
num_cols = [c for c in df.columns if any(x in c for x in ['area','production','yield'])]
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')

sns.set(style="whitegrid")

# 1️⃣ Top 7 Rice Producing States (Bar Plot)
rice_state = df.groupby("state_name")["rice_production_1000_tons"].sum().sort_values(ascending=False).head(7)
plt.figure(figsize=(10,6))
sns.barplot(x=rice_state.values, y=rice_state.index, palette="Greens_r")
plt.title("Top 7 Rice Producing States")
plt.xlabel("Rice Production (1000 tons)")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "top7_rice_states.png"))
plt.close()

# 2️⃣ Top 5 Wheat Producing States (Bar + Pie)
wheat_state = df.groupby("state_name")["wheat_production_1000_tons"].sum().sort_values(ascending=False).head(5)
# Bar Plot
plt.figure(figsize=(8,5))
sns.barplot(x=wheat_state.index, y=wheat_state.values, palette="Blues_r")
plt.title("Top 5 Wheat Producing States")
plt.ylabel("Wheat Production (1000 tons)")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "top5_wheat_states_bar.png"))
plt.close()
# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(wheat_state.values, labels=wheat_state.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Blues", 5))
plt.title("Top 5 Wheat Producing States (%)")
plt.savefig(os.path.join(PLOTS_DIR, "top5_wheat_states_pie.png"))
plt.close()

# 3️⃣ Oilseed Production by Top 5 States
oilseed_state = df.groupby("state_name")["oilseeds_production_1000_tons"].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=oilseed_state.index, y=oilseed_state.values, palette="Oranges_r")
plt.title("Top 5 Oilseed Producing States")
plt.ylabel("Oilseed Production (1000 tons)")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "top5_oilseed_states.png"))
plt.close()

# 4️⃣ Sugarcane Production Trend
if 'year' in df.columns:
    sugar_trend = df.groupby('year')["sugarcane_production_1000_tons"].sum()
    plt.figure(figsize=(10,6))
    sns.lineplot(x=sugar_trend.index, y=sugar_trend.values, marker="o", color="brown")
    plt.title("India Sugarcane Production Trend (Last 50 Years)")
    plt.xlabel("Year")
    plt.ylabel("Production (1000 tons)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "sugarcane_trend.png"))
    plt.close()

# 5️⃣ Rice vs Wheat Production Comparison
rice_total = df.groupby('year')["rice_production_1000_tons"].sum()
wheat_total = df.groupby('year')["wheat_production_1000_tons"].sum()
plt.figure(figsize=(10,6))
sns.lineplot(x=rice_total.index, y=rice_total.values, marker="o", label="Rice")
sns.lineplot(x=wheat_total.index, y=wheat_total.values, marker="s", label="Wheat")
plt.title("Rice vs Wheat Production Over Years")
plt.xlabel("Year")
plt.ylabel("Production (1000 tons)")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "rice_vs_wheat.png"))
plt.close()

# 6️⃣ Correlation Heatmap (Area vs Production for Major Crops)
corr_cols = ['rice_area_1000_ha','rice_production_1000_tons',
             'wheat_area_1000_ha','wheat_production_1000_tons',
             'maize_area_1000_ha','maize_production_1000_tons']
plt.figure(figsize=(8,6))
sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation: Area vs Production (Rice, Wheat, Maize)")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "area_vs_production_corr.png"))
plt.close()

print(f"✅ All EDA plots saved in '{PLOTS_DIR}' folder")
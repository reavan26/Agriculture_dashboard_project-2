# Agriculture_dashboard_project-2

🌾 AgriData Explorer: Understanding Indian Agriculture with EDA
📌 Project Overview

AgriData Explorer is a data analytics and visualization project focused on analyzing Indian agricultural data at the state and district level.
The project leverages Python, SQL, and Power BI to clean raw agricultural data, perform Exploratory Data Analysis (EDA), and present insights through interactive dashboards.

The goal is to make complex agricultural data accessible, interpretable, and actionable for farmers, policymakers, and researchers.

🎯 Problem Statement

India’s agricultural data is large, complex, and often difficult to analyze due to:

Inconsistent formats

Missing values

Fragmented datasets

This makes it challenging for stakeholders to identify trends, productivity gaps, and regional disparities.

This project addresses these challenges by building a complete data pipeline that transforms raw agricultural data into meaningful insights.

🧠 Solution Approach
1️⃣ Data Collection

Dataset sourced from ICRISAT – District Level Agricultural Data

Covers crop area, production, and yield across Indian states and districts

2️⃣ Data Cleaning (Python)

Standardized column names (snake_case)

Removed special characters and extra spaces

Converted area, production, and yield fields to numeric

Handled missing values

Recalculated crop yield for validation

Generated a clean dataset for analysis

3️⃣ Exploratory Data Analysis (EDA)

Performed detailed EDA using Pandas, Matplotlib, and Seaborn, including:

Top rice and wheat producing states

Oilseed and sunflower production analysis

Sugarcane production trends over 50 years

Rice vs wheat production comparison

District-wise and state-wise analysis

Correlation between cultivated area and production

All plots are saved and reused for reporting and dashboards.

4️⃣ SQL Integration

Cleaned data stored in a structured SQL database

Used SQL queries to answer analytical questions such as:

Year-wise production trends

Districts with highest yields

Growth rate analysis for major crops

Area vs production relationships

5️⃣ Power BI Dashboard

Built interactive dashboards with:

Bar charts, line charts, pie charts, and heatmaps

Filters for crop type, state, district, and year

KPI cards for production, area, and yield

Enables drill-down analysis and decision-making

📊 Key Insights

Identified top-performing states for major crops

Observed long-term trends in sugarcane, rice, and wheat production

Strong correlation between cultivated area and production for major crops

Highlighted regional disparities in crop productivity

👥 Business Use Cases
🌱 Farmers

Analyze historical crop performance

Choose crops based on regional productivity

Improve yield through data-driven decisions

🏛 Policymakers

Identify low-productivity regions

Plan subsidies and resource allocation

Support crop insurance and risk management

🔬 Researchers

Study long-term agricultural trends

Analyze yield efficiency and crop behavior

Identify opportunities for innovation

🛠 Tech Stack

Python (Pandas, NumPy, Matplotlib, Seaborn)

SQL (Data storage and querying)

Power BI (Interactive dashboards)

Data Cleaning & EDA

Git & GitHub

📁 Project Structure
agriculture_dashboard/
│
├── data/
│   ├── raw_data.csv
│   └── ICRISAT-District Level Data_clean.csv
│
├── scripts/
│   ├── data_cleaning.py
│   └── eda_plots.py
│
├── plots/
│   └── saved_eda_visuals.png
│
├── power_bi/
│   └── agri_dashboard.pbix
│
└── README.md

📌 Dataset

Source: ICRISAT – District Level Agricultural Data

Covers:

Rice, Wheat, Oilseeds, Sugarcane, Cotton, Pulses, Millets, etc.

Area, Production, Yield

State & District level granularity

✅ Project Outcomes

Clean and structured agricultural dataset

Automated EDA with reusable visual outputs

SQL-based analytical querying

Interactive Power BI dashboards

End-to-end data analytics workflow

🚀 Future Enhancements

Integrate weather and climate data

Add machine learning models for yield prediction

Deploy dashboards online using Power BI Service

👨‍💻 Author
purusoth
Data Science Student

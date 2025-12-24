import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# 1. LOAD DATASETS
# ===============================
day = pd.read_csv("day_wise.csv")
country = pd.read_csv("country_wise_latest.csv")
clean = pd.read_csv("covid_19_clean_complete.csv")

print("Datasets loaded successfully")

# ===============================
# 2. DATAFRAME CONCEPTS
# ===============================
print("\nDataFrame Shape:", day.shape)
print("Columns:", day.columns)
print("\nMissing Values:\n", day.isnull().sum())

# ===============================
# 3. NUMPY CONCEPTS
# ===============================
confirmed_np = np.array(day['Confirmed'])
deaths_np = np.array(day['Deaths'])

print("\nNumPy Analysis")
print("Max Confirmed:", np.max(confirmed_np))
print("Mean Deaths:", np.mean(deaths_np))
print("Standard Deviation:", np.std(confirmed_np))

# ===============================
# 4. GROUPBY OPERATION
# ===============================
country_group = clean.groupby('Country/Region')[['Confirmed','Deaths','Recovered']].max()
top10_confirmed = country_group.sort_values(by='Confirmed', ascending=False).head(10)

# ===============================
# ----------- PLOTS ------------
# ===============================

# PLOT 1: Pie Chart – Global Distribution
latest = day.iloc[-1]
plt.figure()
plt.pie(
    [latest['Confirmed'], latest['Deaths'], latest['Recovered']],
    labels=['Confirmed','Deaths','Recovered'],
    autopct='%1.2f%%',shadow=True,
    startangle=140
)
plt.title("Global COVID-19 Case Distribution")
plt.show()

# PLOT 2: Bar – Top 10 Countries (Confirmed)
plt.figure()
plt.barh(top10_confirmed.index, top10_confirmed['Confirmed'], color='green')
plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Cases")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# PLOT 3: Bar – Top 10 Countries (Deaths)
plt.figure()
plt.barh(top10_confirmed.index, top10_confirmed['Deaths'], color='green')
plt.title("Top 10 Countries by Deaths")
plt.xlabel("Deaths")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# PLOT 4: Bar – Top 10 Countries (Recovered)
plt.figure()
plt.barh(top10_confirmed.index, top10_confirmed['Recovered'] , color='green')
plt.title("Top 10 Countries by Recovered Cases")
plt.xlabel("Recovered")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# PLOT 5: Histogram – Daily Confirmed Cases
plt.figure()
plt.hist(day['New cases'], bins=30 , color='skyblue', edgecolor='black')
plt.title("Histogram of Daily New Cases")
plt.xlabel("New Cases")
plt.ylabel("Frequency")
plt.show()

# PLOT 6: Histogram – Daily Deaths
plt.figure()
plt.hist(day['New deaths'], bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of Daily Deaths")
plt.xlabel("Deaths")
plt.ylabel("Frequency")
plt.show()

# PLOT 7: Scatter – Confirmed vs Deaths
plt.figure(figsize=(7,5))
plt.scatter(day['Confirmed'], day['Deaths'], alpha=0.6,color='purple')
plt.title("Confirmed vs Deaths")
plt.xlabel("Confirmed")
plt.ylabel("Deaths")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# PLOT 8: Box Plot – Confirmed Cases
min_val = np.min(day['Confirmed'])
max_val = np.max(day['Confirmed'])
mean_val = np.mean(day['Confirmed'])
median_val = np.median(day['Confirmed'])

stats = ['Min', 'Mean', 'Median', 'Max']
values = [min_val, mean_val, median_val, max_val]

plt.figure(figsize=(7,5))
plt.bar(stats, values, color=['skyblue', 'orange', 'green', 'red'])

plt.title("Statistical Summary of Confirmed COVID-19 Cases")
plt.xlabel("Statistic Type")
plt.ylabel("Number of Cases")

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# PLOT 9: Bar – Death Rate (Top 10)
country['Death_Rate'] = (country['Deaths'] / country['Confirmed']) * 100
top_death_rate = country.sort_values(by='Death_Rate', ascending=False).head(10)

plt.figure()
plt.bar(top_death_rate['Country/Region'], top_death_rate['Death_Rate'])
plt.title("Top 10 Countries by Death Rate")
plt.xticks(rotation=45)
plt.ylabel("Death Rate (%)")
plt.show()

# PLOT 10: Bar – Active Cases Comparison
top_active = country.sort_values(by='Active', ascending=False).head(10)

plt.figure()
plt.bar(top_active['Country/Region'], top_active['Active'])
plt.title("Top 10 Countries by Active Cases")
plt.xticks(rotation=45)
plt.ylabel("Active Cases")
plt.show()

print("\nAdvanced COVID-19 Analysis Completed Successfully")

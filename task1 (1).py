import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/Prodigy-InfoTech/data-science-datasets/main/Task%201/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
data = pd.read_csv(url, skiprows=4)

print(data.head())
# Bar chart: Top 10 countries by population
year = "2024"
top_countries = data[["Country Name", year]].dropna().nlargest(10, year)

sns.barplot(x=year, y="Country Name", data=top_countries)
plt.title(f"Top 10 Countries by Population in {year}")
plt.show()

# Histogram: Distribution of population across countries
sns.histplot(data[year].dropna(), bins=20, kde=True)
plt.title(f"Distribution of Population Across Countries ({year})")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.show()


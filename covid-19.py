import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=r"D:\workspace\python\Data Manipulation\Covid-19 Data Analysis\worldometer_data.csv"

covid_df=pd.read_csv(data,usecols=["Country/Region","Population","TotalCases","TotalDeaths","TotalRecovered","WHO Region"])

# Calculate total cases, deaths, and recoveries per country
df_country = covid_df.groupby(['Country/Region'])[['TotalCases', 'TotalDeaths', 'TotalRecovered']].max()

# Calculate growth rate (percentage change)
df_country['GrowthRate'] = df_country['TotalCases'].pct_change() * 100

# Aggregating by country and date
df_grouped = covid_df.groupby(['Country/Region']).agg({'TotalCases': 'sum', 'TotalDeaths': 'sum', 'TotalRecovered': 'sum'}).reset_index()

# Aggregating total cases per country
total_cases_country = df_grouped.groupby('Country/Region')[['TotalCases']].max()

# Set plot style
sns.set(style="whitegrid")

# Plotting cumulative cases for each country (without date)
plt.figure(figsize=(14, 7))
sns.barplot(x=covid_df['Country/Region'], y=covid_df['TotalCases'])
plt.title("Total Cumulative Cases by Country")
plt.xlabel('Country/Region')
plt.ylabel('Total Cases')
plt.xticks(rotation=90)
plt.show()


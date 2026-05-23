# The purpose of this project is to see the trend of Alzheimer's Deaths in NJ to see if it increased or not

# Extract: Read data from data.gov 
import pandas as pd
data = pd.read_csv("Leading_Causes_of_Death_US.csv")

# Transformation: Change information so that there are yearly averages for Alzheimer's disease deaths
alzheimers_disease_averages = {}  # Keys: Years, Values: [Total Deaths, Count of Rows]

for index, each_row in data.iterrows():
    # Filter rows where Alzheimer's disease is the cause in NJ 
    if each_row['Cause Name'] == "Alzheimer's disease" and each_row['State'] == "New Jersey":
        year = int(each_row['Year'])  
        deaths = each_row['Deaths']  
        if year not in alzheimers_disease_averages:
            alzheimers_disease_averages[year] = [deaths, 1]  
        else:
            alzheimers_disease_averages[year][0] += deaths
            alzheimers_disease_averages[year][1] += 1

for year, values in alzheimers_disease_averages.items():
    alzheimers_disease_averages[year] = values[0] / values[1]

alzheimers_disease_averages = dict(sorted(alzheimers_disease_averages.items()))

# Loading: Create a trend graph showing the yearly average deaths due to Alzheimer's Disease in NJ
import matplotlib.pyplot as plt
plt.plot(alzheimers_disease_averages.keys(), alzheimers_disease_averages.values())
plt.title("Yearly Average Deaths Due to Alzheimer's Disease in NJ")
plt.xlabel("Years")
plt.ylabel("Average Deaths")
plt.savefig("AlzheimersinNJ.jpg")
plt.show()

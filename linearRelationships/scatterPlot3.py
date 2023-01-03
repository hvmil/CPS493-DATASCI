import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x ="Number of Residents Staying in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time"

y = "Residents Weekly COVID-19 Deaths"

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/main_datasets/MAIN_DATASET/MAIN_20_21_22_Totals_byWeek_QA_checked.csv"

df = pd.read_csv(inputCSV_FilePath)
df = df.sample(frac=.2)

plt.title("Weeks 2020-05-24 through 2022-10-23 ")
plt.xlabel(x)
plt.ylabel(y)
plt.scatter(df[x],df[y],color = 'red', marker='+')
# plt.ylim([0,2.5e3])
# plt.xlim([9e5,1.075e6])



plt.show()


#1. NaNrowRemoval
#2. MapAVG.py
#3. numberOfRows.py
#4. averageOfRange.py

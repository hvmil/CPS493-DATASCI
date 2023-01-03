import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/Covid-19 Nursing Home Data/Cleaned1_2022.csv")
df = df.sample(frac=.1)
x = "Total Resident Confirmed COVID-19 Cases Per 1,000 Residents"
y = "Total Resident COVID-19 Deaths Per 1,000 Residents"

plt.xlabel(x)
plt.ylabel(y)
plt.scatter(df[x],df[y],color = 'red', marker='+')
plt.ylim([0,1000])
plt.xlim([0,1000])

plt.show()


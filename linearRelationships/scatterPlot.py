import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/Covid-19 Nursing Home Data/msc/Cleaned_PawlingNY_Dates.csv")
# df = df.sample(frac=1)
y = "Residents Weekly COVID-19 Deaths"
x = "Week Ending"

plt.xlabel(x)
plt.ylabel(y)
plt.scatter(df[x],df[y],color = 'red', marker='+')
plt.ylim([0,20])
plt.xlim([0,127])

plt.show()
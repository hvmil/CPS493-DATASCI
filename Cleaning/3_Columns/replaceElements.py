#replacing date column to a numeric numeric value
import pandas as pd

#dataframe:
df = pd.read_csv("datasets/Covid-19 Nursing Home Data/msc/Cleaned_PawlingNY.csv")

i = 1


for index, row in df.iterrows():
    df.at[index,"Week Ending"] = i
    i += 1
    






df.to_csv("Cleaned_PawlingNY_dates.csv", encoding='utf-8', index=False)

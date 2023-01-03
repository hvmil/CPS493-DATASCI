import pandas as pd
import numpy as np
#import column names:
import sys
sys.path.append("/Users/Hamil/Documents/GitHub/CPS-493/datasets/Covid-19 Nursing Home Data")
from main_datasets.columnsOfInterest import columns

df1 = pd.read_csv("datasets/Covid-19 Nursing Home Data/main_datasets/faclevel_2020.csv")
df2 = pd.read_csv("datasets/Covid-19 Nursing Home Data/main_datasets/faclevel_2021.csv")
df3 = pd.read_csv("datasets/Covid-19 Nursing Home Data/main_datasets/faclevel_2022.csv")

#merge dataframes
df = pd.concat([df1, df2, df3], ignore_index=True, sort=False)
#dataframe with the wanted columns:
df = pd.DataFrame(df[columns])
#replace null values with NaN:
df = df.replace(r'^\s*$', np.nan, regex=True)

df = df.fillna(0)

########### sort by "Week Ending" #############

df["Week Ending"] = pd.to_datetime(df["Week Ending"])

df = df.sort_values(by='Week Ending')

df.to_csv("MAIN_20_21_22.csv", encoding='utf-8', index=False)
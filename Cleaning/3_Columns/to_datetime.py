import pandas as pd
import numpy as np
#import column names:
import sys
sys.path.append("/Users/Hamil/Documents/GitHub/CPS-493/datasets/Covid-19 Nursing Home Data")
from main_datasets.columnsOfInterest import columns

df = pd.read_csv("datasets/Covid-19 Nursing Home Data/main_datasets/faclevel_2022.csv")

#replace null values with NaN:
df = df.replace(r'^\s*$', np.nan, regex=True)


########### sort by "Week Ending" #############

df["Week Ending"] = pd.to_datetime(df["Week Ending"])

df = df.sort_values(by='Week Ending')

df.to_csv("faclevel_2022_date_cleaned.csv", encoding='utf-8', index=False)
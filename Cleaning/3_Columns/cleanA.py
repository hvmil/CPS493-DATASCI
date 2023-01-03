#csv to dataframe -> replace null valies with NaN -> Remove uwanted columns -> Dataframe to CSV
#remove unwanted columns
import pandas as pd
import numpy as np

#import column names:
import sys
sys.path.append("/Users/Hamil/Documents/GitHub/CPS-493/datasets/Covid-19 Nursing Home Data")
from main_datasets.columnsOfInterest import columns

#create dataframe:
df = pd.read_csv("datasets/Covid-19 Nursing Home Data/msc/PawlingNY.csv")
#replace null values with NaN:
df = df.replace(r'^\s*$', np.nan, regex=True)
#dataframe with the wanted columns:
df = pd.DataFrame(df[columns])

df.to_csv("Cleaned_PawlingNY.csv", encoding='utf-8', index=False)

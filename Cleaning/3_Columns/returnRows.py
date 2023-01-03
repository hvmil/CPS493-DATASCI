#return rows of the last reported week per nursing home
import pandas as pd

#dataframe:
df = pd.read_csv("Cleaning/Cleaned1_2022.csv")

#dataframe column:
providerNum = df["Federal Provider Number"]

#dataframe column:
# dates = df["Federal Provider Number"]

#number of rows in the dataframe
length = len(providerNum.index)

#list to store indicies from providerNum:
indicies = []

#first element
curr = providerNum.loc[0]

#index of an the element
i = 0


for x in providerNum:
    if i == length - 1:
        indicies.append(i)
    elif x == curr:
        i += 1
    else:
        indicies.append(i - 1)
        curr = x
        i+= 1


df = df.iloc[indicies]

df.to_csv("Cleaned2_2022.csv", encoding='utf-8', index=False)

import pandas as pd
import numpy as np

x = pd.DataFrame(
    {
        "Week Ending": ["10/23/22", "05/07/19","08/01/20"],
        "test": [1,2,3]
    }
)

y = pd.DataFrame(
    {
        "Week Ending": ["11/21/22", "07/05/19","08/02/20"],
        "test": [4,5,6]

    }
)

df = pd.concat([x, y], ignore_index=True, sort=False)

print(df)

print(type(df.at[0,"Week Ending"]))

df["Week Ending"] = pd.to_datetime(df["Week Ending"])

print(df)

df = df.sort_values(by='Week Ending')

print(df)

df= df.drop(df[df['test'] == 2].index, inplace=False)

print(df)
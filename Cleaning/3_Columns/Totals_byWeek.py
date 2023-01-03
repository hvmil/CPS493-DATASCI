import pandas as pd
#import column names:
import sys
sys.path.append("/Users/Hamil/Documents/GitHub/CPS-493/datasets/Covid-19 Nursing Home Data/main_datasets")
from columnsOfInterest import columns


inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/main_datasets/MAIN_DATASET/MAIN_20_21_22_QA_checked.csv"
outPutCSVname = "MAIN_20_21_22_Totals_byWeek_QA_checked.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname
column0 = "Week Ending"

df = pd.read_csv(inputCSV_FilePath)
df = df[columns]
lengthStart = len(df)

####Get the keys #####
grouped = df['Week Ending']

grouped = grouped.drop_duplicates()

weeks = list(grouped)
#######################

#### Sum the columns by week ####
dict = {}

for x in weeks:
    dict[x] = [x]
    string = '`Week Ending` == @x'
    for y in columns:
        if y == column0: ##skip the key
            continue
        sum = df.query(string)[y].sum()
        dict[x].append(sum) 
#######################

#### Dictionary to Dataframe ####
df = pd.DataFrame(dict.values(), columns = columns)
df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)
#######################

#### output ####
lengthEnd = len(df)
rowsRemoved = lengthStart - lengthEnd


print("------------------------")
print("# of rows of input: " + str(lengthStart))
print("# of rows of output: " + str(lengthEnd))
print("difference: " + str(rowsRemoved))
print("------------------------")
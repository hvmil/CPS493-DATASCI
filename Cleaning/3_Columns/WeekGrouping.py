import pandas as pd
import numpy as np

column0 = "Week Ending"
column1 = "Residents Weekly Confirmed COVID-19"
column2 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines"
column3 = "Average Cases of COVID-19"
column4 = "Total Entries"
column5 = "Week Number"

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/WeeklyCases_&_PercentVacc/Vaccine&Cases&Week_NaN_rowsRemoved.csv"

outPutCSVname = "Vaccine&Cases&Week_byWeek.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname

dict = {}

df = pd.read_csv(inputCSV_FilePath)

lengthStart = len(df)

def total(newValue, oldValue):
    return round((newValue + oldValue), 1)

def average(newValue, oldValue):
    return round((newValue + oldValue)/2, 1)

value5 = 0
for index, row in df.iterrows():
    key = df.at[index, column0]
    value1 = df.at[index, column1]
    value2 = df.at[index, column2]
    value3 =  df.at[index, column1]
    
    if key not in dict:
        dict[key] = [key,value1,value2,value3,1,value5]
        value5 += 1
    else:
        values = dict[key]
        oldValue1 = values[1]
        oldValue2 = values[2]
        oldValue3 = values[3]
        oldValue4 = values[4]

        newValue1 = total(value1, oldValue1)
        newValue2 = average(value2, oldValue2)
        newValue3 = round(newValue1/ (oldValue4 + 1))
        newValue4 = oldValue4 + 1

        dict[key] = [key, newValue1, newValue2, newValue3, newValue4, value5]


data = list(dict.values())
df = pd.DataFrame(data, columns=[column0,column1,column2,column3,column4,column5])
df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)
lengthEnd = len(df)
rowsRemoved = lengthStart - lengthEnd


print("------------------------")
print("# of rows of input: " + str(lengthStart))
print("# of rows of output: " + str(lengthEnd))
print("difference: " + str(rowsRemoved))
print("------------------------")
import pandas as pd

column0 = "Week Ending"

column1 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines" #key
column2 = "Residents Weekly Confirmed COVID-19" #average

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/WeeklyCases_&_PercentVacc/Vaccine&Cases_NaN_rowsRemoved.csv"

outPutCSVname = "Vaccine_vs_CasesAVG_RangedAverage_n=83.2.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname
dict = {}

df = pd.read_csv(inputCSV_FilePath)

lengthStart = len(df)

for index, row in df.iterrows():
    key = round(df.at[index, column1],1)
    average = df.at[index, column2]
    if key not in dict:
        dict[key] = average
    else:
        average = (dict[key] + average)/2
        dict[key] = round(average)

df = pd.DataFrame(dict.items(), columns=[column0,column1,column2])
lengthEnd = len(df)
rowsRemoved = lengthStart - lengthEnd

df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)


print("------------------------")
print("# of rows of input: " + str(lengthStart))
print("# of rows of output: " + str(lengthEnd))
print("difference: " + str(rowsRemoved))
print("------------------------")
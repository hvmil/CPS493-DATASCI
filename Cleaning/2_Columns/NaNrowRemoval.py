#Remove rows with NaN values
import pandas as pd

column1 = "Residents Weekly Confirmed COVID-19"
column2 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines"

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/WeeklyCases_&_PercentVacc/Vaccine&Cases_unprocessed.csv"

outPutCSVname = "Vaccine&Cases_NaN_rowsRemoved.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname



df = pd.read_csv(inputCSV_FilePath)

lengthStart = len(df)

df = df[df[column1].notnull()]
df = df[df[column2].notnull()]


lengthEnd = len(df)

rowsRemoved = lengthStart - lengthEnd

print("------------------------")
print("# of rows of input: " + str(lengthStart))
print("# of rows of output: " + str(lengthEnd))
print("# of rows of removed: " + str(rowsRemoved))
print("------------------------")


df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)

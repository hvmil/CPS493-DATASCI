#Remove rows with NaN values
import pandas as pd

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/main_datasets/faclevel_20_21_22_cleaned.csv"

outPutCSVname = "faclevel_20_21_22_cleaned_nan=0.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname



df = pd.read_csv(inputCSV_FilePath)

lengthStart = len(df)

df = df.fillna(0)

lengthEnd = len(df)

rowsRemoved = lengthStart - lengthEnd

print("------------------------")
print("# of rows of input: " + str(lengthStart))
print("# of rows of output: " + str(lengthEnd))
print("# of rows of removed: " + str(rowsRemoved))
print("------------------------")


df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)
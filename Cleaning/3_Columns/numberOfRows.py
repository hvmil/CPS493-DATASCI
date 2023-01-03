import pandas as pd

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/WeeklyCases_&_PercentVacc/Vaccine_vs_CasesAVG/Vaccine_vs_CasesAVG_RangedAverage_n=1.csv"




df = pd.read_csv(inputCSV_FilePath)

lengthStart = len(df)

print("------------------------")
print("# of rows of input: " + str(lengthStart))

print("------------------------")
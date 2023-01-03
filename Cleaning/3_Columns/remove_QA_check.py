import pandas as pd
#import column names:
import sys
sys.path.append("/Users/Hamil/Documents/GitHub/CPS-493/datasets/Covid-19 Nursing Home Data/main_datasets")
from columnsOfInterest import columns


inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/main_datasets/MAIN_DATASET/MAIN_20_21_22.csv"
outPutCSVname = "MAIN_20_21_22_Totals_byWeek_nan=0_QA_checked.csv"
outputCSV_FilePath = "outputs/" + outPutCSVname
column0 = "Week Ending"

df = pd.read_csv(inputCSV_FilePath)
lengthStart = len(df)

df = df[df["Passed Quality Assurance Check"] == 'Y']

df = df[columns]
#######################

#### output ####
lengthEnd = len(df)
rowsRemoved = lengthStart - lengthEnd


print("------------------------")
print("# of rows of input: " + str(lengthStart))
print("# of rows of output: " + str(lengthEnd))
print("difference: " + str(rowsRemoved))
print("------------------------")

df.to_csv(outputCSV_FilePath, encoding='utf-8', index=False)
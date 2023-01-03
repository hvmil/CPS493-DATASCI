import pandas as pd

column1 = "Residents Weekly Confirmed COVID-19"
column2 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines"

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/WeeklyCases_&_PercentVacc/Vaccine_vs_CasesAVG/Vaccine_vs_CasesAVG_RangedAverage_n=1.2.csv"

outPutCSVname = "Vaccine_vs_CasesAVG_RangedAverage_n=2.2.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname


df = pd.read_csv(inputCSV_FilePath)
n = 2 #range

col_list1 = df[column1]
col_list2 = df[column2]

col_list1 = [sum(col_list1[i:i+n])//n for i in range(0,len(col_list1),n)]
col_list2 = [sum(col_list2[i:i+n])//n for i in range(0,len(col_list2),n)]

data = {
    column1: col_list1,
    column2: col_list2
}
df = pd.DataFrame(data)

df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)
        


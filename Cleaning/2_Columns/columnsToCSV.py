import pandas as pd
import numpy as np

column1 = "Residents Weekly Confirmed COVID-19"
column2 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines"
inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/Main.csv"
outPutCSVname = "DeathsXCases.csv"


df = pd.read_csv(inputCSV_FilePath)

df = df[[column1,column2]]

outoutCSV_FilePath = "outputs/" + outPutCSVname

df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)



import pandas as pd
import numpy as np

column0 = "Week Ending"
column1 = "Residents Weekly Confirmed COVID-19"
column2 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines"
inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/faclevel_20_21_22_cleaned.csv"
outPutCSVname = "Vaccine&Cases&Week_unprocessed.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname


df = pd.read_csv(inputCSV_FilePath)

df = df[[column0,column1,column2]]


df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)



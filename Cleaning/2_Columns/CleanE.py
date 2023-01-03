import pandas as pd
import numpy as np

column1 = "Residents Weekly Confirmed COVID-19"
column2 = "Percentage of Current Residents Up to Date with COVID-19 Vaccines"

inputCSV_FilePath = "datasets/Covid-19 Nursing Home Data/WeeklyConfirmed_VS_PercentVacc/Vaccine&Cases_unprocessed.csv"

outPutCSVname = "Vaccine&Cases_SkipNaN.csv"
outoutCSV_FilePath = "outputs/" + outPutCSVname
# Dict = {100:[],200:[],300:[],400:[],500:[],600:[],700:[],800:[], 900:[], 1000:[]}
dict = {}

df = pd.read_csv(inputCSV_FilePath)


for index, row in df.iterrows():
    cases = df.at[index, column1]
    percent = df.at[index, column2]
    total = 0
    if pd.isna(percent) or pd.isna(cases): #if NaN
        continue #skip
    if cases not in dict:
        dict[cases] = percent
    else:
        dict[cases] = total
        total = (total + percent)/2
        dict[cases] = round(total,1)

df = pd.DataFrame(dict.items(), columns=[column1,column2])

df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)



#what to do with nan? create two graphs when nan = 0 and when nan is skipped
# {45.0: 4.0, 
# 10.0: 37.0, 
# 13.0: 15.6, 
# 0.0: 40.4, 
# 9.0: nan, if np.nan, then percent = 0
# 1.0: nan, 
# 38.0: 9.1, 
# 18.0: 35.5, 2.0: 6.8, 80.0: 41.2, 25.0: 0.3, 103.0: nan, 5.0: 24.6, 54.0: 0.0, 7.0: 1.8, 34.0: 0.0, 52.0: 0.0, 3.0: 49.6, 4.0: nan, 36.0: 0.1, 21.0: 3.4, 6.0: 46.4, 29.0: 0.5, 63.0: nan, 24.0: 33.7, 114.0: nan, 23.0: 47.7, 12.0: 36.3, 41.0: 32.0, 108.0: nan, 44.0: nan, 144.0: nan, 26.0: nan, 40.0: 4.9, 33.0: 35.5, 82.0: 0.0, 94.0: nan, 14.0: 39.0, 15.0: 32.4, 8.0: 3.8, 31.0: nan, 28.0: 8.6, 65.0: 0.0, 37.0: 21.9, 35.0: nan, 51.0: 1.3, 27.0: 6.6, 78.0: 0.0, 30.0: 1.0, 83.0: nan, 68.0: 41.5, 60.0: 0.0, 66.0: 0.0, 91.0: nan, 76.0: nan, 42.0: 44.1, 88.0: nan, 22.0: 18.7, 32.0: 30.2, 48.0: 34.8, 69.0: nan, 138.0: nan, 17.0: 23.4, 57.0: 0.0, 89.0: nan, 43.0: 5.6, 19.0: 43.2, 85.0: nan, 90.0: nan, 11.0: 37.2, 110.0: nan, 118.0: nan, 61.0: 0.0, 81.0: nan, 47.0: 26.2, 20.0: 5.2, 95.0: nan, 73.0: nan, 50.0: 0.0, 142.0: nan, 77.0: nan, 128.0: nan, 16.0: 14.2, 56.0: 0.0, 119.0: nan, 112.0: nan, 39.0: 33.5, 166.0: nan, 155.0: nan, 55.0: 0.9, 67.0: 0.0, 46.0: 1.4, 53.0: 35.9, 71.0: nan, 72.0: 0.0, 70.0: 16.9, 130.0: nan, 96.0: nan, 62.0: 0.0, 74.0: nan, 59.0: nan, 107.0: nan, 58.0: 0.0, 84.0: 41.2, 92.0: nan, 133.0: nan, 87.0: nan, 64.0: 32.4, 121.0: nan, 49.0: 1.5, 100.0: nan, 75.0: nan, 147.0: nan, 137.0: nan, 104.0: nan, 93.0: 0.0, 162.0: nan, 79.0: 0.0, 222.0: nan, 152.0: nan, 102.0: nan, 109.0: nan, 120.0: nan, 134.0: nan, 105.0: nan, 126.0: nan, 113.0: nan, 178.0: nan, 129.0: nan, 168.0: nan, 312.0: nan, 172.0: nan, 125.0: nan, 86.0: 41.2, 146.0: nan, 122.0: nan, 127.0: nan, 101.0: nan, 99.0: nan, 173.0: nan, 115.0: nan, 156.0: nan, 97.0: nan, 111.0: nan, 135.0: nan, 98.0: nan, 149.0: nan, 164.0: nan, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: nan, nan: 0.0, nan: 0.0, nan: 0.0, nan: 0.0, nan: nan, nan: 0.0, nan: nan, nan: 0.0, nan: nan, nan: 0.0}


# def addtoDict(dict, x):
#     list = dict[x]
#     list.append(deaths)
#     dict[x] = list
#     return dict

# #if cases > n, dict[n] = deaths
# for index, row in df.iterrows():
#     cases = df.at[index,column1]
#     vacPercent = df.at[index,column2]
#     if cases < 100:
#         Dict = addtoDict(Dict, 100)

#     elif cases >= 100 and cases < 200:
#         Dict = addtoDict(Dict, 200)

#     elif cases >= 200 and cases < 300:
#         Dict = addtoDict(Dict, 300)

#     elif cases >= 300 and cases < 400:
#         Dict = addtoDict(Dict, 400)

#     elif cases >= 400 and cases < 500:
#         Dict = addtoDict(Dict, 500)

#     elif cases >= 500 and cases < 600:
#         Dict = addtoDict(Dict, 600)

#     elif cases >= 600 and cases < 700:
#         Dict = addtoDict(Dict, 700)

#     elif cases >= 700 and cases < 800:
#         Dict = addtoDict(Dict, 800)

#     elif cases >= 800 and cases < 900:
#         Dict = addtoDict(Dict, 900)

#     elif cases >= 900 and cases < 1000:
#         Dict = addtoDict(Dict, 1000)
    
#     elif cases >= 1000:
#         Dict = addtoDict(Dict, 500)


# for x in Dict:
#     list = Dict[x]
#     length = len(list)
#     j = 0

#     for y in list:
#         j += y
    
#     j = j/length

#     Dict[x] = j



#df.to_csv(outoutCSV_FilePath, encoding='utf-8', index=False)


#{100: 61.12526785714285, 
# 200: 23.803715846994535, 
# 300: 48.6010763888889, 
# 400: 46.49059782608695, 
# 500: 173.2022090445572, 
# 600: 70.56392561983469, 
# 700: 81.5193271461717, 
# 800: 94.33996966632954, 
# 900: 104.44855785837647, 
# 1000: 110.04844120328167}

    
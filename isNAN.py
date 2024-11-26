import pandas as pd

df = pd.read_csv("FinalDatasets/BARLEY_data_merged.csv")

isNAN =  df['YIELD'].isna()
print(isNAN)
isNAN.to_csv("FinalDatasets/isNAN.csv")
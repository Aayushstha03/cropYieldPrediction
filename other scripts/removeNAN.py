import pandas as pd

df = pd.read_csv("FinalDatasets/cropComplete.csv")
# go thourhg all entries in the YIELD column
for i in range(len(df['YIELD'])):
    # check if the entry is a NaN value
    if pd.isna(df['YIELD'][i]):
        # if it is, replace the contents with 0
        df.loc[i, 'YIELD'] = 0
    
# save the modified dataframe to a new csv file
df.to_csv("FinalDatasets/noNAN.csv", index=False)

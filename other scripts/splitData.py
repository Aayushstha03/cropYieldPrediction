import pandas as pd

data = pd.read_csv("FinalDatasets/structured_crop_yield.csv")

crop_types = data['Crop_Type'].unique()

for crop in crop_types:
    crop_data = data[data['Crop_Type'] == crop]

    filename = f"FinalDatasets/{crop}_data.csv"
    crop_data.to_csv(filename, index=False)



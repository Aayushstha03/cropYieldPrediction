import pandas as pd
import os  # Import os to handle file removal

# Load datasets
data = pd.read_csv("FinalDatasets/cropComplete.csv")
weather_data = pd.read_csv("FinalDatasets/WEATHER_data.csv")

# Split the crop dataset by crop type and save each to a separate file
crop_types = data['CROP_TYPE'].unique()

for crop in crop_types:
    crop_data = data[data['CROP_TYPE'] == crop]
    filename = f"FinalDatasets/{crop}_data.csv"
    crop_data.to_csv(filename, index=False)

# List of crop data files
crop_files = [f"FinalDatasets/{crop}_data.csv" for crop in crop_types]
join_columns = ['YEAR', 'DISTRICT_NAME']

# Merge each crop dataset with the weather dataset and remove the original crop data files
for crop_file in crop_files:
    crop_data = pd.read_csv(crop_file)
    # Perform an inner join with the weather dataset
    merged_data = crop_data.merge(weather_data, on=join_columns, how='inner')
    # Save the merged dataset to a new file
    output_file = crop_file.replace('.csv', '_merged.csv')
    merged_data.to_csv(output_file, index=False)
    print(f"Merged dataset saved for {crop_file} to {output_file}")
    
    # Remove the original crop data file
    os.remove(crop_file)
    print(f"Removed temporary file: {crop_file}")

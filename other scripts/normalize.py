# import pandas as pd

# file_paths = [
#     "FinalDatasets/BARLEY_data_merged.csv",
#     "FinalDatasets/MAIZE_data_merged.csv",
#     "FinalDatasets/MILLET_data_merged.csv",
#     "FinalDatasets/PADDY_data_merged.csv",
#     "FinalDatasets/WHEAT_data_merged.csv",
# ]

# for file_path in file_paths:
#     # Read the CSV file
#     df = pd.read_csv(file_path)
    
#     # Drop rows where PRODUCTION or AREA is 0
#     df = df[(df['PRODUCTION'] != 0) & (df['AREA'] != 0)]
    
#     # Create a new column YIELD by dividing PRODUCTION by AREA
#     df['YIELD'] = df['PRODUCTION'] / df['AREA']
    
#     # Multiply YIELD by 1000 and truncate to 2 decimal places
#     df['YIELD'] = (df['YIELD'] * 1000).round(2)
    
#     # Drop the columns AREA and PRODUCTION
#     df = df.drop(columns=['AREA', 'PRODUCTION'])
    
#     # Save the modified DataFrame back to the CSV file
#     df.to_csv(file_path, index=False)
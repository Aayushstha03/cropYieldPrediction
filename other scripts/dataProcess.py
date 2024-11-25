import pandas as pd

df = pd.read_csv("data/crop_yield.csv")
# Assume df is your existing dataframe
# Extract the district names
districts = df['DISTRICT_NAME']

# Reshape the data
reshaped_data = []
for col in df.columns[1:]:  # Skip DISTRICT_NAME
    crop, stat, year = col.split('_')
    year = f"{year[:4]}-{year[4:]}"  # Adjust year formatting if needed
    for district, value in zip(districts, df[col]):
        reshaped_data.append([district, year, crop, stat, value])

# Create a new DataFrame
reshaped_df = pd.DataFrame(reshaped_data, columns=['DISTRICT_NAME', 'Year', 'Crop_Type', 'Statistic', 'Value'])

# Pivot table to align Area, Production, and Yield into columns
final_df = reshaped_df.pivot_table(
    index=['DISTRICT_NAME', 'Year', 'Crop_Type'],
    columns='Statistic',
    values='Value',
    aggfunc='first'
).reset_index()

# Rename columns for clarity
final_df.columns.name = None  # Remove the multiindex column name
final_df.rename(columns={
    'A': 'Area',
    'P': 'Production',
    'Y': 'Yield'
}, inplace=True)

print(final_df)
final_df.to_csv("data/structured_crop_yield.csv")

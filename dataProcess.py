import pandas as pd

# File paths
crop_yield_file = 'data/crop_yield.csv'  # Replace with your crop yield file path
weather_file = 'data/weather_data.csv'   # Replace with your weather file path
output_file = 'data/structured_data_full.csv'  # Final structured dataset path

# Load the crop yield dataset
crop_yield_df = pd.read_csv(crop_yield_file)

# Reshape crop yield data
# Extract years from the column names for Area, Production, Yield
crop_long = pd.wide_to_long(
    crop_yield_df,
    stubnames=[
        'BARLEY_A', 'BARLEY_P', 'BARLEY_Y', 'MAIZE_A', 'MAIZE_P', 'MAIZE_Y',
        'MILLET_A', 'MILLET_P', 'MILLET_Y', 'PADDY_A', 'PADDY_P', 'PADDY_Y',
        'WHEAT_A', 'WHEAT_P', 'WHEAT_Y'
    ],
    i='DISTRICT_NAME',
    j='YEAR',
    sep='_',
    suffix=r'\d+'
).reset_index()

# Load the weather dataset
weather_df = pd.read_csv(weather_file)

# Define seasons for Nepal
seasons = {
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11],
    'Winter': [12, 1, 2]
}

# Assign seasons to months
weather_df['SEASON'] = weather_df['MONTH'].apply(lambda x: next((season for season, months in seasons.items() if x in months), None))

# Aggregate weather data by DISTRICT, YEAR, and SEASON (including all relevant factors)
weather_agg = weather_df.groupby(['DISTRICT', 'YEAR', 'SEASON']).agg({
    'PRECIPITATION': 'sum',            # Total rainfall
    'TEMP_2M': 'mean',                 # Mean temperature
    'TEMP_2M_MAX': 'max',              # Maximum temperature
    'TEMP_2M_MIN': 'min',              # Minimum temperature
    'HUMIDITY_AT_2M': 'mean',          # Mean humidity
    'RELATIVE_HUMIDITY_2M': 'mean',    # Mean relative humidity
    'WIND_SPEED_10M': 'mean',          # Mean wind speed
    'WIND_SPEED_10M_MAX': 'max',       # Maximum wind speed
    'WIND_SPEED_10M_MIN': 'min',       # Minimum wind speed
    'SURFACE_PRESSURE': 'mean',        # Mean surface pressure
    'WET_BULB_TEMP_2M': 'mean',        # Mean wet bulb temperature
    'SURFACE_TEMP': 'mean'             # Mean surface temperature
}).reset_index()

# Pivot weather data to make seasonal features as columns
weather_pivot = weather_agg.pivot(index=['DISTRICT', 'YEAR'], columns='SEASON')
weather_pivot.columns = [f"{season.lower()}_{metric}" for season, metric in weather_pivot.columns]
weather_pivot.reset_index(inplace=True)

# Merge crop yield and weather data
final_df = pd.merge(crop_long, weather_pivot, left_on=['DISTRICT_NAME', 'YEAR'], right_on=['DISTRICT', 'YEAR'], how='inner')

# Drop unnecessary columns and save the final dataset
final_df.drop(columns=['DISTRICT'], inplace=True)
final_df.to_csv(output_file, index=False)

print(f"Structured dataset saved to {output_file}")

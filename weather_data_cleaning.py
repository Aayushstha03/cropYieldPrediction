import pandas as pd

weather_df = pd.read_csv("data/weather_data.csv")
# Adjust season names in the classification function
def classify_season(month):
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8, 9]:
        return "Summer"
    elif month in [10, 11]:
        return "Autumn"
    else:
        return "Winter"

weather_df['Season'] = weather_df['MONTH'].apply(classify_season)

# Aggregate data by district, year, and season
seasonal_aggregates = weather_df.groupby(['DISTRICT', 'YEAR', 'Season']).agg({
    'PRECIPITATION': 'sum',  # Total rainfall for the season
    'TEMP_2M': 'mean',       # Average temperature
    'HUMIDITY_AT_2M': 'mean', # Average humidity
    'WIND_SPEED_10M': 'mean', # Average wind speed
    # Add other aggregations as needed
}).reset_index()

# Pivot table to restructure data into columns for each season
pivoted_weather_df = seasonal_aggregates.pivot_table(
    index=['DISTRICT', 'YEAR'],
    columns='Season',
    values=['PRECIPITATION', 'TEMP_2M', 'HUMIDITY_AT_2M', 'WIND_SPEED_10M']
).reset_index()

# Flatten MultiIndex columns
pivoted_weather_df.columns = [
    f"{col[1]}_{col[0]}" if col[1] else col[0] 
    for col in pivoted_weather_df.columns
]

# Truncate all numerical columns to two decimal places
numeric_columns = pivoted_weather_df.select_dtypes(include=['float64', 'int64']).columns
pivoted_weather_df[numeric_columns] = pivoted_weather_df[numeric_columns].round(2)


# Rename columns to reflect the new season names
pivoted_weather_df.rename(columns={
    # Winter
    'Winter_PRECIPITATION': 'winter_rainfall',
    'Winter_TEMP_2M': 'winter_temperature',
    'Winter_HUMIDITY_AT_2M': 'winter_humidity',
    'Winter_WIND_SPEED_10M': 'winter_wind_speed',
    
    # Spring
    'Spring_PRECIPITATION': 'spring_rainfall',
    'Spring_TEMP_2M': 'spring_temperature',
    'Spring_HUMIDITY_AT_2M': 'spring_humidity',
    'Spring_WIND_SPEED_10M': 'spring_wind_speed',
    
    # Summer
    'Summer_PRECIPITATION': 'summer_rainfall',
    'Summer_TEMP_2M': 'summer_temperature',
    'Summer_HUMIDITY_AT_2M': 'summer_humidity',
    'Summer_WIND_SPEED_10M': 'summer_wind_speed',
    
    # Autumn
    'Autumn_PRECIPITATION': 'autumn_rainfall',
    'Autumn_TEMP_2M': 'autumn_temperature',
    'Autumn_HUMIDITY_AT_2M': 'autumn_humidity',
    'Autumn_WIND_SPEED_10M': 'autumn_wind_speed',
    
    # Optional: If additional variables like TEMP_2M_MAX, TEMP_2M_MIN exist
    'Winter_TEMP_2M_MAX': 'winter_temperature_max',
    'Winter_TEMP_2M_MIN': 'winter_temperature_min',
    'Spring_TEMP_2M_MAX': 'spring_temperature_max',
    'Spring_TEMP_2M_MIN': 'spring_temperature_min',
    'Summer_TEMP_2M_MAX': 'summer_temperature_max',
    'Summer_TEMP_2M_MIN': 'summer_temperature_min',
    'Autumn_TEMP_2M_MAX': 'autumn_temperature_max',
    'Autumn_TEMP_2M_MIN': 'autumn_temperature_min',
}, inplace=True)


print(pivoted_weather_df)
pivoted_weather_df.to_csv("data/structured_weather.csv")


# # Rename columns for clarity
# pivoted_weather_df.rename(columns={
#     'Winter_PRECIPITATION': 'winter_rainfall',
#     'Winter_TEMP_2M': 'winter_temperature',
#     'Winter_HUMIDITY_AT_2M': 'winter_humidity',
#     'Pre-monsoon_PRECIPITATION': 'pre_monsoon_rainfall',
#     'Pre-monsoon_TEMP_2M': 'pre_monsoon_temperature',
#     'Monsoon_PRECIPITATION': 'monsoon_rainfall',
#     'Post-monsoon_TEMP_2M': 'post_monsoon_temperature',
#     # Continue renaming for all features
# }, inplace=True)
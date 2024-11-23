import pandas as pd

# Load the dataset
file_path = "data/crop_yield.csv"
data = pd.read_csv(file_path)

# Reshape the data
melted_data = data.melt(
    id_vars=["DISTRICT_NAME"],  # Columns to keep
    var_name="Variable",        # Name for the new column of variable names
    value_name="Value"          # Name for the new column of values
)

# Extract Crop, Year, and Metric
melted_data["Crop"] = melted_data["Variable"].str.extract(r'^(.*?)_')[0]
melted_data["Metric"] = melted_data["Variable"].str.extract(r'_(.*?)_\d')[0]
melted_data["Year"] = melted_data["Variable"].str.extract(r'_(\d{4}\d{2})$')[0]

# Convert Year to a standard format (optional)
melted_data["Year"] = melted_data["Year"].apply(lambda x: f"19{x[:2]}-{x[2:]}" if int(x[:2]) < 50 else f"20{x[:2]}-{x[2:]}")

# Drop the original variable column
melted_data = melted_data.drop(columns=["Variable"])

# Pivot or group by as needed
print(melted_data.head())

melted_data.to_csv('data/structured_crop_yield.csv')
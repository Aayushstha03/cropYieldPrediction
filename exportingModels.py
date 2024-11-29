import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Ensure the directory for storing models exists
os.makedirs("models", exist_ok=True)

def export_random_forest_model(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    crop_name = file_path.split('/')[-1].split('_')[0]  # Extract crop name from file name

    # One-hot encode DISTRICT_NAME
    data = pd.get_dummies(data, columns=['DISTRICT_NAME'], prefix='DISTRICT', drop_first=True)

    # Prepare features (X) and target (y)
    X = data.drop(columns=['YEAR', 'CROP_TYPE', 'PRODUCTION'])
    y = data['PRODUCTION']

    # Train-test split
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Save the trained model
    model_path = f"models/{crop_name}_rf_model.pkl"
    joblib.dump(rf_model, model_path)
    print(f"Random Forest model for {crop_name} saved at {model_path}")

# List of file paths for datasets
file_paths = [
    "FinalDatasets/BARLEY_data_merged.csv",
    "FinalDatasets/MAIZE_data_merged.csv",
    "FinalDatasets/MILLET_data_merged.csv",
    "FinalDatasets/PADDY_data_merged.csv",
    "FinalDatasets/WHEAT_data_merged.csv",
]

# Loop through each file and export the model
for file_path in file_paths:
    export_random_forest_model(file_path)

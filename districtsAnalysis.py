import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Configure visualizations
sns.set_theme(style="whitegrid")

def district_error_analysis(file_paths):
    district_errors = {}

    for file_path in file_paths:
        # Load dataset
        data = pd.read_csv(file_path)
        crop_name = file_path.split('/')[-1].split('_')[0]  # Extract crop name

        # One-hot encode DISTRICT_NAME
        data = pd.get_dummies(data, columns=['DISTRICT_NAME'], prefix='DISTRICT', drop_first=True)

        # Prepare features and target
        X = data.drop(columns=['YEAR', 'CROP_TYPE', 'PRODUCTION'])
        y = data['PRODUCTION']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
        rf_model.fit(X_train, y_train)

        # Predict
        y_pred = rf_model.predict(X_test)

        # Calculate errors per district
        district_columns = [col for col in X.columns if col.startswith('DISTRICT_')]
        for district_col in district_columns:
            mask = X_test[district_col] == 1
            if mask.sum() > 0:
                district_name = district_col.replace('DISTRICT_', '')
                mse = mean_squared_error(y_test[mask], y_pred[mask]) if mask.any() else 0
                district_errors[district_name] = district_errors.get(district_name, 0) + mse

    # Convert results to DataFrame
    error_df = pd.DataFrame(list(district_errors.items()), columns=["District", "Total_Error"])
    error_df = error_df.sort_values(by="Total_Error", ascending=False).head(10)

    # Plot top 10 districts by error
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Total_Error", y="District", data=error_df, palette="Reds_r")
    plt.title("Top 10 Districts with Highest Prediction Errors (Across All Crops)")
    plt.xlabel("Total Prediction Error (MSE)")
    plt.ylabel("District")
    plt.show()  

    return error_df


# List of file paths
file_paths = [
    "FinalDatasets/BARLEY_data_merged.csv",
    "FinalDatasets/MAIZE_data_merged.csv",
    "FinalDatasets/MILLET_data_merged.csv",
    "FinalDatasets/PADDY_data_merged.csv",
    "FinalDatasets/WHEAT_data_merged.csv",
]

# Run district error analysis
district_error_results = district_error_analysis(file_paths)
print("Top 10 Districts with Highest Errors Across All Crops:")
print(district_error_results)

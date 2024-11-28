import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset for a single crop
file_path = "FinalDatasets/BARLEY_data_merged.csv"
data = pd.read_csv(file_path)

# One-hot encode the DISTRICT_NAME column
data = pd.get_dummies(data, columns=['DISTRICT_NAME'], prefix='DISTRICT', drop_first=True)

# Preprocess the dataset
# Drop unused columns and separate features (X) and target (y)
X = data.drop(columns=['YEAR', 'CROP_TYPE', 'PRODUCTION'])
y = data['PRODUCTION']

# Preprocessing: Scale features for SVR
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1),
    "Support Vector Regression": SVR(kernel='linear', C=10, epsilon=0.5)
}

# Define the number of folds for cross-validation
k = 10
kf = KFold(n_splits=k, shuffle=True, random_state=42)

# Perform K-Fold Cross-Validation for each model
results = {}
for model_name, model in models.items():
    if model_name == "Support Vector Regression":
        # Use scaled data for SVR
        scores = cross_val_score(model, X_scaled, y, cv=kf, scoring='r2')
    else:
        # Use original data for others
        scores = cross_val_score(model, X, y, cv=kf, scoring='r2')
    
    results[model_name] = scores
    print(f"{model_name} - R² Scores for {k}-Fold Cross Validation: {scores}")
    print(f"{model_name} - Mean R²: {scores.mean():.2f}, Std Dev: {scores.std():.2f}\n")

# Visualize the cross-validation results
plt.figure(figsize=(10, 6))
for model_name, scores in results.items():
    plt.plot(range(1, k + 1), scores, marker='o', label=model_name)

plt.title(f'{k}-Fold Cross Validation Results')
plt.xlabel('Fold Number')
plt.ylabel('R² Score')
plt.legend()
plt.grid()
plt.show()

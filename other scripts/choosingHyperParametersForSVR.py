import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# Load the dataset for a single crop
file_path = "FinalDatasets/BARLEY_data_merged.csv"
data = pd.read_csv(file_path)

# One-hot encode the DISTRICT_NAME column
data = pd.get_dummies(data, columns=['DISTRICT_NAME'], prefix='DISTRICT', drop_first=True)

# Preprocess the dataset
# Drop unused columns and separate features (X) and target (y)
X = data.drop(columns=['YEAR', 'CROP_TYPE','PRODUCTION'])
y = data['PRODUCTION']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the parameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'epsilon': [0.01, 0.1, 0.2, 0.5],
    'kernel': ['linear', 'rbf']
}

# Initialize SVR model
svr = SVR()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=svr, param_grid=param_grid, 
                        scoring='neg_mean_squared_error', 
                        cv=5, verbose=2, n_jobs=-1)

# Fit GridSearchCV
grid_search.fit(X_train_scaled, y_train)

# Retrieve best parameters and model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

print(f"Best Parameters: {best_params}")
print(f"Best Score: {-grid_search.best_score_:.4f}")  # Negative MSE is returned, so negate it for readability

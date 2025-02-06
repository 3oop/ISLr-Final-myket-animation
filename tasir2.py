import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
from lime.lime_tabular import LimeTabularExplainer
import joblib
import shap
import dalex as dx
import matplotlib.pyplot as plt
from sklearn.inspection import partial_dependence

# Load the data
clean_data = pd.read_csv("C:/Users/USER/Downloads/clean_data.csv")
data = clean_data
print(data)
# Drop unnecessary columns
data = data.drop(columns=['URL', 'Name', 'Country', 'Rade'])

# Define X and y
X = data.drop(columns=['Amtiaz'])
y = data['Amtiaz']

# Convert categorical variables to dummy variables
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create XGBoost model
model = xgb.XGBRegressor(n_estimators=200, random_state=42, objective="reg:squarederror")
model.fit(X_train, y_train)

# Predict using the model
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("XGBoost MSE:", mse)

# Save the model
joblib.dump(model, 'xgboost_model.pkl')

# Create Explainer for SHAP
explainer = shap.TreeExplainer(model)

# Calculate SHAP values for test data
shap_values = explainer.shap_values(X_test)

# Select a sample for interpretation
i = 0
shap.initjs()
shap.force_plot(explainer.expected_value, shap_values[i], X_test.iloc[i], feature_names=X.columns)

# Create explainer for breakDown
explainer = dx.Explainer(model, X_train, y_train)

# Select a sample for interpretation
instance = X_test.iloc[0]

# Create breakDown explanation
bd = explainer.predict_parts(instance)
bd.plot()

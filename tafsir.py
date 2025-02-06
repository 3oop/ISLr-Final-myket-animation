import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from lime.lime_tabular import LimeTabularExplainer
import joblib
import shap
import dalex as dx
import matplotlib.pyplot as plt
from sklearn.inspection import partial_dependence

# بارگذاری داده‌ها
clean_data = pd.read_csv("C:/Users/USER/Downloads/clean_data.csv")
data = clean_data
print(data)
# حذف ستون‌های غیر ضروری
data = data.drop(columns=['URL', 'Name', 'Country', 'Rade'])

# تعریف متغیرهای X و y
X = data.drop(columns=['Amtiaz'])
y = data['Amtiaz']

# تبدیل متغیرهای کیفی به دامی (dummy variables)
X = pd.get_dummies(X, drop_first=True)

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل Random Forest
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# پیش‌بینی با استفاده از مدل
y_pred = model.predict(X_test)

# محاسبه میانگین مربعات خطا
mse = mean_squared_error(y_test, y_pred)
print("Random Forest MSE:", mse)

joblib.dump(model, 'random_forest_model.pkl')



# ایجاد Explainer برای SHAP
explainer = shap.TreeExplainer(model)

# محاسبه مقادیر SHAP برای داده‌های تست
shap_values = explainer.shap_values(X_test)

# انتخاب یک نمونه برای تفسیر
i = 0
shap.initjs()
shap.force_plot(explainer.expected_value, shap_values[i], X_test.iloc[i], feature_names=X.columns)



# ایجاد explainer برای Break Down
explainer = dx.Explainer(model, X_train, y_train)

# انتخاب یک نمونه برای تفسیر
instance = X_test.iloc[0]

# ایجاد تفسیر Break Down
bd = explainer.predict_parts(instance)
bd.plot()

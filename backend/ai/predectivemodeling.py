# =========================================
# FINANCIAL PREDICTIVE MODELING TOOLKIT
# =========================================

# Core Libraries
import pandas as pd
import numpy as np

# Modeling Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import statsmodels.api as sm
from prophet import Prophet

import xgboost as xgb
import lightgbm as lgb

import tensorflow as tf
import torch
import torch.nn as nn
import torch.optim as optim

# =========================================
# 1️⃣ Pandas + NumPy — Data Wrangling
# =========================================

# Example: simulate financial data
np.random.seed(42)
dates = pd.date_range(start="2020-01-01", periods=100)
df = pd.DataFrame({
    "date": dates,
    "revenue": np.random.normal(1000, 100, 100).cumsum(),
    "marketing_spend": np.random.uniform(50, 200, 100)
})

# Add derived features
df["month"] = df["date"].dt.month
df["growth_rate"] = df["revenue"].pct_change().fillna(0)

print(df.head())

# =========================================
# 2️⃣ scikit-learn — Regression Example
# =========================================
X = df[["marketing_spend", "month", "growth_rate"]]
y = df["revenue"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
print("\n🔹 scikit-learn Regression Results")
print("R²:", r2_score(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))

# =========================================
# 3️⃣ statsmodels — ARIMA for Time Series
# =========================================
ts = df.set_index("date")["revenue"]
arima_model = sm.tsa.ARIMA(ts, order=(1, 1, 1)).fit()
forecast = arima_model.forecast(steps=5)
print("\n🔹 ARIMA Forecast:")
print(forecast)

# =========================================
# 4️⃣ Prophet — Time-Series Forecasting
# =========================================
prophet_df = df.rename(columns={"date": "ds", "revenue": "y"})
prophet_model = Prophet()
prophet_model.fit(prophet_df)

future = prophet_model.make_future_dataframe(periods=30)
forecast_prophet = prophet_model.predict(future)
print("\n🔹 Prophet Forecast (Last 5 Days):")
print(forecast_prophet.tail())

# =========================================
# 5️⃣ XGBoost — Gradient Boosting
# =========================================
xgb_model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)

print("\n🔹 XGBoost R²:", r2_score(y_test, y_pred_xgb))

# =========================================
# 6️⃣ LightGBM — Gradient Boosting
# =========================================
lgb_model = lgb.LGBMRegressor(n_estimators=200, learning_rate=0.1)
lgb_model.fit(X_train, y_train)
y_pred_lgb = lgb_model.predict(X_test)

print("\n🔹 LightGBM R²:", r2_score(y_test, y_pred_lgb))

# =========================================
# 7️⃣ TensorFlow — Deep Learning Regression
# =========================================
tf_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])
tf_model.compile(optimizer='adam', loss='mse')
tf_model.fit(X_train, y_train, epochs=50, verbose=0)

y_pred_tf = tf_model.predict(X_test).flatten()
print("\n🔹 TensorFlow RMSE:", mean_squared_error(y_test, y_pred_tf, squared=False))

# =========================================
# 8️⃣ PyTorch — Deep Learning Regression
# =========================================
class FinancialNN(nn.Module):
    def __init__(self, input_dim):
        super(FinancialNN, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
    def forward(self, x):
        return self.layers(x)

# Convert to tensors
X_train_t = torch.tensor(X_train.values, dtype=torch.float32)
y_train_t = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

model = FinancialNN(X_train_t.shape[1])
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Train
for epoch in range(200):
    optimizer.zero_grad()
    outputs = model(X_train_t)
    loss = criterion(outputs, y_train_t)
    loss.backward()
    optimizer.step()

# Predict
X_test_t = torch.tensor(X_test.values, dtype=torch.float32)
y_pred_torch = model(X_test_t).detach().numpy().flatten()
print("\n🔹 PyTorch RMSE:", mean_squared_error(y_test, y_pred_torch, squared=False))
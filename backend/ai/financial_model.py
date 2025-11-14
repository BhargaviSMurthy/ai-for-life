# =====================================
# Financial Prediction - Starter Project
# =====================================

# 1️⃣ Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error

# 2️⃣ Create a small dataset
# We'll simulate 12 months of data
data = {
    "month": np.arange(1, 13),
    "marketing_spend": [500, 700, 800, 1200, 1500, 1600, 1700, 2000, 2200, 2500, 2700, 3000]
}

# Let's assume revenue grows with marketing spend + some random noise
np.random.seed(42)
data["revenue"] = [spend * 1.5 + np.random.normal(0, 200) for spend in data["marketing_spend"]]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("financial_data.csv", index=False)
print("✅ Data created and saved as 'financial_data.csv'")
print(df.head())

# 3️⃣ Load the dataset (as you would in a real project)
df = pd.read_csv("financial_data.csv")

# 4️⃣ Prepare features (X) and target (y)
X = df[["marketing_spend", "month"]]   # input features
y = df["revenue"]                      # target we want to predict

# 5️⃣ Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6️⃣ Create and train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 7️⃣ Make predictions
y_pred = model.predict(X_test)

# 8️⃣ Evaluate model performance
r2 = r2_score(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred, squared=False)

print("\n📊 Model Evaluation:")
print(f"R² Score: {r2:.3f}")
print(f"RMSE: {rmse:.2f}")

# 9️⃣ Predict revenue for a new scenario
new_spend = np.array([[3500, 13]])  # next month, spend $3500
predicted_revenue = model.predict(new_spend)
print(f"\n💡 Predicted Revenue for month 13 with $3500 spend: ${predicted_revenue[0]:.2f}")

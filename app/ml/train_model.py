import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib


df = pd.read_csv("app/data/sanandaj_smart_grid_dataset_v2.csv")

# Features
X = df[[
    "hour",
    "temperature",
    "peak_hour",
    "holiday"
]]

# Target
y = df["consumption_kwh"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("MAE:", mae)

# Save model
joblib.dump(model, "app/ml/power_model.pkl")

print("Model saved successfully")
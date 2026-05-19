import joblib
import pandas as pd

model = joblib.load("app/ml/power_model.pkl")


def predict_consumption(data):

    input_data = pd.DataFrame([{
        "hour": data.hour,
        "temperature": data.temperature,
        "peak_hour": data.peak_hour,
        "holiday": data.holiday
    }])

    prediction = model.predict(input_data)

    return round(float(prediction[0]), 3)
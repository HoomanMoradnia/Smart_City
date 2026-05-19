from fastapi import APIRouter
from app.models.predict_model import PredictionInput
from app.services.prediction_service import predict_consumption

router = APIRouter()


@router.post("/predict")
def predict(data: PredictionInput):

    prediction = predict_consumption(data)

    alert = "normal"

    if prediction > 2:
        alert = "warning"

    if prediction > 3.5:
        alert = "critical"

    return {
        "predicted_consumption": prediction,
        "alert": alert
    }
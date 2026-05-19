from fastapi import APIRouter
from app.models.meter_model import MeterData
from app.services.meter_storage import meter_data_storage


router = APIRouter()


@router.post("/meter-data")
def receive_meter_data(data: MeterData):
    meter_data_storage.append(data.model_dump())
    return {
        "message": "Meter data received successfully.",
        "data": data
    }


@router.get("/latest-data")
def get_latest_data():
    return meter_data_storage[-10:]
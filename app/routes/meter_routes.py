from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.models.meter_model import MeterData
from app.models.database_models import MeterRecord
from app.database.db import SessionLocal


router = APIRouter()


@router.post("/meter-data")
def receive_meter_data(data: MeterData):
    
    db: Session = SessionLocal()

    new_record = MeterRecord(
        customer_id=data.customer_id,
        region_id=data.region_id,
        timestamp=data.timestamp,
        consumption_kwh=data.consumption_kwh,
        temperature=data.temperature
    )

    db.add(new_record)
    db.commit()
    db.flush(new_record)
    db.close()

    return {
        "message": "Meter data received successfully.",
    }


@router.get("/latest-data")
def get_latest_data():
    
    db: Session = SessionLocal()
    
    records = (
        db.query(MeterRecord)
        .order_by(MeterRecord.timestamp.desc())
        .limit(10)
        .all()
    )

    db.close()

    return records
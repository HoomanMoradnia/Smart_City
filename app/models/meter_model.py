from pydantic import BaseModel
from datetime import datetime


class MeterData(BaseModel):
    customer_id: int
    region_id: str
    timestamp: datetime
    consumption_kwh: float
    temperature: float
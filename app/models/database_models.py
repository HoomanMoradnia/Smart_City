from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database.db import Base


class MeterRecord(Base):

    __tablename__ = "meter_records"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    region_id = Column(String)
    timestamp = Column(DateTime)
    consumption_kwh = Column(Float)
    temperature = Column(Float)
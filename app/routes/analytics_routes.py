from fastapi import APIRouter
from app.services.analytics_service import (
    average_consumption,
    peak_hours,
    region_consumption
)


router = APIRouter()


@router.get("/analytics/average")
def avg_consumption():
    return average_consumption()


@router.get("/analytics/peak-hours")
def get_peak_hours():
    return peak_hours()


@router.get("/analytics/regions")
def get_region_consumption():
    return region_consumption()
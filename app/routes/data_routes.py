from fastapi import APIRouter
from app.services.data_service import (
    get_all_data,
    get_region_data,
    get_customer_data
)

router = APIRouter()


@router.get("/data")
def all_data():
    return get_all_data()


@router.get("/region/{region_id}")
def region_data(region_id: str):
    return get_region_data(region_id)


@router.get("/customer/{customer_id}")
def customer_data(customer_id: int):
    return get_customer_data(customer_id)
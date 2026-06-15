from fastapi import APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from app.services.dashboard_service import (
    dashboard_stats,
    region_chart_data,
    hourly_city_consumption,
    top_consumers,
    alert_statistics
)
from app.services.customer_service import (
    get_customers,
    get_customer_details,
    get_customer_chart_data
)
from app.services.pricing_service import (
    calculate_customer_bill,
    predict_month_end_usage,
    advanced_tariff_alert
)


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def dashboard(request: Request):

    stats = dashboard_stats()

    regions = region_chart_data()

    hourly = hourly_city_consumption()

    top_users = top_consumers()

    alerts = alert_statistics()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "stats": stats,
            "regions": regions,
            "hourly": hourly,
            "top_users": top_users,
            "alerts": alerts
        }
    )


@router.get("/customers")
def customers(request: Request, search: str = None, region: str = None, profile: str = None):

    customers_data = get_customers(search=search, region=region, profile=profile)

    return templates.TemplateResponse(
        request=request,
        name="customers.html",
        context={
            "customers": customers_data,
            "search": search,
            "region": region,
            "profile": profile
        }
    )


@router.get("/customers/{customer_id}")
def customer_detail(request: Request, customer_id: int):

    customer = get_customer_details(customer_id)

    if customer is None:
        return {"error": "Customer not found"}

    chart_data = get_customer_chart_data(customer_id)

    # Dynamic Pricing
    bill = calculate_customer_bill(customer_id)

    predicted_usage = (predict_month_end_usage(customer_id))

    alert = advanced_tariff_alert(bill["monthly_usage"], predicted_usage)

    return templates.TemplateResponse(
        request=request,
        name="customer_detail.html",
        context={
            "customer": customer,
            "chart_data": chart_data,
            "bill": bill,
            "predicted_usage": predicted_usage,
            "alert": alert
        }
    )
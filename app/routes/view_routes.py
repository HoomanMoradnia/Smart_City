from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.dashboard_service import dashboard_stats
from app.services.customer_service import (
    get_customers,
    get_customer_details,
    get_customer_chart_data
)
from app.services.pricing_service import (
    calculate_customer_bill,
    predict_month_end_usage,
    tariff_alert
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/")
def dashboard(request: Request):

    stats = dashboard_stats()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "stats": stats
        }
    )


@router.get("/customers")
def customers(request: Request):

    customers_data = get_customers()

    return templates.TemplateResponse(
        request=request,
        name="customers.html",
        context={
            "customers": customers_data
        }
    )


@router.get("/customers/{customer_id}")
def customer_detail(
    request: Request,
    customer_id: int
):

    customer = get_customer_details(
        customer_id
    )

    chart_data = get_customer_chart_data(
        customer_id
    )

    if customer is None:

        return {
            "error": "Customer not found"
        }

    # Dynamic Pricing
    bill = calculate_customer_bill(
        customer_id
    )

    predicted_usage = (
        predict_month_end_usage(
            customer_id
        )
    )

    alert = tariff_alert(
        predicted_usage
    )

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
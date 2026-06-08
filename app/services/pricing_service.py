import pandas as pd

DATA_PATH = "app/data/sanandaj_smart_grid_dataset_v2.csv"

df = pd.read_csv(DATA_PATH)


def get_tariff(monthly_usage):

    if monthly_usage <= 100:
        return 603

    elif monthly_usage <= 200:
        return 702

    elif monthly_usage <= 300:
        return 1506

    elif monthly_usage <= 400:
        return 2710

    elif monthly_usage <= 500:
        return 3113

    elif monthly_usage <= 600:
        return 3916

    return 4319


def calculate_customer_bill(customer_id):

    customer_df = df[
        df["customer_id"] == customer_id
    ]

    monthly_usage = round(
        customer_df["consumption_kwh"].sum(),
        2
    )

    tariff = get_tariff(
        monthly_usage
    )

    estimated_cost = round(
        monthly_usage * tariff,
        0
    )

    return {
        "monthly_usage": monthly_usage,
        "tariff": tariff,
        "estimated_cost": estimated_cost
    }


def predict_month_end_usage(customer_id):

    customer_df = df[
        df["customer_id"] == customer_id
    ]

    days_recorded = 30

    current_usage = (
        customer_df["consumption_kwh"]
        .sum()
    )

    daily_average = (
        current_usage / days_recorded
    )

    predicted_usage = (
        daily_average * 30
    )

    return round(
        predicted_usage,
        2
    )


def tariff_alert(predicted_usage):

    if predicted_usage > 600:

        return (
            "Critical: Highest tariff tier expected."
        )

    elif predicted_usage > 400:

        return (
            "Warning: Higher tariff tier expected."
        )

    elif predicted_usage > 300:

        return (
            "Notice: Approaching next tariff tier."
        )

    return (
        "Normal consumption."
    )
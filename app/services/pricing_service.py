import joblib
import pandas as pd


model = joblib.load(
    "app/ml/power_model.pkl"
)

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

    customer_df = df[df["customer_id"] == customer_id]

    monthly_usage = round(customer_df["consumption_kwh"].sum(), 2)

    tariff = get_tariff(monthly_usage)

    bill_data = calculate_step_bill(monthly_usage)

    return {
        "monthly_usage": monthly_usage,
        "tariff": tariff,
        "estimated_cost": bill_data["total_cost"],
        "breakdown": bill_data["breakdown"]
    }


def calculate_step_bill(monthly_usage):

    tiers = [
        (100, 603),
        (100, 702),
        (100, 1506),
        (100, 2710),
        (100, 3113),
        (100, 3916),
        (float("inf"), 4319)
    ]

    remaining = monthly_usage

    total_cost = 0

    breakdown = []

    for limit, tariff in tiers:

        if remaining <= 0:
            break

        consumed = min(remaining, limit)

        cost = consumed * tariff

        breakdown.append({
            "consumption": round(consumed, 2),
            "tariff": tariff,
            "cost": round(cost)
        })

        total_cost += cost

        remaining -= consumed

    return {
        "total_cost": round(total_cost),
        "breakdown": breakdown
    }


def predict_month_end_usage(customer_id):

    customer_df = df[df["customer_id"] == customer_id]

    if customer_df.empty:
        return 0

    last_record = customer_df.iloc[-1]

    predicted_hourly_usage = model.predict(
        pd.DataFrame([{
            "hour": last_record["hour"],
            "temperature": last_record["temperature"],
            "peak_hour": last_record["peak_hour"],
            "holiday": last_record["holiday"]}])
    )[0]

    current_usage = (customer_df["consumption_kwh"].sum())

    predicted_usage = (current_usage + predicted_hourly_usage * 24)

    return round(predicted_usage, 2)


def tariff_alert(predicted_usage): # This function most be removed later.

    if predicted_usage > 600:
        return ("Critical: Highest tariff tier expected.")

    elif predicted_usage > 400:
        return ("Warning: Higher tariff tier expected.")

    elif predicted_usage > 300:
        return ("Notice: Approaching next tariff tier.")

    return ("Normal consumption.")


def next_tariff_threshold(monthly_usage):

    thresholds = [100, 200, 300, 400, 500, 600]

    for threshold in thresholds:
        if monthly_usage < threshold:
            return threshold

    return None


def advanced_tariff_alert(current_usage, predicted_usage):

    threshold = next_tariff_threshold(current_usage)

    if threshold is None:
        return ("Critical: Highest tariff tier.")

    if predicted_usage >= threshold:
        return (
            f"Warning: predicted usage "
            f"may exceed "
            f"{threshold} kWh tier."
        )

    return ("Normal consumption.")
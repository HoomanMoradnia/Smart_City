import pandas as pd

DATA_PATH = "app/data/sanandaj_smart_grid_dataset_v2.csv"

df = pd.read_csv(DATA_PATH)


def dashboard_stats():
    return {
        "customers": int(df["customer_id"].nunique()),
        "regions": int(df["region_id"].nunique()),
        "average_consumption": round(df["consumption_kwh"].mean(), 2),
        "max_consumption": round(df["consumption_kwh"].max(), 2)
    }


def region_chart_data():

    region_data = (df.groupby("region_id")["consumption_kwh"].mean().reset_index())

    return {
        "labels": region_data["region_id"].tolist(),
        "values": region_data["consumption_kwh"].round(2).tolist()
    }


def hourly_city_consumption():

    hourly_data = (df.groupby("hour")["consumption_kwh"].mean().reset_index())

    return {
        "labels": hourly_data["hour"].tolist(),
        "values": hourly_data["consumption_kwh"].round(2).tolist()
    }


def top_consumers():
    consumers = (df.groupby("customer_id")["consumption_kwh"].sum().sort_values(ascending=False).head(5))

    return consumers.to_dict()


def alert_statistics():

    alerts = (df["alert"].value_counts().to_dict())

    return alerts
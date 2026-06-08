import pandas as pd

DATA_PATH = "app/data/sanandaj_smart_grid_dataset_v2.csv"

df = pd.read_csv(DATA_PATH)


def dashboard_stats():

    return {
        "customers": int(df["customer_id"].nunique()),
        "regions": int(df["region_id"].nunique()),
        "average_consumption": round(
            df["consumption_kwh"].mean(), 2
        ),
        "max_consumption": round(
            df["consumption_kwh"].max(), 2
        )
    }
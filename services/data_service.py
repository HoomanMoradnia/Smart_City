import pandas as pd

DATA_PATH = "app/data/sanandaj_smart_grid_dataset_v2"

df = pd.read_csv(DATA_PATH)


def get_all_data():
    return df.to_dict(orient="records")


def get_region_data(region_id: str):
    filtered = df[df["region_id"] == region_id]
    return filtered.to_dict(orient="records")


def get_customer_data(customer_id: int):
    filtered = df[df["customer_id"] == customer_id]
    return filtered.to_dict(orient="records")
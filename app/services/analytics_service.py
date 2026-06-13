import pandas as pd


DATA_PATH = "app/data/sanandaj_smart_grid_dataset_v2.csv"

df = pd.read_csv(DATA_PATH)


def average_consumption():
    avg = df["consumption_kwh"].mean()
    return {"average_consumption": round(avg, 3)}


def peak_hours():
    peak_data = (df.groupby("hour")["consumption_kwh"].mean().sort_values(ascending=False))
    return peak_data.head(5).to_dict()


def region_consumption():
    region_data = (df.groupby("region_id")["consumption_kwh"].mean())
    return region_data.to_dict()
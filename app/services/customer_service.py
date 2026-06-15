import pandas as pd

DATA_PATH = "app/data/sanandaj_smart_grid_dataset_v2.csv"

df = pd.read_csv(DATA_PATH)


def get_customers(search=None, region=None, profile=None):

    customers = (df.groupby("customer_id")
        .agg({
            "region_id": "first",
            "customer_profile": "first",
            "consumption_kwh": "mean"
        })
        .reset_index()
    )

    if search:
        customers = customers[customers["customer_id"].astype(str).str.contains(str(search), case=False)]

    if region:
        customers = customers[customers["region_id"] == region]

    if profile:
        customers = customers[customers["customer_profile"].str.lower() == profile.lower()]

    return customers.to_dict(orient="records")


def get_customer_details(customer_id: int):

    customer_df = df[df["customer_id"] == customer_id]

    if customer_df.empty:
        return None

    return {
        "customer_id": customer_id,
        "region_id": customer_df["region_id"].iloc[0],
        "profile":customer_df["customer_profile"].iloc[0],
        "avg_consumption":round(customer_df["consumption_kwh"].mean(), 2),
        "max_consumption":round(customer_df["consumption_kwh"].max(), 2),
        "records":len(customer_df)
    }


def get_customer_chart_data(customer_id: int):

    customer_df = df[df["customer_id"] == customer_id].copy()

    if customer_df.empty:
        return None

    chart_df = customer_df.tail(168)

    return {
        "labels": chart_df["datetime"].tolist(),
        "values": chart_df["consumption_kwh"].tolist()
    }
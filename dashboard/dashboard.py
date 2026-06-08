import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Smart Grid Dashboard",
    layout="wide"
)

st.title("⚡ Smart City Dashboard")

# -----------------------------
# Average Consumption
# -----------------------------

avg_response = requests.get(f"{API_URL}/analytics/average")

avg_data = avg_response.json()

st.metric(
    label="Average Consumption",
    value=f"{avg_data['average_consumption']} kWh"
)

# -----------------------------
# Region Consumption
# -----------------------------

region_response = requests.get(
    f"{API_URL}/analytics/regions"
)

region_data = region_response.json()

region_df = pd.DataFrame({
    "Region": list(region_data.keys()),
    "Consumption": list(region_data.values())
})

fig_regions = px.bar(
    region_df,
    x="Region",
    y="Consumption",
    title="Average Consumption by Region"
)

st.plotly_chart(fig_regions, use_container_width=True)

# -----------------------------
# Peak Hours
# -----------------------------

peak_response = requests.get(
    f"{API_URL}/analytics/peak-hours"
)

peak_data = peak_response.json()

peak_df = pd.DataFrame({
    "Hour": list(peak_data.keys()),
    "Consumption": list(peak_data.values())
})

fig_peak = px.line(
    peak_df,
    x="Hour",
    y="Consumption",
    title="Peak Consumption Hours"
)

st.plotly_chart(fig_peak, use_container_width=True)

# -----------------------------
# Latest Smart Meter Data
# -----------------------------

latest_response = requests.get(
    f"{API_URL}/latest-data"
)

latest_data = latest_response.json()

st.subheader("Latest Meter Data")

st.dataframe(latest_data)
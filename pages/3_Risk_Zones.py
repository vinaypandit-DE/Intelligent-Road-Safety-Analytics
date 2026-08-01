import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")

st.title("📍 Road Accident Risk Zones")

# ------------------------
# Load Data
# ------------------------

DATA_DIR = Path(__file__).parent.parent / "data"

risk_df = pd.read_csv(DATA_DIR / "risk_zones.csv")

# ------------------------
# KPIs
# ------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Districts",
        len(risk_df)
    )

with col2:
    st.metric(
        "Highest Risk Score",
        round(risk_df["Risk_Score"].max(),2)
    )

with col3:
    st.metric(
        "Average Risk Score",
        round(risk_df["Risk_Score"].mean(),2)
    )

st.divider()

# ------------------------
# Search
# ------------------------

district = st.selectbox(
    "Search District",
    ["All"] + sorted(risk_df["Local_Authority_(District)"].tolist())
)

if district != "All":
    filtered_df = risk_df[
        risk_df["Local_Authority_(District)"] == district
    ]
else:
    filtered_df = risk_df

# ------------------------
# Top Risk Zones
# ------------------------

st.subheader("Top Risk Zones")

st.dataframe(
    filtered_df.sort_values(
        "Risk_Score",
        ascending=False
    ),
    use_container_width=True
)

# ------------------------
# Risk Score Chart
# ------------------------

st.subheader("Top 20 Highest Risk Districts")

top20 = risk_df.sort_values(
    "Risk_Score",
    ascending=False
).head(20)

st.bar_chart(
    top20.set_index(
        "Local_Authority_(District)"
    )["Risk_Score"]
)
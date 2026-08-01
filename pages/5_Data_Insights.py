import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")

st.title("📈 Road Accident Data Insights")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "cleaned_data.csv")

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Records", len(df))

with col2:
    st.metric("Districts", df["Local_Authority_(District)"].nunique())

with col3:
    st.metric("Vehicle Types", df["Vehicle_Type"].nunique())

st.divider()

st.subheader("Accident Severity Distribution")

st.bar_chart(
    df["Accident_Severity"].value_counts()
)

st.subheader("Weather Conditions")

st.bar_chart(
    df["Weather_Conditions"].value_counts()
)

st.subheader("Road Surface Conditions")

st.bar_chart(
    df["Road_Surface_Conditions"].value_counts()
)

st.subheader("Vehicle Types")

st.bar_chart(
    df["Vehicle_Type"].value_counts().head(10)
)
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ----------------------------
# Load Models
# ----------------------------

MODEL_DIR = Path(__file__).parent.parent / "models"

model = joblib.load(MODEL_DIR / "xgboost_model.pkl")
preprocessor = joblib.load(MODEL_DIR / "preprocessor.pkl")
label_encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")

# ----------------------------
# Load Dataset
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "cleaned_data.csv")

# Same preprocessing used during training
df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

df = df.drop(
    columns=[
        "Accident_Index",
        "Accident Date",
        "Latitude",
        "Longitude",
        "Time",
        "Accident_Severity",
    ]
)

# ----------------------------
# UI
# ----------------------------

st.title("🚗 Accident Severity Prediction")

st.write("Enter accident details below.")

col1, col2 = st.columns(2)

with col1:

    month = st.selectbox("Month", sorted(df["Month"].unique()))

    day = st.selectbox("Day of Week", sorted(df["Day_of_Week"].unique()))

    junction_control = st.selectbox(
        "Junction Control",
        sorted(df["Junction_Control"].unique())
    )

    junction_detail = st.selectbox(
        "Junction Detail",
        sorted(df["Junction_Detail"].unique())
    )

    light = st.selectbox(
        "Light Conditions",
        sorted(df["Light_Conditions"].unique())
    )

    road_surface = st.selectbox(
        "Road Surface",
        sorted(df["Road_Surface_Conditions"].unique())
    )

    road_type = st.selectbox(
        "Road Type",
        sorted(df["Road_Type"].unique())
    )

    weather = st.selectbox(
        "Weather",
        sorted(df["Weather_Conditions"].unique())
    )

with col2:

    district = st.selectbox(
        "District",
        sorted(df["Local_Authority_(District)"].unique())
    )

    police = st.selectbox(
        "Police Force",
        sorted(df["Police_Force"].unique())
    )

    vehicle = st.selectbox(
        "Vehicle Type",
        sorted(df["Vehicle_Type"].unique())
    )

    urban = st.selectbox(
        "Urban/Rural",
        sorted(df["Urban_or_Rural_Area"].unique())
    )

    speed = st.number_input(
        "Speed Limit",
        10,
        100,
        30
    )

    vehicles = st.number_input(
        "Number of Vehicles",
        1,
        20,
        2
    )

    casualties = st.number_input(
        "Number of Casualties",
        1,
        20,
        1
    )

    hour = st.slider(
        "Hour",
        0,
        23,
        12
    )

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict Severity", use_container_width=True):

    input_df = pd.DataFrame({

        "Month":[month],
        "Day_of_Week":[day],
        "Year":[2022],
        "Junction_Control":[junction_control],
        "Junction_Detail":[junction_detail],
        "Light_Conditions":[light],
        "Local_Authority_(District)":[district],
        "Carriageway_Hazards":["None"],
        "Number_of_Casualties":[casualties],
        "Number_of_Vehicles":[vehicles],
        "Police_Force":[police],
        "Road_Surface_Conditions":[road_surface],
        "Road_Type":[road_type],
        "Speed_limit":[speed],
        "Urban_or_Rural_Area":[urban],
        "Weather_Conditions":[weather],
        "Vehicle_Type":[vehicle],
        "Hour":[hour]

    })

    X = preprocessor.transform(input_df)

    prediction = model.predict(X)

    probability = model.predict_proba(X).max()

    severity = label_encoder.inverse_transform(prediction)[0]

    st.success(f"### Predicted Severity : {severity}")

    #st.metric(
        #"Prediction Confidence",
        #f"{probability*100:.2f}%"
    #)
import streamlit as st

st.set_page_config(
    page_title="Intelligent Road Safety Analytics",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Intelligent Road Safety Analytics Dashboard")

st.markdown("""
Welcome to the **Intelligent Road Safety Analytics System**.

This project demonstrates an end-to-end Big Data Analytics pipeline built using:

- Apache Spark
- PySpark
- Spark SQL
- Scikit-learn
- XGBoost
- Apache Airflow
- Streamlit
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Road Accident Records", "300K+")

with col2:
    st.metric("Machine Learning Models", "2")

st.divider()

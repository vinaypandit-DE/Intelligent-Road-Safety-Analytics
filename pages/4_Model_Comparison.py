import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📊 Machine Learning Model Comparison")

# ---------------------------------------
# Model Metrics
# ---------------------------------------

comparison = pd.DataFrame({

    "Model":[
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy":[
        0.84,
        0.75
    ],

    
    "F1 Score":[
        0.77,
        0.71
    ]

})

# ---------------------------------------
# Best Model
# ---------------------------------------

best_model = comparison.loc[
    comparison["Accuracy"].idxmax(),
    "Model"
]

st.success(f"🏆 Best Performing Model : {best_model}")

# ---------------------------------------
# Metrics Table
# ---------------------------------------

st.subheader("Performance Metrics")

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------
# Accuracy
# ---------------------------------------

st.subheader("Accuracy")

st.bar_chart(
    comparison.set_index("Model")["Accuracy"]
)



# ---------------------------------------
# F1 Score
# ---------------------------------------

st.subheader("F1 Score")

st.bar_chart(
    comparison.set_index("Model")["F1 Score"]
)
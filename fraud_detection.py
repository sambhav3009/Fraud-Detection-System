# import streamlit as st
# import pandas as pd
# import joblib

# model=joblib.load("models/final_fraud_detection_model.pkl")

# st.title("Fraud Detection Prediction App")

# st.markdown("Please enter the transaction details and use the predict button")

# st.divider()

# transaction_type=st.selectbox("Transaction Type", [ "PAYMENT", "TRANSFER", "CASH_OUT", "TRANSFER", "DEPOSIT"])
# amount=st.number_input("Amount", min_value=0.0, value=10000.0)
# oldbalanceOrg=st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
# newbalanceOrig=st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
# oldbalanceDest=st.number_input("Old Balance (Receiver)", min_value=0.0, value=5000.0)
# newbalanceDest=st.number_input("New Balance (Receiver)", min_value=0.0, value=6000.0)

# if st.button("Predict"):
#     input_data=pd.DataFrame([{
#         "type":transaction_type,
#         "amount":amount,
#         "oldbalanceOrg":oldbalanceOrg,
#         "newbalanceOrig":newbalanceOrig,
#         "oldbalanceDest":oldbalanceDest,
#         "newbalanceDest":newbalanceDest
#     }])

#     prediction=model.predict(input_data)[0]

#     st.subheader(f"Prediction: '{int(prediction)}'")

#     if prediction==1:
#         st.error("The transaction can be fraudulent.")
#     else:
#         st.success("The transaction looks like it is not fraudulent.")

import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(

    page_title="Fraud Detection Dashboard",

    page_icon="🛡️",

    layout="centered"

)

# -------------------------------
# Load Model
# -------------------------------

model = joblib.load(

    "models/final_fraud_detection_model.pkl"

)

BEST_THRESHOLD = 0.95

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("📌 About")

st.sidebar.write("""

### Fraud Detection System

Final Model: Random Forest

Threshold: 0.95

Features Used:

- Transaction Type

- Amount

- Sender Balance

- Receiver Balance

- Engineered Balance Difference Features

""")

# -------------------------------
# Main Title
# -------------------------------

st.title("🛡️ Fraud Detection Dashboard")

st.write(

    "Enter transaction details and click Predict."

)

st.divider()

# -------------------------------
# Inputs
# -------------------------------

transaction_type = st.selectbox(

    "Transaction Type",

    [

        "PAYMENT",

        "TRANSFER",

        "CASH_OUT",

        "CASH_IN",

        "DEBIT"

    ]

)

amount = st.number_input(

    "Transaction Amount",

    min_value=0.0,

    value=10000.0

)

oldbalanceOrg = st.number_input(

    "Sender Old Balance",

    min_value=0.0,

    value=10000.0

)

newbalanceOrig = st.number_input(

    "Sender New Balance",

    min_value=0.0,

    value=9000.0

)

oldbalanceDest = st.number_input(

    "Receiver Old Balance",

    min_value=0.0,

    value=5000.0

)

newbalanceDest = st.number_input(

    "Receiver New Balance",

    min_value=0.0,

    value=6000.0

)

# -------------------------------
# Predict Button
# -------------------------------

if st.button("🔍 Predict"):

    balanceDiffOrig = (

        oldbalanceOrg

        -

        newbalanceOrig

    )

    balanceDiffDest = (

        newbalanceDest

        -

        oldbalanceDest

    )

    input_data = pd.DataFrame([{

        "type": transaction_type,

        "amount": amount,

        "oldbalanceOrg": oldbalanceOrg,

        "newbalanceOrig": newbalanceOrig,

        "oldbalanceDest": oldbalanceDest,

        "newbalanceDest": newbalanceDest,

        "balanceDiffOrig": balanceDiffOrig,

        "balanceDiffDest": balanceDiffDest

    }])

    probability = model.predict_proba(

        input_data

    )[0][1]

    prediction = int(

        probability >= BEST_THRESHOLD

    )

    st.divider()

    st.subheader("Prediction Result")

    st.metric(

        "Fraud Probability",

        f"{probability:.2%}"

    )

    if prediction == 1:

        st.error(

            "🚨 High Fraud Risk"

        )

        st.write(

            "This transaction should be investigated."

        )

    else:

        st.success(

            "✅ Transaction Appears Legitimate"

        )

        st.write(

            "No immediate fraud indicators detected."

        )

    st.divider()

    st.subheader("Transaction Summary")

    st.dataframe(

        input_data,

        use_container_width=True

    ) 
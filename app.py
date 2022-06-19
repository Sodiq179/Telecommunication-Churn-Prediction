import pickle
import numpy as np
import pandas as pd
import streamlit as st

(model, call_prices) = pickle.load(open("churnModel.pkl", "rb"))


def telecom_churn_prediction(customerDetails):
    input_data = pd.DataFrame(customerDetails, index = [0])
    prediction = model.predict(input_data)

    if prediction == 0:
        report =  "This customer is not likely to churn"
    else:
        report = "This customer is likely to churn"

    return report



def main():

    st.title("Telecommunication Churn Prediction")

    account_length = st.number_input("Account Length")
    area_code = st.selectbox("Area Code", ["408","415","510"])
    voice_mail_plan = st.selectbox("Voicemail Plan", ["Yes", "No"])
    international_plan = st.selectbox("International Plan", ["Yes", "No"])
    customer_service_calls = st.number_input("Customer Service Calls")
    number_vmail_messages = st.number_input("Number of Voicemail Messages")
    total_day_calls = st.number_input("Total Day Calls")
    total_day_minutes = st.number_input("Total Day Minutes")
    total_eve_calls = st.number_input("Total Evening Calls")
    total_eve_minutes = st.number_input("Total Evening Minutes")
    total_night_calls = st.number_input("Total Night Calls")
    total_night_minutes = st.number_input("Total Night Minutes")
    total_intl_calls = st.number_input("Total International Calls")
    total_intl_minutes = st.number_input("Total International Minutes")
    
    customerDetails = {'account_length': account_length,
                    'area_code': area_code,
                    'customer_service_calls': customer_service_calls,
                    'international_plan': 'No',
                    'number_vmail_messages': number_vmail_messages,
                    'total_day_calls': total_day_calls,
                    'total_day_charge':  total_day_minutes * call_prices["Day_charge"],
                    'total_day_minutes':  total_day_minutes,
                    'total_eve_calls':  total_eve_calls,
                    'total_eve_charge': total_eve_minutes * call_prices["Eve_charge"],
                    'total_eve_minutes': total_eve_minutes,
                    'total_intl_calls': total_intl_calls,
                    'total_intl_charge': total_intl_minutes * call_prices["Intl_charge"],
                    'total_intl_minutes': total_intl_minutes,
                    'total_night_calls': total_night_calls,
                    'total_night_charge': total_night_minutes * call_prices["Night_charge"],
                    'total_night_minutes': total_night_minutes,
                    'voice_mail_plan': voice_mail_plan}

    if st.button("Predict"):
        predictResult = telecom_churn_prediction(customerDetails)
        st.success(predictResult)

if __name__ == "__main__":
    main()
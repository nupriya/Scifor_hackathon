import streamlit as st
import pandas as pd
import numpy as np
import urllib
import json
import base64
import datetime
import pickle
import joblib

# Load the model
model = joblib.load('Price_pred.pkl')

def main():
    # Streamlit app layout
    st.title('Price Prediction App')
    

    # Input fields
    freq = st.number_input('Frequency of orders', value=0)
    price = st.number_input('Price', value=0)
    freight_value = st.number_input('Freight Value', value=0)
    product_name_length = st.number_input('Product Length', value=0)
    product_photos_qty = st.number_input('Product Quantity', value=0)
    estimated_delivery_time = st.number_input('Estimated Delivery Time', value=0)

    # Make prediction
    if st.button('Predict'):
        input_data = [[freq, price, freight_value, product_name_length, product_photos_qty, estimated_delivery_time]]
        prediction = model.predict(input_data)
        st.write(f'The predicted price is: {prediction[0]}')

if __name__ == "__main__":
    main()

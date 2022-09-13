import xgboost as xgb
import streamlit as st
import pandas as pd

from .streamlit_fhs import Cantidad, Class_cliente, Margen

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('XGB_1.json')

#Caching the model for faster loading
@st.cache

def predict(Cantidad, Class_cliente, Margen):
    #Predicting the price of the carat
    if Class_cliente == 0:
        Class_cliente = 1
    elif Class_cliente == 1:
        Class_cliente = 2
    elif Class_cliente == 2:
        Class_cliente = 3

    prediction = model.predict(pd.DataFrame([[Cantidad, Class_cliente, Margen]], columns=['Cantidad', 'Class_Cliente', 'Margen']))
    return prediction

st.header('Enter the characteristics of the offer:')

Cantidad = st.number_input('Cantidad:', min_value=0, value=1)
Class_cliente = st.selectbox('Clasificación CLiente:', ['0', '1', '2'])
Margen = st.number_input('Margen:', min_value=0.0, max_value=1.0, value=0.05)


if st.button('Predict Price'):
    price = predict(Cantidad, Class_cliente, Margen)
    st.success(f'The optimal priceis ${price[0]:.2f} EUR')
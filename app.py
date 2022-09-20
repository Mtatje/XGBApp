import numpy as np
import pandas as pd
import pickle 
import streamlit as st

pickle_a=open("xgb.pkl","rb")
regressor=pickle.load(pickle_a) # our model

def predict_chance(Cantidad, Class_cliente, Margen):
    prediction=regressor.predict([[Cantidad,Class_cliente,Margen]]) #predictions using our model
    return prediction 


def main():
    st.title("Optimal Price Prediction") #simple title for the app
    html_temp="""
        <div>
        <h2>Optimal Price Prediction ML app</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    Cantidad=st.number_input("Cantidad")
    Class_cliente=st.number_input("Classificación Cliente")
    Margen=st.number_input("Margen %")#giving inputs as used in building the model
    result=""
    if st.button("Predict"):
        result=predict_chance(Cantidad, Class_cliente, Margen) #result will be displayed if button is pressed
    st.success("The optimal price for this offer is {}".format(result))
        
if __name__=='__main__':
    main()
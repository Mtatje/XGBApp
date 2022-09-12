!pip install streamlit
import streamlit as st

from google.colab import drive 
drive.mount('/content/drive')

%cd /content/drive/MyDrive/Pricing

Cantidad = st.text_input('Cantidad mts.')
Margen = st.text_input('Margen Deseado')
Clasificación_Cliente = st.text_input('Clasificación Cliente')
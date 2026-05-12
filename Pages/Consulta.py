import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")  # leitura do arquivo com pandas

st.title("Clientes cadastrados")
st.divider()

st.dataframe(dados)
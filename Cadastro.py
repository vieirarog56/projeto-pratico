##################################
# projeto pratico - parte 1
#                 - parte 2
##################################

import streamlit as st
import pandas as pd
from datetime import date

# quando temos mais de um arquivo pages a tela ja tem a divisao no lado esquerdo

def gravar_dados(nome,data_nasc,tipo):
#    pass
    if nome and data_nasc <= date.today():
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n")   # f string o \n importante -quebra de linha no excell
        st.session_state["sucesso"] = True 
    else:
        st.session_state["sucesso"] = False
    

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon = "🔨"
)

st.title("Cadastro de Clientes")
st.divider()  # linha separadora

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")
dt_nasc = st.date_input("Data nascimnento",format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de Cliente",
                    ["Pessoa Jurídica",
                    "Pessoa Física"])
btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome,dt_nasc,tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                  icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")
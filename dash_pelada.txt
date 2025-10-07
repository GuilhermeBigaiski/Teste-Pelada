import streamlit as st
from datetime import date

st.title("Formulário da Pelada de Quinta")

# Data da partida
data_partida = st.date_input("Data da Partida", value=date.today())

# Time do jogador
time = st.selectbox("Time", ["Panela", "Antis"])

# Nome do jogador
jogador = st.text_input("Nome do Jogador")

# Gols
gols = st.number_input("Gols Marcados", min_value=0, max_value=10, step=1)

# Botão de envio
if st.button("Enviar"):
    st.success(f"Dados salvos para {jogador}: {gols} gols no time {time} em {data_partida}")
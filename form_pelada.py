import streamlit as st

# Datas fictícias das peladas
datas_pelada = [
    "2025-07-25", "2025-08-01", "2025-08-08", "2025-08-15"
]

# Jogadores fictícios
jogadores = ["Murilo", "Gui Kit", "Pedro", "Ramon", "Raphael", "Mene", "Cezar", "Gigio"]

st.title("Formulário de Gols - Pelada Quinta-feira")

# Seleção de data
data_escolhida = st.selectbox("Selecione a data da pelada:", datas_pelada)

st.write("---")
st.subheader("Preencha os dados dos jogadores:")

dados_partida = []

for jogador in jogadores:
    with st.expander(f"{jogador}"):
        time = st.radio("Time:", ["Panela", "Antis"], key=jogador+"_time")
        gols = st.number_input("Gols marcados:", min_value=0, max_value=10, step=1, key=jogador+"_gols")
        dados_partida.append({
            "jogador": jogador,
            "time": time,
            "gols": gols
        })

# Botão de envio
if st.button("Salvar Dados"):
    st.success("Dados preenchidos com sucesso!")
    st.write("🔎 Resumo dos dados registrados:")
    st.dataframe(dados_partida)
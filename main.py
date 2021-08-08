import streamlit as st
import pandas as pd


@st.cache
def load_data():

    data = pd.read_csv('produtores_por_estado.csv')
    filtro = data.produtores > 1
    prod = data[filtro]
    releitura = prod.head()
    dados = releitura
    return dados

# carregar os dados
df = load_data()
filter = pd.DataFrame(df, columns=['produtores', 'estado'])
#if st.sidebar.checkbox("Mostrar dados?"):
#    st.write(filter)

st.sidebar.header("Parâmetros")
st.sidebar.markdown("""
A base de dados de produtores por estado.
""")
st.sidebar.table(filter)
st.map(df)


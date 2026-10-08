import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="Dashboard - Indicador 7",
    layout="wide"
)

st.title("Dashboard - Indicador 7")

dados = {
    "Categoria": ["A", "B", "C", "D"],
    "Valor": [10, 20, 15, 25]
}

df = pd.DataFrame(dados)

fig, ax = plt.subplots()

ax.bar(df["Categoria"], df["Valor"])
ax.set_title("Indicador 7")
ax.set_xlabel("Categoria")
ax.set_ylabel("Valor")

st.pyplot(fig)
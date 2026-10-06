import streamlit as st
import pandas as pd

st.title("Padaria da Turma 3C2")
st.header("Sistema da Padaria")
st.subheader("Escolha seus produto")
st.write("Selecione os produtos que deseja comprar!")

produtos = pd.DataFrame({
    "Produto": [
        "Pap",
        "Pao de queijo",
        "Coxinha",
        "Bolo de chocolate",
        "Café",
        "Suco"
    ],
    "Preco": [
        0.80,
        2.50,
        6.00,
        5.00,
        8.00,
        3.00,
        5.00
    ]
})

st.write("Produtos disponíveis")
st.dataframe(produtos)

escolhidos = st.multiselect(
    "Escolha os produtos:",
    produtos["Produto"]
)

quantidade = st.number_input(
    "Escolha a quantidade:",
    min_value=1,
    value=1
)

if st.button("Calcular valor  total"):

    if len(escolhidos) > 0:

        selecionados = produtos[
            produtos["Produto"].isin(escolhidos)
        ]

        subtotal = selecionados["Preço"].sum()

        total = subtotal * quantidade

        st.subheader("Resumo da compra")

        st.write("Produtos escolhidos:")
        st.dataframe(selecionados)

        st.write(f"Subtotal: R$ {subtotal:.2f}")
        st.write(f"Quantidade: {quantidade}")

        st.success(f"Valor total: R$ {total:.2f}")

    else:
        st.warning("Escolha pelo menos um produto!")

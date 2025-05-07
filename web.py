import streamlit as st
import functions as fn  # import the functions file

# Inputs
col1, col2 = st.columns(2)
with col1:
    price = st.number_input("Price")
with col2:
    probability = st.number_input("Probability")

prob_based_on_price = fn.price_to_probability(price)
edge = fn.edge(prob_based_on_price, probability)


st.button("Calculate Edge", on_click=st.write(f"Edge: {edge}%"))

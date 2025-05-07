import streamlit as st
import functions as fn  # import the functions file

# Inputs
col1, col2 = st.columns(2)
with col1:
    price = st.number_input("Price")
with col2:
    probability = st.number_input("Probability")


edge = fn.edge(fn.price_to_probability(price), probability)


st.button("Calculate Edge", on_click=st.write(f"Edge: {edge}%"))

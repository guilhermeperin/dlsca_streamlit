import streamlit as st


def write():
    st.header('Optimization')

    st.subheader("Model Search")

    st.markdown("SideDL provides multiple options for deep learning model search. ")

    st.subheader("SideDL Methods")

    st.markdown('- Random search')
    st.markdown('- Grid search')
    st.markdown('- Bayesian optimization')
    st.markdown('- Reinforcement learning')

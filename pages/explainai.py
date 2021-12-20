import streamlit as st


def write():
    st.header('Explainable AI')

    st.markdown("The purpose of explainable AI module in SideDL software is to provide more information about evaluated deep learning models. "
                "There are several reasons for that:")
    st.markdown("- A manufacturer wants to understand more precisely how the vulnerabilities of their systems could be explored by deep "
                "learning models.\n"
                "- When analyzing the security of the product, the evaluator wants to understand if the designed deep learning model is "
                "appropriate for the problem. \n"
                "- Deep learning models can be incredible large. Normally, deep neural networks contain millions of trainable parameters. "
                "For that, the evaluator would need to be able to look inside this \'black box\' and see how decisions are made.")

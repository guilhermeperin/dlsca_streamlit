import streamlit as st

st.set_page_config(layout="wide")

import awesome_streamlit as ast
import awesome_streamlit.core.services as ast_core_services
import pages.introduction
import pages.theory
import pages.optimization
import pages.explainai
import pages.demonstration

ast_core_services.other.set_logging_format()

PAGES = {
    "SideDL": pages.introduction,
    "Theory": pages.theory,
    "Optimization": pages.optimization,
    "Explainable AI": pages.explainai,
    "Demonstration": pages.demonstration
}


def main():
    """Main function of the App"""
    st.sidebar.title("SideDL")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()

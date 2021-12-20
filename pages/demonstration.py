import streamlit as st
import numpy as np
import pandas as pd
from models.models import *


def write():
    st.header('SideDL Demonstration')

    st.subheader('1. Select the dataset')

    dataset_option = st.selectbox(
        'Select the dataset',
        ('ascad-variable.h5', 'ASCAD.h5'))

    dataset_dict = {
        "ascad-variable.h5": {
            "filename": "ascad-variable.npz",
            "key": "00112233445566778899AABBCCDDEEFF",
            "first_sample": 0,
            "number_of_samples": 1400,
            "number_of_profiling_traces": 200000,
            "number_of_attack_traces": 10000
        },
        "ASCAD.h5": {
            "filename": "ASCAD.npz",
            "key": "4DFBE0F27221FE10A78D4ADC8E490469",
            "first_sample": 0,
            "number_of_samples": 700,
            "number_of_profiling_traces": 50000,
            "number_of_attack_traces": 10000
        }
    }

    st.write('Dataset Name:', dataset_option)
    st.write('Number of traces for profiling:', dataset_dict[dataset_option]['number_of_profiling_traces'])
    st.write('Number of traces for attack:', dataset_dict[dataset_option]['number_of_attack_traces'])
    st.write('Key of attack set:', dataset_dict[dataset_option]['key'])
    st.write('Number of points of attacked interval:',
             dataset_dict[dataset_option]['number_of_samples'] - dataset_dict[dataset_option]['first_sample'])

    traces = np.load(f"{dataset_dict[dataset_option]['filename']}")["traces"]
    traces_to_plot = np.array([traces[0], traces[1], traces[2]]).T
    chart_data = pd.DataFrame(
        traces_to_plot,
        columns=['trace_0', 'trace_1', 'trace_2'])

    st.line_chart(chart_data)

    st.subheader('2. Model creation')

    model_option = st.radio(
        'Select the model creation type',
        ('Single Model', 'Model Search'))

    if model_option == "Single Model":
        col1, col2 = st.columns([5, 1])

        with col1:
            single_model_option = st.selectbox(
                'Select the neural network',
                ('MLP_1', 'MLP_2', 'CNN_1', 'CNN_2'))
            st.code(models_dict[single_model_option], language='python')

        with col2:
            st.number_input("Number of epochs", min_value=1)
            st.number_input("Batch-size", min_value=1)

        st.button("Start")

    if model_option == "Model Search":
        col1, col2, col3 = st.columns(3)
        with col1:
            model_search_option = st.selectbox(
                'Select the model search type',
                ('Random Search', 'Grid Search', 'Bayesian Optimization', 'Reinforcement Learning'))

        with col2:
            objective_metric = st.radio("Select the objective metric", ("Guessing Entropy", "Success Rate", "Loss", "Accuracy"))

        with col3:
            number_of_searches = st.number_input("Number of searches", min_value=1)

        st.button("Start")

    st.subheader('3. Select the explain method')
    col1, col2 = st.columns([1, 4])

    with col1:
        explain_method = st.selectbox(
            'Select the explainability method',
            ('Input Gradients', 'Layer Activity')
        )

    with col2:
        if explain_method == "Input Gradients":
            st.image("images/visualization.png")

        if explain_method == "Layer Activity":
            st.write("Activity Layer 1: 10%")
            st.write("Activity Layer 1: 18%")
            st.write("Activity Layer 1: 20%")

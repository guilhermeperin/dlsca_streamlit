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

    st.subheader('2. Select the neural network')

    dataset_option = st.selectbox(
        '',
        ('MLP_1', 'MLP_2', 'CNN_1', 'CNN_2'))

    st.code(models_dict[dataset_option], language='python')

    st.subheader('3. Select the model search')
    st.subheader('4. Select the explain method')

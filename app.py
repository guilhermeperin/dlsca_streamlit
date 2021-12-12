import streamlit as st
import pandas as pd
import numpy as np

st.title('State-of-the-art Deep Learning Models for Profiling Side-Channel Analyis')

st.markdown('Side channel analysis (SCA) are non-invasive attacks that explore unintended information leakage from security-aware '
            'devices.')
st.markdown('This page provides state-of-the-art deep learning models and results for open-source SCA datasets.')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)


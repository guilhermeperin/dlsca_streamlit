import streamlit as st
import pandas as pd
import numpy as np

st.title('State-of-the-art Deep Learning Models')

st.markdown('This page provides state-of-the-art deep learning models and results for open-source SCA datasets.')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)
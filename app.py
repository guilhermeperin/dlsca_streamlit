import streamlit as st
import pandas as pd
import numpy as np

st.title('Profiling Side-Channel Analyis with Deep Learning')

st.markdown('Side channel analysis (SCA) are non-invasive attacks that explore unintended information leakage from electronic '
            'devices. Electronic devices leak unintended information such as power consumption, electromagnetic emissions, time,'
            'acoustic, temperature and photonic emission.')
st.markdown('Cryptographic algorithms are mathematically secure. However, when deployed in microcontrolers, microprocessors, FPGAs or ASIC,'
            'just to mention a few, they become vulnerable to side-channel attacks due the unintended leakages. Countermeasures are usually'
            'implemented to mitigate side-channel attacks. In this article, we demonstrate how protected AES implementations are still'
            'vulnerable to a very strong class of side-channel attacks known as profiling SCA. The process follows exactly the supervised'
            'learning procedure and we show how deep neural network can be used as the learning algorithm.')
st.markdown('This page provides state-of-the-art deep learning models and results for open-source SCA datasets.')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)


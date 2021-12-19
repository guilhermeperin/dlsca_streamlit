import streamlit as st
import pandas as pd
import numpy as np
import urllib.request as url_request
import h5py

import aisy_sca

st.title('Profiling Side-Channel Analyis with Deep Learning')

st.markdown('Side channel analysis (SCA) are non-invasive attacks that explore unintended information leakage from electronic '
            'devices. Electronic devices leak unintended information such as power consumption, electromagnetic emissions, time, '
            'acoustic, temperature and photonic emission.')
st.markdown('Cryptographic algorithms are mathematically secure. However, when deployed in microcontrolers, microprocessors, FPGAs or ASIC,'
            'just to mention a few, they become vulnerable to side-channel attacks due the unintended leakages. Countermeasures are usually'
            'implemented to mitigate side-channel attacks. In this article, we demonstrate how protected AES implementations are still'
            'vulnerable to a very strong class of side-channel attacks known as profiling SCA. The process follows exactly the supervised'
            'learning procedure and we show how deep neural network can be used as the learning algorithm.')
st.header('Profiling SCA')
st.subheader('Preparing the dataset')

from pathlib import Path

my_file = Path('ascad-variable.h5')
if not my_file.is_file():
    url = 'https://static.data.gouv.fr/resources/ascad-atmega-8515-variable-key/20190903-083349/ascad-variable.h5'
    url_request.urlretrieve(url, 'ascad-variable.h5')

aisy = aisy_sca.Aisy()
aisy.set_resources_root_folder("resources/")
aisy.set_database_root_folder("resources/databases/")
aisy.set_datasets_root_folder("")
aisy.set_database_name("database_ascad.sqlite")

dataset_dict = {
    "ascad-variable.h5": {
        "filename": "ascad-variable.h5",
        "key": "00112233445566778899AABBCCDDEEFF",
        "first_sample": 0,
        "number_of_samples": 1400,
        "number_of_profiling_traces": 200000,
        "number_of_attack_traces": 1000
    }
}

aisy.set_dataset(dataset_dict["ascad-variable.h5"])
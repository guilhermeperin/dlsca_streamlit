from tensorflow.keras.optimizers import *
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

import aisy_sca
from aisy_database.db_select import *

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

# import urllib.request as url_request
# import h5py
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     ssl._create_default_https_context = _create_unverified_https_context

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

# from pathlib import Path
#
# my_file = Path('ascad-variable.h5')
# if not my_file.is_file():
#     url = 'https://static.data.gouv.fr/resources/ascad-atmega-8515-variable-key/20190903-083349/ascad-variable.h5'
#     url_request.urlretrieve(url, 'ascad-variable.h5')

aisy = aisy_sca.Aisy()
aisy.set_resources_root_folder("resources/")
aisy.set_database_root_folder("resources/databases/")
aisy.set_datasets_root_folder("")
aisy.set_database_name("database_ascad.sqlite")

dataset_option = st.selectbox(
    'Select the dataset',
    ('ascad-variable.h5', 'ASCAD.h5'))

dataset_dict = {
    "ascad-variable.h5": {
        "filename": "ascad-variable.h5",
        "key": "00112233445566778899AABBCCDDEEFF",
        "first_sample": 0,
        "number_of_samples": 1400,
        "number_of_profiling_traces": 200000,
        "number_of_attack_traces": 10000
    },
    "ASCAD.h5": {
        "filename": "ASCAD.h5",
        "key": "4DFBE0F27221FE10A78D4ADC8E490469",
        "first_sample": 0,
        "number_of_samples": 700,
        "number_of_profiling_traces": 50000,
        "number_of_attack_traces": 10000
    }
}

aisy.set_dataset(dataset_dict[dataset_option])

st.write('Dataset Name:', dataset_option)
st.write('Number of traces for profiling:', dataset_dict[dataset_option]['number_of_profiling_traces'])
st.write('Number of traces for attack:', dataset_dict[dataset_option]['number_of_attack_traces'])
st.write('Key of attack set:', dataset_dict[dataset_option]['key'])
st.write('Number of points of attacked interval:',
         dataset_dict[dataset_option]['number_of_samples'] - dataset_dict[dataset_option]['first_sample'])

#
#
# def mlp(classes, number_of_samples):
#     model = Sequential(name="basic_mlp")
#     model.add(Dense(200, activation='selu', input_shape=(number_of_samples,)))
#     model.add(Dense(200, activation='selu'))
#     model.add(Dense(200, activation='selu'))
#     model.add(Dense(200, activation='selu'))
#     model.add(Dense(classes, activation='softmax'))
#     model.summary()
#     optimizer = Adam(learning_rate=0.001)
#     model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
#     return model
#
#
# aisy.set_aes_leakage_model(leakage_model="HW", byte=2)
# aisy.set_batch_size(400)
# aisy.set_epochs(20)
# aisy.set_neural_network(mlp)
#
# aisy.run()
#
# db_select = DBSelect("resources/databases/database_ascad.sqlite")
# guessing_entropy = db_select.select_guessing_entropy_from_analysis(aisy.settings["analysis_id"])
# success_rates = db_select.select_success_rate_from_analysis(aisy.settings["analysis_id"])
#
# fig, ax = plt.subplots()
# for ge in guessing_entropy:
#     ax.plot(ge["values"], label="Attack set")
# st.pyplot(fig)

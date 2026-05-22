import streamlit as st
import pandas as pd
import numpy as np
import dummy_data

@st.cache_data
def get_data():
     return dummy_data.get_data1()
data = get_data()

# Form inputs
ngrams_raw = st.text_input("Comma-separated ngrams")
# Todo: dates, smoothing. No case sensitivity because this is the cn dashboard

ngrams = ngrams_raw.split(',')
ngrams = [ng for ng in ngrams if ng in data.keys()]

this_data = data[ngrams]
st.line_chart(this_data)

if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.write('This page has been run', st.session_state.counter, 'times');

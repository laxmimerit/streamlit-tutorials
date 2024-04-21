import streamlit as st
import pandas as pd
from transformers import pipeline

# Function to simulate an expensive computation
# @st.cache_data
def read_data():
    df = pd.read_csv("https://github.com/laxmimerit/All-CSV-ML-Data-Files-Download/raw/master/IMDB-Dataset.csv")
    return df.head()

# Function to store and retrieve data in session state
def update_session_state():
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    st.write("Counter:", st.session_state.counter)
    st.session_state.counter += 1

# Title
st.title("Working with Caching and Session State")

# Example of caching
st.button("Increment counter")
result = read_data()
st.write("Result of expensive computation:", result)

# update session state
update_session_state()

# Load NLP model from Hugging Face using caching. It will not reload model again
@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis")
    st.success("Loaded NLP model from Hugging Face!")
    return model

model = load_model()
st.success("Got model successfully!")
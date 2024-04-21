import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Data Objects Example")

# Display JSON data
st.subheader("JSON Data")

# Sample JSON data
json_data = {
    "name": "KGP Talkie",
    "age": 30,
    "city": "Mumbai"
}
st.json(json_data)

# Sample DataFrame
# Display DataFrame
st.subheader("DataFrame")

import pandas as pd
df = pd.read_csv("data/auto.csv")
st.dataframe(df.head())

# Display DataFrame as table
st.subheader("DataFrame as Table")
st.table(df.head())

# Sample code
st.subheader("Sample Code")

sample_code = '''
def greet(name):
    return "Hello, " + name + "!"
    
print(greet("KGP Talkie"))
'''
st.code(sample_code, language='python')

# Sample metric
st.subheader("Sample Metric")
st.metric("Accuracy", value=0.85, delta=+0.05)

# Sample data editor
st.subheader("Data Editor")
edited_data = st.data_editor(df.head())

st.write("Edited DataFrame:")
st.write(edited_data)

edited_data.to_csv("data/edited_data.csv", index=False)

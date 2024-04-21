import streamlit as st

# Title
st.title("Streamlit Text Input Examples")

# Text Input
name = st.text_input("Enter your name:", "")

# Text Area
feedback = st.text_area("Enter your feedback:", "")

# Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Date Input
date = st.date_input("Select a date:")

# Time Input
time = st.time_input("Select a time:")

# Color Picker
color = st.color_picker("Pick a color")

# Display inputs
st.write("Name:", name)
st.write("Feedback:", feedback)
st.write("Age:", age)
st.write("Date:", date)
st.write("Time:", time)
st.write("Color:", color)

# print color based on color values

# HTML
html_code = """
        <h1 style='color: {};'>This is a blue heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
""".format(color)
st.markdown(html_code, unsafe_allow_html=True)
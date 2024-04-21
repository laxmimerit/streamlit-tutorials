import streamlit as st
import time

# Title
st.title("Streamlit Status and Progress Indicator Examples")

# Empty
st.subheader("Empty Element")
empty_elem = st.empty()
empty_elem.text("This text will be replaced after 3 seconds...")
time.sleep(3)
empty_elem.text("Replaced!")

# Progress
st.subheader("Progress Bar")
progress_bar = st.progress(0)
status_text = st.empty()
for i in range(101):
    time.sleep(0.05)
    progress_bar.progress(i)
    status_text.text(f"Progress: {i}%")
status_text.text("Progress: Done!")

# Spinner
st.subheader("Spinner")
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Process completed!")

# Status
st.subheader("Status")
st.status("This is a status message")

# Toast
st.subheader("Toast")
st.warning("This is a warning message")
st.error("This is an error message")
st.success("This is a success message")
st.info("This is an info message")

# Snow
st.subheader("Snow")
st.snow()

# Balloons
st.subheader("Balloons")
st.balloons()

# Success, error, warning, info
st.subheader("Different Alert Types")
st.success("Success alert message")
st.error("Error alert message")
st.warning("Warning alert message")
st.info("Info alert message")

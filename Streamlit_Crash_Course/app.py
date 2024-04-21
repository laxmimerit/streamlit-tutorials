## Streamlit Application Basics
# Reference Book: https://packt.link/17kvV
# Code Repository: https://github.com/laxmimerit/streamlit-tutorials
# streamlit run app.py

import streamlit as st

st.title("Streamlit Basics: This is Title")

st.header("This is header")

st.subheader("This is subheader")

st.text("This is a simple text")

st.write("This is a write method")

st.header("Markdown and HTML")
st.markdown("`This is markdown`")

st.markdown("```import streamlit as st```")

st.markdown("[KGP Talkie](https://youtube.com/kgptalkie)")

st.markdown("#### this heading")

html_page = """
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

<h1 style="color:orange;">A Blue Heading</h1>

<p style="color:aqua;">A red paragraph.</p>

</body>
</html>
"""

st.markdown(html_page, unsafe_allow_html=True)

st.header("Buttons")

button = st.button("Submit This")
if button:
    st.success("Button is clicked!!!")

st.info("This is general info")

st.warning("This is warning")

st.error("This is an error")

st.markdown("---")

st.header("Audio, Video & Image")
from PIL import Image

#image
img = Image.open("kgptalkie.png")
st.image(image=img, width=100, caption="KGP Talkie Logo")

#video
video_file = open("sample-video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/X_Ts7VhHgEU?si=I19jtg3G9ooxR7je")

# audio
audio_file = open("sample.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes)

st.markdown("---")
st.header("Widgets")

#button
submit = st.button("Submit")
if submit:
    st.text("button is clicked")

#checkbox
if st.checkbox("Checkboc"):
    st.write("Checkbox is selected")

# Radio Button
radio_button = st.radio("Which Topic You Want to See", ["DL", "NLP", "Graph", "ML"])
st.write("You have selected: ", radio_button)

#selectbox
topics = st.selectbox("Your Interest", ["DL", "NLP", "Graph", "ML"])

#multi select
topics = st.multiselect("Your Interest", ["DL", "NLP", "Graph", "ML"])
st.write(topics)


# text input
name = st.text_input("Your Name", "Write something")
st.write("Your name is: ", name)


st.text_input("Your Email")
st.text_input("Your Mobile")
st.number_input("What is item price")
st.text_area("Write your feedback")


# slider
st.slider("Your happiness score", 10, 100, step=10)

if st.button("balloons"):
    st.balloons()

st.markdown("---")
st.header("Dataframes and Tables")

import pandas as pd
df = pd.read_csv("auto.csv")
st.dataframe(df.head())

# st.table(df.head())

# Plotting
st.area_chart(df[['mpg', "cylinders"]])
st.bar_chart(df[['mpg', 'cylinders']].head(20))
st.line_chart(df[['mpg', 'cylinders']].head(100))

# Seaborn and Matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[['mpg', "cylinders", "displacement", "horsepower"]].corr(), annot=True)
st.pyplot(fig)

st.markdown("---")
st.header("Date and Time")

import datetime, time
input_date = st.date_input("Select Your Date:")
st.write("you have selected date: ", input_date)

input_time = st.time_input("Select your time")
st.write("you have selected time", input_time)

st.markdown("---")
st.header("Extra")
data = {"name":"laxmi kant tiwari", "youtube": "https://kgptalkie.com"}
st.markdown("`{}`".format(data))
st.json(data)

st.markdown("""```import pandas as pd```""")

st.code("""
import pandas as pd
import numpy as np
""", language='python')

st.markdown("---")
st.header("Progress bar and Spinner")

import time

st.button("Run")
mybar = st.progress(0)
for value in range(100):
    time.sleep(0.01)
    mybar.progress(value)

with st.spinner("Please wait..."):
    time.sleep(10)

st.success("Done!!!")











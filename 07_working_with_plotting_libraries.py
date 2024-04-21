import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import seaborn as sns

# Title
st.title("Streamlit Plotting Libraries Examples")

df = pd.read_csv("./2 Tutorials/data/auto.csv")
st.dataframe(df.head())
columns = ["mpg","cylinders","displacement","horsepower","weight",
 "acceleration","year","origin","name"
]

# Area Chart
st.subheader("Area Chart")
st.area_chart(df[['mpg', 'cylinders']])

# Bar Chart
st.subheader("Bar Chart")
st.bar_chart(df[['mpg', 'cylinders']].head(20))

# Line Chart
st.subheader("Line Chart")
st.line_chart(df[['mpg', 'cylinders']].head(100))

# Seaborn Plot
st.subheader("Pyplot / Seaborn Plot")
fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[['mpg', "cylinders", "displacement", "horsepower"]].corr(), annot=True)
st.pyplot(fig)

# line plot
fig, ax = plt.subplots()
ax.plot(df['mpg'])
ax.set_xlabel('Index')
ax.set_ylabel('mpg')
ax.set_title('Line plot of mpg')
st.pyplot(fig)

#scatter plot
fig, ax = plt.subplots()
ax.scatter(df['mpg'], df['horsepower'])
ax.set_xlabel('mpg')
ax.set_ylabel('horsepower')
ax.set_title('Scatter plot of mpg and horsepower')
st.pyplot(fig)


# Plotly Chart
st.subheader("Plotly Chart")
fig = px.scatter(df, x='mpg', y='horsepower', color='origin', hover_name='name')
st.plotly_chart(fig)


# Map
st.subheader("Map")
temp = pd.read_csv("./2 Tutorials/data/weather_data.csv")
st.write(temp)
st.map(temp, latitude='lat', longitude='lon', size='temp')

# Altair Chart
st.subheader("Altair Chart")
columns = ["mpg","cylinders","displacement","horsepower","weight",
 "acceleration","year","origin","name"
]
alt_chart = alt.Chart(df).mark_circle().encode(
    x='mpg',
    y='horsepower',
    color='origin',
    tooltip=['name', 'year']
).interactive()
st.write(alt_chart)



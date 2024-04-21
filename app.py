import streamlit as st

st.title("Streamlit Playlist Series")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])
# page = st.sidebar.selectbox("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.write("Welcome to the homepage!")
    st.write("Here, you can explore various features of Streamlit.")

    # Expander
    with st.expander("Click to learn more about Streamlit"):
        st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.")

    # Popover
    with st.popover("Open popover"):
        st.markdown("Hello World 👋")
        name = st.text_input("What's your name?")

    st.write("Your name:", name)

elif page == "About":
    st.write("This is the About page.")
    st.write("Here, you can find information about Streamlit and its features.")

elif page == "Contact":
    st.write("Feel free to contact us!")
    st.write("You can reach out to us via email or social media.")

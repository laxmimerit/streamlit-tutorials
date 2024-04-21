import streamlit as st

# streamlit run app.py  --server.enableXsrfProtection false

# Title
st.title("Streamlit Media and File Examples")


# Image
st.subheader("Image")
image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
if image is not None:
    st.image(image, caption="Uploaded Image", width=100)

# use link to display image
st.image("https://kgptalkie.com/wp-content/uploads/2019/03/cropped-iPad-Pro-Copy@2x-1.png", caption="KGP Talkie Logo", width=100)

# Audio
st.subheader("Audio")
audio = st.file_uploader("Upload an audio file:", type=["mp3", "wav"])
if audio is not None:
    st.audio(audio, format="audio/mp3")

# Video
st.subheader("Video")
video = st.file_uploader("Upload a video file:", type=["mp4"])
st.write(video)
if video is not None:
    st.video(video, format="video/mp4")

# Use link to display video
st.video("https://www.youtube.com/watch?v=LjZTXKaPz2M", format="video/mp4")


# File Uploader
st.subheader("File Uploader")
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)
    st.write("type:", uploaded_file.type)
    st.write("\n")

# Download Button
st.subheader("Download Button")
download_data = "Hello, Streamlit!"
st.download_button(label="Download Example Text", data=download_data, file_name="example.txt")

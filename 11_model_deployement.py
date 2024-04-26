## pip install streamlit #use it on Python 3.8
from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import remove

from cartooner import cartoonize
import cv2

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    ":dog: Try uploading an image to watch the background magically removed."
)
st.sidebar.write("## Upload and download :gear:")

# Create the columns
col1, col2 = st.columns(2)

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Package the transform into a function
def remove_bg(upload, threshold):
    image = Image.open(upload)
    
    cartoon = cartoonize(image)
    st.image(cartoon)

    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image, alpha_matting_foreground_threshold=threshold)

    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("---")
    st.sidebar.download_button(
        "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
    )

    # download the cartoonized image
    img = Image.fromarray(cartoon)

    st.sidebar.download_button(
        "Download cartoonized image", convert_image(img), "cartoon.png", "image/png"
    )

# Create the file uploader
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

threshold = st.sidebar.slider("Background Threshold", 0, 255, value=50, step=5)

# Fix the image!
if my_upload is not None:
    remove_bg(upload=my_upload, threshold=threshold)
else:
    remove_bg("./images/cat.jpg", threshold=threshold)
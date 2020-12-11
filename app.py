from keras.models import load_model
import numpy as np 
import streamlit as st
from PIL import Image 
import io 
from classify import predict

# load model
model = load_model('MNIST/mnist_model')

# Streamlit
st.title("Simple MNIST example")

uploaded_img = st.file_uploader("Upload your image", type=["jpg", "png"])

if st.button("Predict!"):
    if uploaded_img is None:
        st.write("You did not upload a correct image")
    else:
        img = Image.open(uploaded_img)
        st.image(img, width=100)
        st.header("Predicted value on image: {}".format(predict(img, model)[0]))
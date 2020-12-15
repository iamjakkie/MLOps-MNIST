import streamlit as st
from PIL import Image 
from keras.models import load_model
from utils.aws_utils import get_model, test
from utils.classify import predict


def refresh_model():
    return load_model(get_model('mlops-mnist', 'MNIST/mnist_model.h5'))

def run_prediction():
    model = refresh_model()
    uploaded_img = st.file_uploader("Upload your image", type=["jpg", "png"])
    if st.button("Predict!", key='predict'):
        if uploaded_img is None:
            st.write("You did not upload a correct image")
        else:
            img = Image.open(uploaded_img)
            st.image(img)
            st.header("Predicted value on image: {}".format(predict(img, model)[0]))

def get_prev_predictions(login):
    pass            

def run_dashboard_page(login):
    if login:
        get_prev_predictions(login)
    run_prediction()
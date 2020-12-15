import streamlit as st
from PIL import Image 
from keras.models import load_model
from utils.aws_utils import get_model, get_user_history, get_image
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
            predictedValue = predict(img, model)[0])
            st.header("Predicted value on image: {}".format(predictedValue)
            st.text("Do you want to review inaccurate prediction?")
            if st.button("Yes", key='review'):
                actualValue = st.text_input("", type='number')
                if st.button("Save!", key='save'):
                    save(img, predictedValue, actualValue)

def save(uploaded_img, predictedValue:int, actualValue:int=None):
    """Saves image to s3 bucket and inserts prediction to the RDS db

    Args:
        uploaded_img ([type]): Image object to be saved
        predictedValue (int): predictedValue
        actualValue (int): actualValue
    """


def get_prev_predictions(login:str):
    """Generates previous predictions

    Args:
        login (str): currently logged user
    """
    prev_predictions = get_user_history(login)
    for prediction in prev_predictions:
        st.image(get_image(prediction[0]))
        st.header("Predicted value on image: {}".format(prediction[1]))

def run_dashboard_page(login):
    if login:
        get_prev_predictions(login)
    run_prediction()
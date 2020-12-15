# MLOps-MNIST

## App
The application uses model trained using proposed convolutional network (https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.1-introduction-to-convnets.ipynb) for handwritten digit recognition. Streamlit is the main component of the app. Notebook code has been transformed into python script which produces a keras model. Model has been uploaded manually to s3 bucket as a first version of algorithm used for predictions. Application uses boto3 library to interact with AWS – for model download, saving the predictions, getting historical data and logging user into the app. Basic application functionality is to allow user to use trained model for custom images.
![dashboard](/doc/dashboard.PNG)


![aws](/doc/aws.png)

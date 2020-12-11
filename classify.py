from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
import cv2


def predict(image, model): 
    img = image.copy()
    img = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))
    img = img.astype('float32')
    img = img.reshape(1,28,28,1)
    img /= 255

    # img = np.expand_dims(image, axis=0)
    #img = load_img(image, color_mode='grayscale', target_size=(28, 28, 1))
    # convert the image pixels to a numpy array
    # img = img_to_array(img)
    # reshape data for the model
    # img = image.reshape((1, 28, 28, 1))
    # predict
    return model.predict_classes(img) 
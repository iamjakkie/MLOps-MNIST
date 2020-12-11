from keras.models import load_model
import numpy as np
from keras.preprocessing import image

model = load_model('mnist_model')


# load img - keras
img = image.load_img(path='img/2.png', grayscale=True, target_size=(28,28,1))
img = image.img_to_array(img)
img = img.reshape((1, 28, 28, 1))



pred = model.predict_classes(img)
print(pred)
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import vgg19

class rps:

    def __init__(self,filename):
        self.filename =filename

    def prediction(self):
        model = load_model('model.h5')


        img_file = self.filename
        img = image.load_img(img_file,target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img,axis=0)

        result = model.predict(img)
        result = np.argmax(result,axis=1)
        key_res = int(result)

        values = {0: 'paper', 1: 'rock', 2: 'scissors'}
        pred = values[key_res]
        print(pred)


        return pred



import os.path
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
from io import BytesIO

model_load_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ckp1")
model = load_model(model_load_path)

def load_image(img_file):

#    data_file = BytesIO(img_data)

    img = Image.open(img_file)
    resized = img.resize((256, 256), resample=Image.LANCZOS)
    img_tensor = image.img_to_array(resized.convert("RGB")) # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor

def predict_image(img_data):
    img_tensor = load_image(img_data)

    return model.predict(img_tensor, verbose=1)

import os.path
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image

model_load_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ckp1")
model = load_model(model_load_path)

def load_image(img_file):
    img = Image.open(img_file)
    resized = img.resize((256, 256), resample=Image.LANCZOS)
    img_tensor = image.img_to_array(resized.convert("RGB")) # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels)

    return img_tensor

def predict_image(img_data):
    img_tensor = load_image(img_data)

    return model.predict(img_tensor, verbose=1)

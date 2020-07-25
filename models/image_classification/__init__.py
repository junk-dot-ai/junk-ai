import os.path
import base64
import io
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image

model_load_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ckp1")
model = load_model(model_load_path)

def load_image(img_file):
    img = Image.open(img_file)
    img_processed = img.resize((256, 256), resample=Image.LANCZOS).convert("RGB")

    with io.BytesIO() as img_buffer:
        img_processed.save(img_buffer, format="PNG")
        img_b64 = base64.b64encode(img_buffer.getvalue())

    img_tensor = image.img_to_array(img_processed)
    img_tensor = np.expand_dims(img_tensor, axis=0)

    return img_tensor, img_b64

def predict_image(img_data):
    img_tensor, img_b64 = load_image(img_data)
    return model.predict(img_tensor, verbose=1)[0], img_b64

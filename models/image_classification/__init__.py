import os.path
import base64
import io
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image


models_info = {
    "animal": ['Dog', 'Dolphin', 'Elephant', 'Lizard'],
    "object": ['Ball', 'Book', 'Bottle', 'Bowl', 'Chest of drawers', 'Coin', 'Flowerpot', 'Frying pan', 'Knife', 'Luggage and bags', 'Spoon']
}


def load_image(img_file):
    img = Image.open(img_file)
    img_processed = img.resize((256, 256), resample=Image.LANCZOS).convert("RGB")

    with io.BytesIO() as img_buffer:
        img_processed.save(img_buffer, format="PNG")
        img_b64 = base64.b64encode(img_buffer.getvalue())

    img_tensor = image.img_to_array(img_processed)
    img_tensor = np.expand_dims(img_tensor, axis=0)

    return img_tensor, img_b64


def predict_image(img_data, category):
    model_load_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{category}_model")
    model = load_model(model_load_path)

    img_tensor, img_b64 = load_image(img_data)

    classes = models_info[category]
    confidences = model.predict(img_tensor, verbose=1)[0]
    confidences = map(lambda n: round(n * 100, 2), confidences)

    class_to_confidence = dict(zip(classes, confidences)) # {"Dog": 96.29 ... }
    prediction = max(class_to_confidence, key=class_to_confidence.get)

    return prediction, class_to_confidence, img_b64

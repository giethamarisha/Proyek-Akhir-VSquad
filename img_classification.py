import keras
from PIL import Image, ImageOps
import numpy as np
from keras.engine.functional import Functional


def teachable_machine_classification(img, weight_file):
    # Load the model
    model = keras.models.load_model("Model PA.h5")

    data = np.ndarray(shape=(1, 100, 100, 3), dtype=np.float32)
    image = img

    size = (100, 100)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    return np.argmax(prediction)
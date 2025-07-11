#from keras.models import load_model  # TensorFlow is required for Keras to work

from tensorflow.keras.models import load_model
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st

import h5py

f = h5py.File("keras_model.h5", mode="r+")
model_config_string = f.attrs.get("model_config")

if model_config_string.find('"groups": 1,') != -1:
    model_config_string = model_config_string.replace('"groups": 1,', '')
f.attrs.modify('model_config', model_config_string)
f.flush()

model_config_string = f.attrs.get("model_config")

assert model_config_string.find('"groups": 1,') == -1

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(r'D:\Bhawna\course\AI-ML NIELIT\intel project\eAuto\keras_model.h5', compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1

st.title("Car Brand Identifier")
st.header('Upload an Image of Car')

uploaded_file= st.file_uploader('Choose the image....', type=['jpg','jpeg','png'])
if uploaded_file is not None:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image,caption='Uploaded Image....', use_container_width=True)

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    st.write(f'Class: {class_name[2:]}')
    st.write(f"Confidence Score:{confidence_score}")

#for run streamlit file on browser use treminal command streamlit run app.py
   

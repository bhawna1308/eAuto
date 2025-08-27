# app.py
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

# -----------------------------
# Load the model
# -----------------------------
model_path = os.path.join("model", "keras_model.h5")
model = load_model(model_path, compile=False)

# Load class labels
labels_path = os.path.join("model", "labels.txt")
with open(labels_path, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Car Brand Identifier")
st.header("Upload an Image of a Car")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize to 224x224
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convert to numpy array and normalize
    image_array = np.asarray(image).astype(np.float32)
    normalized_image_array = (image_array / 127.5) - 1

    # Add batch dimension
    data = np.expand_dims(normalized_image_array, axis=0)

    # Make prediction
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Display results
    st.write(f"Class: {class_name}")
    st.write(f"Confidence Score: {confidence_score:.2f}")

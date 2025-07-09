# 🚗 Car Brand Identifier using AI/ML (EAuto Project)

This is an AI-powered car logo detection project built using a deep learning model trained with [Teachable Machine by Google](https://teachablemachine.withgoogle.com/), deployed using **Streamlit**.

It allows users to upload a photo of a car, and the system identifies the **car brand** based on its logo using a trained image classification model.

---

## 📌 Features

- 🔍 Car logo detection using image classification
- 🧠 Model trained using Google's Teachable Machine
- 🌐 Deployed via Streamlit 
- 📷 Upload image and instantly get car brand prediction
- 🔒 No manual labeling — all auto-trained

---


## 🧠 Model Training

The model was trained using [Teachable Machine](https://teachablemachine.withgoogle.com/) and exported as:

- `keras_model.h5` – The trained model file.
- `labels.txt` – Label file containing class names.

> Model is stored in:  
> keras_model.h5
> labels.txt

---

## 📁 Folder Structure

```bash
eAuto/
│
├── app.py                  # Streamlit web app
├── keras_model.h5          # Trained model from Teachable Machine
├── labels.txt              # Class labels for the model
└── README.md               # You're reading this :)

#for run streamlit file on browser use treminal command streamlit run app.py

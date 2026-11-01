
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

st.title("Vegetable Image Classification")

classes = [
    "Bean",
    "Bitter Gourd",
    "Bottle Gourd",
    "Brinjal",
    "Broccoli",
    "Cabbage",
    "Capsicum",
    "Carrot",
    "Cauliflower",
    "Cucumber",
    "Papaya",
    "Potato",
    "Pumpkin",
    "Radish",
    "Tomato"
]

# Load model

@st.cache_resource
def load_model():
    try:
        return tf.keras.models.load_model("Vegetable_cnn.keras")
    except:
        return None

model = load_model()

if model:
    st.success("Model loaded")

    uploaded_image = st.file_uploader(
        "Upload vegetable image",
        type=['jpg', 'png', 'jpeg']
    )

    if uploaded_image:
        img = Image.open(uploaded_image).convert("RGB")
        st.image(img, width=300)

        if st.button("Predict"):
            img_resized = img.resize((224, 224))

            img_array = image.img_to_array(img_resized) / 255.0

            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)

            predicted_class = np.argmax(prediction[0])

            confidence = prediction[0][predicted_class]

            st.subheader(f"Prediction: {classes[predicted_class]}")

            st.write(f"Confidence: {confidence:.2%}")

else:
    st.error("Model not found!")

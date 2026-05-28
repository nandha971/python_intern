import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(page_title="CNN Classifier", page_icon="🖼️")
st.title("🖼️ Deep Learning Image Classifier")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('cnn_image_classifier.h5')

try:
    model = load_model()
    st.sidebar.success("Model loaded successfully!")
except Exception as e:
    st.sidebar.error("Could not load model file.")

CLASS_NAMES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # Preprocess
    img_resized = image.resize((32, 32))
    img_array = np.array(img_resized)[:, :, :3] / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    
    # Predict
    predictions = model.predict(img_batch)
    predicted_class_idx = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100
    
    st.success(f"### Prediction: **{CLASS_NAMES[predicted_class_idx]}**")
    st.info(f"### Confidence: **{confidence:.2f}%**")
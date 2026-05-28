import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# 1. Page Config and Setup
st.set_page_config(page_title="CNN Image Classifier", page_icon="🖼️", layout="centered")
st.title("🖼️ Deep Learning Image Classifier")
st.write("Upload an image, and our trained Convolutional Neural Network (CNN) will predict its class.")

# 2. Load the Trained Model
@st.cache_resource
def load_model():
    # Load the H5 model file saved during training
    model = tf.keras.models.load_model('cnn_image_classifier.h5')
    return model

try:
    model = load_model()
    st.sidebar.success("Model loaded successfully!")
except Exception as e:
    st.sidebar.error("Could not load model. Ensure 'cnn_image_classifier.h5' is in the same directory.")

# Class names mapping (Example matching the CIFAR-10 classes)
CLASS_NAMES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# 3. File Uploader Interface
uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    st.write("🔄 Processing and classifying...")
    
    # 4. Image Preprocessing to match model input constraints
    # Resize to (32, 32) as expected by our CNN model architecture
    img_resized = image.resize((32, 32))
    img_array = np.array(img_resized)
    
    # Ensure image has 3 color channels (RGB)
    if img_array.shape[-1] != 3:
        img_array = img_array[:, :, :3]
        
    # Scale pixel values and expand dimensions to create a batch of 1
    img_array = img_array / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    
    # 5. Model Inference Execution
    predictions = model.predict(img_batch)
    score = tf.nn.softmax(predictions[0])
    predicted_class_idx = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100
    
    # 6. Display Output Predictions
    st.success(f"### Prediction: **{CLASS_NAMES[predicted_class_idx]}**")
    st.info(f"### Confidence Score: **{confidence:.2f}%**")
# app.py
from flask import Flask, render_template, request, redirect, url_for
import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model_folder = 'models'

# Load your machine learning model here
model_path_h5 = os.path.join(model_folder, 'model2.h5')
model_path_json = os.path.join(model_folder, 'model.json')
model_path_tflite = os.path.join(model_folder, 'model.tflite')

# Load model
if os.path.exists(model_path_h5):
    model = tf.keras.models.load_model(model_path_h5)
elif os.path.exists(model_path_json):
    with open(model_path_json, 'r') as json_file:
        model_json = json_file.read()
    model = tf.keras.models.model_from_json(model_json)
elif os.path.exists(model_path_tflite):
    interpreter = tf.lite.Interpreter(model_path=model_path_tflite)
    interpreter.allocate_tensors()
    model = interpreter
else:
    print("Model file not found.")

# Function to preprocess the image before prediction
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

# Function to perform prediction using the loaded model
def predict(image_path):
    # Preprocess the image
    processed_image = preprocess_image(image_path)

    # Make prediction
    if model is not None:
        predictions = model.predict(processed_image)
        predicted_class_index = np.argmax(predictions)
        
        # Mapping index to class label
        class_labels = ["paper", "rock", "scissors"]
        predicted_label = class_labels[predicted_class_index]
        
        accuracy = f"{predictions[0][predicted_class_index] * 100:.2f}%"
        return predicted_label, accuracy
    else:
        return "Model not loaded", "N/A"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle image upload
        if 'image' not in request.files:
            return redirect(request.url)
        
        file = request.files['image']

        if file.filename == '':
            return redirect(request.url)

        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            # Perform prediction
            start_time = time.time()
            predicted_label, accuracy = predict(image_path)
            prediction_time = round(time.time() - start_time, 2)

            # Render result page
            return render_template('result.html', 
                                   image_path=image_path, 
                                   predicted_label=predicted_label, 
                                   accuracy=accuracy, 
                                   prediction_time=prediction_time)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

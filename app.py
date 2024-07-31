import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import tensorflow as tf

# Load pre-trained MNIST model
model = tf.keras.models.load_model('mnist_model.h5')

# Flask application setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to MNIST image size
    image = np.array(image)  # Convert to numpy array
    image = image / 255.0  # Normalize
    image = image.reshape(1, 28, 28, 1)  # Reshape for the model
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Load and preprocess the image
            image = Image.open(filepath)
            preprocessed_image = preprocess_image(image)
            
            # Predict digit
            predictions = model.predict(preprocessed_image)
            digit = np.argmax(predictions[0])
        except Exception as e:
            digit = f"Error: {e}"

        return render_template('results.html', filename=filename, digit=digit)
    
    return redirect(request.url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

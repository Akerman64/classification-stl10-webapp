import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
MODEL_PATH = 'mobilenet_stl10_transfer_learning.keras'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static/uploads'

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# STL-10 Classes
CLASSES = [
    'airplane', 'bird', 'car', 'cat', 'deer', 
    'dog', 'horse', 'monkey', 'ship', 'truck'
]

# Load Model
print("Loading model...")
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(img_path):
    # Load image with target size 96x96 (STL-10 standard)
    img = image.load_img(img_path, target_size=(96, 96))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # Preprocess input (normalization for MobileNet)
    img_array = preprocess_input(img_array)
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_results = None
    image_url = None
    
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_url = url_for('static', filename='uploads/' + filename)
            
            if model:
                try:
                    # Preprocess and Predict
                    processed_image = prepare_image(filepath)
                    predictions = model.predict(processed_image)
                    
                    # Get Top 3
                    top_3_indices = predictions[0].argsort()[-3:][::-1]
                    top_3_probs = predictions[0][top_3_indices]
                    
                    prediction_results = []
                    for i in range(3):
                        prediction_results.append({
                            'class': CLASSES[top_3_indices[i]],
                            'probability': round(float(top_3_probs[i]) * 100, 2)
                        })
                except Exception as e:
                    print(f"Prediction error: {e}")
                    prediction_results = [{'class': 'Error', 'probability': 0}]
            
    return render_template('index.html', predictions=prediction_results, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

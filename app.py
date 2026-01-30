import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from werkzeug.utils import secure_filename
import logging
from pathlib import Path
import time
import threading
import shutil
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "logs"
LOG_DIR = Path(LOG_PATH)
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("animal_classification")

logger.info("Demarrage de l'application")

# --- Détection GPU/CPU ---
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logger.info(f"GPU détecté : {len(gpus)} GPU(s) disponibles")
    except RuntimeError as e:
        logger.warning(f"Erreur configuration GPU : {e}")
else:
    logger.info("Aucun GPU détecté, utilisation du CPU")

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
logger.info("Chargement du model...")
try:
    model = load_model(MODEL_PATH)
    logger.info("Model chargé avec succès.")
except Exception as e:
    logger.warning(f"Erreur de chargement du model: {e}")
    model = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(96, 96))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_results = None
    image_url = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_url = url_for('static', filename='uploads/' + filename)
            
            if model:
                try:
                    model.trainable = False
                    processed_image = prepare_image(filepath)
                    predictions = model.predict(processed_image)

                    top_3_indices = predictions[0].argsort()[-3:][::-1]
                    top_3_probs = predictions[0][top_3_indices]
                    
                    prediction_results = []
                    for i in range(3):
                        prediction_results.append({
                            'class': CLASSES[top_3_indices[i]],
                            'probability': round(float(top_3_probs[i]) * 100, 2)
                        })
                except Exception as e:
                    logger.warning(f"Prediction error: {e}")
                    prediction_results = [{'class': 'Error', 'probability': 0}]
            
    return render_template('index.html', predictions=prediction_results, image_url=image_url)

def clean_upload_folder(clean_interval=60*10):
    while True:
        try:
            if os.path.exists(UPLOAD_FOLDER):
                for filename in os.listdir(UPLOAD_FOLDER):
                    file_path = os.path.join(UPLOAD_FOLDER, filename)
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                logger.info("[CLEANER] Upload folder cleaned")
        except Exception as e:
            logger.warning(f"[CLEANER] Error: {e}")
        time.sleep(clean_interval)

def start_upload_cleaner_thread():
    thread = threading.Thread(
        target=clean_upload_folder,
        daemon=True
    )
    thread.start()

if __name__ == '__main__':
    start_upload_cleaner_thread()
    app.run(host="0.0.0.0", debug=False, port=5000)

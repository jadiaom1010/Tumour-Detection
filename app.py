import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
from chatbot_api import get_chatbot_response


app = Flask(__name__)

model = load_model('BrainTumor10EpochsCategorical.h5')
print('Model loaded. Check http://127.0.0.1:5000/')


def get_className(classNo):
    if classNo == 0:
        return "No Brain Tumor"
    elif classNo == 1:
        return "Yes Brain Tumor"


def getResult(img):
    image = cv2.imread(img)  # Read image file
    image = Image.fromarray(image, 'RGB')  # Convert to RGB
    image = image.resize((64, 64))  # Resize image to 64x64 pixels
    image = np.array(image)  # Convert image to numpy array
    input_img = np.expand_dims(image, axis=0)  # Expand dimensions for model input

    # Use model.predict() and np.argmax to get the predicted class
    result = np.argmax(model.predict(input_img), axis=-1)
    
    return result


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        value = getResult(file_path)
        result = get_className(value)
        return result
    return None

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question')
    
    # Use the chatbot API to get a response
    bot_response = get_chatbot_response(question)
    return jsonify({'answer': bot_response})



if __name__ == '__main__':
    app.run(debug=True)

# -*- coding: utf-8 -*-

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='model_mnist_cnn.h5'

# Load your trained model
model = load_model(MODEL_PATH)




def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(28,28), grayscale=True, color_mode = "grayscale") 

    # Preprocessing the image
    x = image.img_to_array(img)

    ## Scaling
    x = x.reshape(1,784)
    x = x/255
   

   

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds="This number is 0"
    elif preds==1:
        preds="This number is 1"
    elif preds==2:
        preds="This number is 2"
    elif preds==3:
        preds="This number is 3"
    elif preds==4:
        preds="This number is 4"
    elif preds==5:
        preds="This number is 5"
    elif preds==6:
        preds="This number is 6"
    elif preds==7:
        preds="This number is 7"
    elif preds==8:
        preds="This number is 8"
    else:
        preds="This number is 9"
    
    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)

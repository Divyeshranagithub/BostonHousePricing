import pickle
from flask import Flask, request, app, jsonify, render_template, url_for  
import numpy as np
import pandas as pd

app = Flask(__name__)
## Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
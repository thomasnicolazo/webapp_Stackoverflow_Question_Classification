# -*- coding: utf-8 -*-
import sys
import numpy as np
import pickle
import joblib
from function import *
from flask import Flask, request, render_template

# Load ML model
model = joblib.load(open('bestModelUSELogistic.pkl', 'rb')) 
# Load reduced Tags 
labels= joblib.load(open('labels.pkl','rb'))
# load dictionary reduced Tags to Tags
dicPassage = joblib.load(open('dicoPassageTagToList.pickle','rb'))
# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
	# Put all form entries values in a list 
    features = str([i for i in request.form.values()])
    print(features,file=sys.stderr)
    text_to_predict = textProcessing(features)
    # model prediction
    prediction = model.predict(text_to_predict)
    # conver numeric to tag
    reducedTags = numericToReducedTags(prediction[0],labels)# prediction list in list
    #Reduced tags to stackoverflow tags
    StackTags = ReducedTagsToStackTags(reducedTags,dicPassage)
    ###output = prediction
    # Check the output values and retrive the result with html tag based on the value
    return render_template('index.html',result = StackTags)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port=5000)
#Run the application

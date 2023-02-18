from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        myage = request.form['age']
        mysalary = request.form['salary']
        mystatus = request.form['status']
        if str(myage) =='' or str(mygender) =='' or str(mystatus) ==''
            return render_template('index.html', href2='Please insert your age, salary and marital status.')
        else:
            model = load('app/movie-recommender.joblib')
            np_arr = np.array([myage, mysalary, mystatus])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            #return predictions_to_str
            return render_template('index.html', href2='The suitable movie for you (age:'+str(myage)+' ,salary:'+str(mysalary)+', marital status:'+str(mystatus)+') is:'+predictions_to_str)
        


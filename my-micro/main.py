from flask import Flask, render_template, request
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import  session
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath,abspath
import requests
import pickle
import numpy as np
import json
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
model = pickle.load(open('finalized_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['GET', 'POST'])
def predict():
    output=0
    if request.method == 'POST':
        BHK=int(request.form['BHK'])
        Size=int(request.form['Size'])
        City=str(request.form['City'])
        Area_Locality=str(request.form['Area_Locality'])
        Bathroom=int(request.form['Bathroom'])
        Floor_no=int(request.form['Floor_no'])
        Total_floor=int(request.form['Total_floor'])
        City_Delhi=0
        City_Hyderabad=0
        City_Kolkata=0
        City_Mumbai=0
        City_Chennai=0
        if City=='Chennai':
            City_Chennai=1
        elif City=='Delhi':
            City_Delhi=1
        elif City=='Hyderabad':
            City_Hyderabad=1
        elif City=='Kolkata':
            City_Kolkata=1
        else:
            City_Mumbai=1
        UPLOAD_FOLDER='static/'    
        map = json.load( open(os.path.join(basedir,UPLOAD_FOLDER,"area_loc.json" )) )
        Area_Loc=map[Area_Locality]
        input=[BHK,Size, Area_Loc,Bathroom,Floor_no,Total_floor,
        City_Chennai,City_Delhi,City_Hyderabad, City_Kolkata,
        City_Mumbai]
        output=int(np.exp(model.predict([input])))
        return render_template("rent_val.html",prediction=output)
    return render_template("predict.html")

if __name__=="__main__":
    app.run(debug=True)

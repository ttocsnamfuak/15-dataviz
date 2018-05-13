# import necessary libraries
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
   
#################################################
# Database Setup
#################################################
import pandas as pd
import sqlite3

conn = sqlite3.connect("belly_button_biodiversity.sqlite")

#Create Dataframes
otu_df = pd.read_sql_query("select * from otu;", conn)

samples_df = pd.read_sql_query("select * from samples;", conn)

sampMeta_df = pd.read_sql_query("select * from samples_metadata", conn)





#################################################
# Create routes
#################################################
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    
    samples_list = samples_df.columns
    x = len(samples_list)
    cleanList = []

    for i in range(1,x):
        cleanList.append(samples_list[i])

    return jsonify(cleanList)

@app.route("/otu")
def otu():
    # results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()
    # results = ["Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
    #     "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
    #     "Bacteria",
    #     "Bacteria",
    #     "Bacteria"]
    otuDesc =[]
    for index in range(len(otu_df["otu_id"])):
        otuDesc.append(otu_df.iloc[index,1])
    
    return jsonify(otuDesc)

@app.route("/metadata/<sample>")
def metadata(sample):
    # results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()
    print(sample)
    
    # sample = "BB_940" 
    data = sample.split("_")
    idBB = data[1] 
    print(sampMeta_df.loc[sampMeta_df['SAMPLEID'] == int(idBB)])  
    idResult_df = sampMeta_df.loc[sampMeta_df['SAMPLEID'] == int(idBB)]
    results = [{
        'AGE': int(idResult_df.iloc[0]['AGE']),
        "BBTYPE": idResult_df.iloc[0]['BBTYPE'],
        "ETHNICITY": idResult_df.iloc[0]['ETHNICITY'],
        "GENDER": idResult_df.iloc[0]['GENDER'],
        "LOCATION": idResult_df.iloc[0]['LOCATION'],
        "SAMPLEID": int(idResult_df.iloc[0]['SAMPLEID'])
    }]

    return jsonify(results)

@app.route("/wfreq/<sample>")
def wfreq(sample):
    # results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()
    print(sample)
    # results = [24]
    
    
    data = sample.split("_")
    wfreqID = data[1] 
    
    print(wfreqID)
    print(sampMeta_df.loc[sampMeta_df['SAMPLEID'] == int(wfreqID)]) 

    wfreqResult_df = sampMeta_df.loc[sampMeta_df['SAMPLEID'] == int(wfreqID)]
    
    print(wfreqResult_df)

    wfreqNbr = wfreqResult_df.iloc[0]['WFREQ']
    
    return jsonify(wfreqNbr)

@app.route('/samples/<sample>')
def sample(sample):
    # results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()
    print(sample)
    descSamples_df = samples_df.sort_values('otu_id', ascending=False)

    clList = descSamples_df.columns
    
    print(clList)
    print(len(clList))
    position = 0
    for index in range(len(clList)):
        if (clList[index] == sample):
            position = index
            break
        position += 1
    
    sampleList =[]
    otuList =[]
    for index in range(len(descSamples_df["otu_id"])):
        if (descSamples_df.iloc[index,position] != 0):
            sampleList.append(int(descSamples_df.iloc[index,position]))
            otuList.append(int(descSamples_df.iloc[index,0]))
        
    sampleResults = [{
            'otu_ids': otuList,
            'sample_values': sampleList
        }] 


    return jsonify(sampleResults)


# @app.route("/api/names")
# def pets():
#     results = db.session.query(Pet.name).all()
#     print(results)
#     all_pets = list(np.ravel(results))
#     return jsonify(all_pets)

if __name__ == "__main__":
    app.run()

# @app.route("/otu")
# def home():
#     return render_template("index.html")

# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         pet_type = request.form["petType"]
#         age = request.form["petAge"]

#         pet = Pet(name=name, type=pet_type, age=age)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("http://localhost:5000/", code=302)

#     return render_template("form.html")

# @app.route("/api/pals")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:18:26 2018

@author: scott
"""

import pandas as pd
import sqlite3

conn = sqlite3.connect("belly_button_biodiversity.sqlite")

#Create Dataframes
otu_df = pd.read_sql_query("select * from otu;", conn)

samples_df = pd.read_sql_query("select * from samples;", conn)

sampMeta_df = pd.read_sql_query("select * from samples_metadata", conn)

#Create list arrays for routes json
#Names
samples_list = samples_df.columns
x = len(samples_list)
cleanList = []

for i in range(1,x):
    cleanList.append(samples_list[i])
    
#OTU Descriptions
otuDesc =[]
for index in range(len(otu_df["otu_id"])):
    otuDesc.append(otu_df.iloc[index,1])

#/metadata/<sample>
sample = "BB_940" 
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
        "SAMPLEID": idResult_df.iloc[0]['SAMPLEID']
    }]

#/wfreq/<sample>
sample = "BB_940"
data = sample.split("_")
wfreqID = data[1] 

wfreqResult_df = sampMeta_df.loc[sampMeta_df['SAMPLEID'] == int(idBB)]
wfreqNbr = int(wfreqResult_df.iloc[0]['WFREQ'])
    
#//samples/<sample>
sample = "BB_944"

descSamples_df = samples_df.sort_values('otu_id', ascending=False)

clList = descSamples_df.columns
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

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

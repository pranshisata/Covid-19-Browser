#!/usr/bin/env python
# coding: utf-8

import json
import os
import numpy as np
import pandas as pd

# Fetching all the json files from Kaggle which contains research papers

path_to_json = '/Users/pranshisata/Desktop/Pranshi/Sem 4/Internship:Project/archive/document_parses/pdf_json'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
json_files

len(json_files)

# Exploratory Data Analysis (EDA)
# EDA: Exploratory Data Analysis is an approach to analyzing data sets to summarize their main characteristics, often with visual methods.

# Defining pandas DataFrame for the columns I want from the JSON file
jsonData = pd.DataFrame(columns=['paper_id', 'abstract', 'body_text'])

idabstract = []

# We will use enumerate() because we want json and an index number

for index, js in enumerate(json_files[:3000]):     # Using 3000 files only to reduce memory load and resources
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

# Now, we will create a layout of the json files

        paper_id = json_text['paper_id']
        
        abstract=''
        for entry in json_text['abstract']:
            abstract += entry['text']
        idabstract.append({paper_id:abstract})
        
        body_text=""
        for entry in json_text['body_text']:
            body_text += entry['text']
                
# Pushing a list of data into pandas DataFrame at rows given by 'index'
        jsonData.loc[index] = [paper_id, abstract, body_text]

print(jsonData)

# Display DataFrame
jsonData


# Remove Null Values
# Remove null values because they don't have any values and they might cause trouble while the model is predicting.

df = jsonData
for col in df.columns:
    print(col, df[col].isnull().sum())

# Combining the JSON files

def parser():

    dictionary = dict()
    dictionary["data"] = list()
    jsonFiles = [path_to_json + "/" + pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    for index, js in enumerate(json_files[:3000]): # Using 3000 files only to reduce memory load and resources
        with open(os.path.join(path_to_json, js)) as jsonFile:
            data = json.load(jsonFile)
            struct = dict()
            authors = list()
            affiliations = set()

            for auth in data["metadata"]["authors"]:
                authors.append(" ".join([auth["first"], auth["last"]]))
                #affiliations.add(auth["affiliation"]["institution"])

            struct["Title"] = data["metadata"]["title"]
            struct["ID"] = data["paper_id"]
            struct["Authors"] = "; ".join(authors)
            #struct["Affiliations"] = "; ".join(affiliations)
            dictionary["data"].append(struct)

    print (dictionary)

    with open("dataTable.txt", "w") as outputJsonFile:
        json.dump(dictionary, outputJsonFile)

parser()





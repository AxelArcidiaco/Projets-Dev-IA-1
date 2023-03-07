# librairies
from flask import render_template
from joblib import load
import pandas as pd
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# chargement du modèle
model = load('ext_tree.joblib')

# création d'une nouvelle instance API
app = FastAPI(version= "0.1.0",
              title='ComparCars', 
              description='API de comparaison de prix de véhicules d\'occasion',
              docs_url= "/api",)

class request_body(BaseModel):
    year : int
    transmission : str
    power: int
    location : str
    fuel_type : str 
    owner_type : str
    kilometers_driven : int
    mileage : int
    seats : int


@app.post('/api')
def predict(data : request_body):

# Prédiction sur une donnée
    new_data = pd.DataFrame(columns=[ 'year',
    'transmission',
    'power',
    'location',
    'fuel_type', 
    'owner_type',
    'kilometers_driven',
    'mileage',
    'seats'], data=[[
    data.year,
    data.transmission,
    data.power,
    data.location,
    data.fuel_type,
    data.owner_type,
    data.kilometers_driven,
    data.mileage,
    data.seats
    ]])
    
    prix = model.predict(new_data)

    return { 'Prix estimé du véhicule ': prix[0] }


# route pour l'accueil
@app.get('/')
def home():
    return 'API de ComparCars'



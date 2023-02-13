#Importations des bibliothèques
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Configuration de la base de données qui collecte des données d'utilisateurs
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

#Route de connexion de la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

#Route de connexion pour le formulaire d'inscription qui récupère le username et password dans la base de données
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('register.html')

#Route de connexion d'utilisateur SI il est dans la base de données SINON - message d'erreur 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return redirect(url_for('scan'))
        
        return 'Incorrect username or password. Please try again.'
    return render_template('login.html')

#Route de redirection vers la page formulaire SCAN
@app.route("/scan")
def scan():
    return render_template("scan.html")


# Chargement du modèle IA en .pkl - liason avec le formulaire SCAN
model = pickle.load(open("Classification\\Projet Classification\\projetFraude\\Arbre_Decision.pkl", "rb"))

@app.route("/scan", methods=["POST"])
def scanForm():
    temps = request.form["input1"]
    transaction = request.form["input2"]
    montant = request.form["input3"]
    data_predict = pd.DataFrame(columns=["step","type", "amount"],data=[[temps,transaction,montant]])

# Utiliser les données collectées pour faire des prédictions avec le modèle
    prediction = model.predict(data_predict)

    if prediction == 1:
        message = "Fraude"
        css_class = "fraude"
    else:
        message = "Transaction approuvée"
        css_class = "non-fraude"

    return render_template("result.html", message=message, css_class=css_class) 




# @app.route("/result")
# def result():
#     return render_template("result.html")

#Lancement d'application
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


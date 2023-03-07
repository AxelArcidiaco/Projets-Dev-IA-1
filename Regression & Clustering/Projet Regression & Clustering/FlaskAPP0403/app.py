from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from models import User, db, Contact, ContactForm
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import secrets
import pickle
import joblib


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# génération de la clé sécrète
app.secret_key = secrets.token_hex(16)

db.init_app(app)

# Initialise le gestionnaire de connexion
login_manager = LoginManager()
login_manager.init_app(app)


app.app_context().push()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email déjà utilisé', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        # Créer un nouvel utilisateur avec les données du formulaire
        new_user = User(username=username, email=email, password_hash=hashed_password)
        # Ajouter le nouvel utilisateur à la base de données
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')


@login_manager.user_loader
def load_user(user_id):
    # Charge l'utilisateur à partir de la base de données
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Vérifie si l'utilisateur est déjà connecté
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Récupère les informations de connexion depuis le formulaire
        email = request.form['email']
        password = request.form['password']

        # Recherche l'utilisateur dans la base de données
        user = User.query.filter_by(email=email).first()

        # Vérifie si le mot de passe est correct
        if not  user or not check_password_hash(user.password_hash, password):
            flash('Email ou mot de passe incorrect', 'danger')
            return redirect(url_for('login'))
        else:
            # Connecte l'utilisateur
            login_user(user)
            # Redirige l'utilisateur vers la page d'accueil
            return redirect(url_for('index'))
    # Affiche le formulaire de connexion
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Déconnecte l'utilisateur
    logout_user()

    # Redirige l'utilisateur vers la page d'accueil
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Créer un nouveau contact avec les données du formulaire
        new_contact = Contact(name=name, email=email, message=message)
        # Ajouter le nouveau contact à la base de données
        db.session.add(new_contact)
        db.session.commit()
        return "Message envoyé"
    return render_template('contact.html', form=form)


########## ROUTES DES PREDICTIONS  ############################

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Import des modèles
mdl1 = 'Regression & Clustering\\Projet Regression & Clustering\\FlaskAPP0403\\bagging_regressor_restraint_3.pkl'
mdl2 = 'Regression & Clustering\\Projet Regression & Clustering\\FlaskAPP0403\\ExtraTreesRegressor_full-10.pkl'
mdl3 = 'Regression & Clustering\\Projet Regression & Clustering\\FlaskAPP0403\\extr_tree.joblib'

# route de control_panel pour choisir les modèles
modeles = [mdl1, mdl2, mdl3]

@app.route('/control_panel')
def control():
    return render_template('control_panel.html', 
                           modele01=modeles[0], 
                           modele02=modeles[1], 
                           modele03=modeles[2])


# On charge le modèle
with open(mdl1, 'rb') as model:
    model = pickle.load(model)

class request_body(BaseModel):
    year : int
    transmission : str
    power : int
   

# modele 01 : trois features
@app.route('/predict01', methods = ['POST', 'GET'])
def predict01():
        
    # la boucle qui affiche les années
    year_list = []
    for i in range(1998, 2024):
        year_list.append(i)
        
    return render_template('predict_01.html', year_list=year_list)
        
    

# modele 02 : dix features
@app.route('/predict02')
def predict02():

    # la boucle qui affiche les années
    year_list = []
    for i in range(1998, 2024):
        year_list.append(i)
        

    return render_template('predict_02.html', year_list=year_list )

# modele 03 : 9 features
@app.route('/predict03')
def predict03():

    # la boucle qui affiche les années
    year_list = []
    for i in range(1998, 2024):
        year_list.append(i)


    return render_template('predict_03.html', year_list=year_list)

# prediction des modèles
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        year = request.form.get("year")
        transmission = request.form.get("transmission")
        power = request.form.get("power")

        # Prédiction sur une donnée
        new_data = [[
            year,
            transmission,
            power
        ]]
    
        prix = model.predict(new_data)
    return render_template('prediction.html', prix = round(prix[0], 2))

###########################################################################


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
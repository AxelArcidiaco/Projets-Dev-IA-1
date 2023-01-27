import os
from flask import Flask, render_template, request, redirect, url_for, abort, session, flash
import pandas as pd 
import random
import collections
import copy

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.no_of_chance = 4

file_csv = "./big_data_pokemon_quiz.csv"

# Avoir les infos sur les pokemons et les technologies big data

db_pokemon = pd.read_csv("./pokemons_database.csv")
df_big_data = pd.read_csv("./big_data_database.csv")

dict_pokemons = db_pokemon[['name','desc']].set_index('name').to_dict()['desc']
dict_big_data = df_big_data[['name', 'desc']].set_index('name').to_dict()['desc']

dict_global  = collections.defaultdict()

for pokemon in dict_pokemons.keys() :  
    dict_global[pokemon] = "Pokemon"

for techno in dict_big_data.keys() :  
    dict_global[techno] = "Big Data"


######### On définit le nombre de questions du questionnaire

longueur_questionnaire = 10

####### On définit les éléments du questitonnaire

liste_choice = ['Flaaffy',
 'Myria',
 'Featurefu',
 'Sceptile',
 'Akiban',
 'Mime-jr',
 'Bookkeeper',
 'Hparser',
 'Chesnaught',
 'Velox']
    

questions = {}    
for x in range(1, longueur_questionnaire + 1) : 
    item = liste_choice[x-1]
    questions[str(x)] = {"question" : "{} : Pokemon or Big Data ?".format(item), "options" :["Pokemon", "Big Data"], "answer" : dict_global[item]}


# Ici on vérifie si le fichier qui conserve les réponses existe ou pas

if not os.path.isfile(file_csv):
    df = pd.DataFrame({'user' : [], 'score' : []})
    #for question in questions.keys() :
    for x in range(1, longueur_questionnaire+ 1 ) : 
        df[str(x)] = []
    df.to_csv(file_csv, index = False)


#### La page d'accueil #####
@app.route('/')
def home():
    return render_template('index.html')


#### s'inscrire #####

liste = [None] * (longueur_questionnaire + 2)

@app.route('/signup', methods=['POST'])
def signup():
    session['username'] = request.form['username']
    liste[0] = request.form['username']
    #df.iloc[-1]["user"] = request.form['username']
    return redirect(url_for('bienvenue'))


#### page de bienvenue une fois l'inscription faite #####

@app.route('/bienvenue')
def bienvenue():
    if not 'username' in session:
        return abort(403)        
    return render_template('message.html', username=session['username'])
    
#### le questionnaire #####
    
@app.route('/questionnaire/', methods=['GET', 'POST'])
def questionnaire():
    print(request.method)
    print(session.get("question", "a"))

    if request.method == "POST":
        if "question" in session:
            entered_answer = request.form.get('answer', '')
            liste[int(session["question"])] = entered_answer
            print(questions.get(session["question"],False))
            if questions.get(session["question"],False):
                if entered_answer != questions[session["question"]]["answer"]:
                    mark = 0
                else:
                    mark = 4
                session["mark"] += mark
                session["question"] = str(int(session["question"])+1)
        else:
            print("question missing")
  
    if "question" not in session:
        session["question"] = "1"
        session["mark"] = 0
    elif session["question"] not in questions: #cas où il n'y a plus de question
        df = pd.read_csv(file_csv)
        df.reset_index(drop = True,inplace = True)          
        liste[longueur_questionnaire+1]  =  session["mark"]
        df.loc[-1]  = liste
        df.to_csv(file_csv, index = False)       
        return render_template("score.html", score = session["mark"])
    return render_template("quiz.html", question=questions[session["question"]]["question"], question_number=session["question"],
                            nb_questions = len(questions), options=questions[session["question"]]["options"], score = session["mark"], score_total = len(questions)*4)


@app.route('/logout')
def logout():
    # réinitialiser la session
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))    




@app.route('/metrics')
def metrics():
    df = pd.read_csv(file_csv) 
    cols = copy.copy(liste_choice)
    cols.insert(0,'user')
    ### la colonne score
    cols.insert(df.shape[1], 'score')
    df.columns = cols
    ### on va déterminer quel pokemon est le plus souvent reconnu par les utilisateurs pour ensuite l'afficher
    max_bonne_reponse = 0
    for question in range(0, longueur_questionnaire) : 
        if dict_global[liste_choice[question]] == 'Pokemon' : 
            try:
                nombre_reponse = df[liste_choice[question]].value_counts()['Pokemon'] 
                if nombre_reponse > max_bonne_reponse : 
                    max_bonne_reponse = nombre_reponse
                    pokemon_mieux_trouve_image = liste_choice[question].lower() + ".jpg"
                    pokemon_mieux_trouve = liste_choice[question]
            except KeyError:
                pass


    df.sort(['score'], ascending=[0],inplace = True)

    return render_template('metrics.html',tables=[df.head(3).to_html(index = False)],
                                                  titles = cols , nom_pokemon = pokemon_mieux_trouve, 
                                                  nb_answers = df.shape[0], image = pokemon_mieux_trouve_image )

if __name__ == '__main__':
    app.run(debug = True)
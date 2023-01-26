from flask import Flask  # pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    # return "Hello World!"
    return "Salutation!" # Exercice 1 - Remplacez "Hello World !" par "ce que vous voulez" et affichez ce nouveau texte dans la page hébergée en local.

if __name__ == "__main__":
    app.run()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home2.html", message_bienvenue="Bienvenue sur la page d'accueil !")

@app.route("/next")
def suite():
    return render_template("page_suivante.html")

# gestion d'erreur 404
@app.errorhandler(404)  
# inbuilt function which takes error as parameter
def not_found(e):  
# defining function
    return render_template("404.html")

if __name__ == "__main__":
   app.run()
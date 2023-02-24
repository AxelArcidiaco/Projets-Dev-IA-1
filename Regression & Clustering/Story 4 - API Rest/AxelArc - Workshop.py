# Importation bibliothèque Python
from flask import Flask, request
from flask_restplus import Api, Resource, fields
from werkzeug.utils import cached_property

persons = {
    "Arcidiaco": "Axel",
    "Perciot": "Nicolas",
    "Panel": "Loic",
    "Jacquenet": "Adrien",
    "Bouchonnet": "Aude",
    "Kurdy": "Bassam"
}

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")

name_space = app.namespace('names', description='Manage names')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

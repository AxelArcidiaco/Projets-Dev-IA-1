# Importation bibliothèque Python
from flask import Flask
from flask_restplus import Api, Resource

persons = {
    "Arcidiaco": "Axel",
    "Perciot": "Nicolas",
    "Panel": "Loic",
    "Jacquenet": "Adrien",
    "Bouchonnet": "Aude",
    "Kurdy": "Bassam"
}

flask_app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace('main', description='Main APIs')

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

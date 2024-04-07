from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

this_is_our_location = os.path.abspath(os.path.dirname(__file__))
the_file_path_of_db = os.path.join(this_is_our_location, 'listed_building_db.db')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + the_file_path_of_db

db=SQLAlchemy(app)

from my_db_app import routes
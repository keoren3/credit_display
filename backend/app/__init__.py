from flask import Flask
from flask_cors import CORS
from config import Config
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager


back_app = Flask(__name__)
back_app.config.from_object(Config)

CORS(back_app)
mongo = PyMongo(back_app)
bcrypt = Bcrypt(back_app)
jwt = JWTManager(back_app)

from app.profile import profile
back_app.register_blueprint(profile)




from app import routes


from flask import Flask
from flask_cors import CORS
from config import Config

back_app = Flask(__name__)
CORS(back_app)
back_app.config.from_object(Config)

from app import routes
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class Config(object):
   UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
   JWT_SECRET_KEY = 'creadit-display-super-secret'
   MONGO_URI = "mongodb+srv://rohiz:r2u4g6h8@creditdata-xurnm.mongodb.net/rohi_db"
   DEBUG=True


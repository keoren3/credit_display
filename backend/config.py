import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
    JWT_SECRET_KEY = 'credit-display-super-secret'
    SECRET_KEY = "credit-display-super-secret"
    MONGODB_SETTINGS = {
        'DB': 'rohi_db',
        'host': "mongodb+srv://creditdata-xurnm.mongodb.net/rohi_db",
        'port': 8080,
        'username': 'rohiz',
        'password': 'r2u4g6h8'
    }
    # MONGO_URI = "mongodb+srv://rohiz:r2u4g6h8@creditdata-xurnm.mongodb.net/rohi_db"

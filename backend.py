from flask import Flask
from db_handler import db_handler

app = Flask(__name__)
db_user = ""

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    db = db_handler("mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
    db.connect_to_db("t")
    app.run()

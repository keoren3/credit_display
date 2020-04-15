
import uuid
from app import app

from app import db_handler
from flask import Flask, flash, redirect, request, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_pymongo import PyMongo


ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}

DEBUG = True



# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/register',methods=['POST'])
def register():
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    # db.insert({'user_test': user_name,'user_password_test':password})
    return 'Success'



@app.route('/result_success', methods=['GET'])
def result_s():
    return "File Uploaded Successfully"


@app.route('/result_failed', methods=['GET'])
def result_f():
    return "File Uploaded Fail"


@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('result_f'))
        file = request.files['file']
        filename = secure_filename(file.filename)

        # Gen GUUID File Name
        fileExt = filename.split('.')[1]
        autoGenFileName = uuid.uuid4()

        newFileName = str(autoGenFileName) + '.' + fileExt

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newFileName))
        response_object['message'] = 'File added'
        # print("finish save file")
        return redirect(url_for('result_s'))
    return jsonify(response_object)


if __name__ == '__main__':
    # db = db_handler(
    #     "mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
    # db.connect_to_db("t")
    app.run()

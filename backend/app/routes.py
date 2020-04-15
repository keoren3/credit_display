
import uuid
import os
from app import back_app

from flask import Flask, flash, redirect, request, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_pymongo import PyMongo


ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}






# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
mongo = PyMongo(back_app)


@back_app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Pong!')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@back_app.route('/')
def hello():
    return "Hey EveryOne!"

@back_app.route('/register',methods=['POST'])
def register():
    users = mongo.db.users
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    users.insert({'user_test': user_name,'user_password_test':password})
    return 'Success'




@back_app.route('/result_success', methods=['GET'])
def result_s():
    return "File Uploaded Success"


@back_app.route('/result_failed', methods=['GET'])
def result_f():
    return "File Uploaded Fail"


@back_app.route('/upload', methods=['GET', 'POST'])
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


# if __name__ == '__main__':
#     # db = db_handler(
#     #     "mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
#     # db.connect_to_db("t")
#     app.run()

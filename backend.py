import os
import uuid

from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from credit_backend import get_data_from_excel
from db_handler import db_handler

ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
    return "Hello World!"


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

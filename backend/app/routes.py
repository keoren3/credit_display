
import uuid
import os
from app import back_app

from flask import Flask, flash, redirect, request, url_for, jsonify
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}


@back_app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Pong!')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@back_app.route('/')
def hello():
    return "Hey EveryOne!"

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
        return "Upload successfuly"
    return jsonify(response_object)


# if __name__ == '__main__':
#     # db = db_handler(
#     #     "mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
#     # db.connect_to_db("t")
#     app.run()


import uuid
import os

from flask import Blueprint, flash, redirect, request, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import get_jwt_identity, jwt_required

file_handler = Blueprint('file_handler', __name__)

ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_handler.route('/upload', methods=['GET', 'POST'])
@jwt_required
def uploadFile():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
    #    if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(url_for('result_f'))
    #     file = request.files['file']
    #     filename = secure_filename(file.filename)

    #     # Gen GUUID File Name
    #     fileExt = filename.split('.')[1]
    #     autoGenFileName = uuid.uuid4()

    #     newFileName = str(autoGenFileName) + '.' + fileExt

    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], newFileName))
    #     response_object['message'] = 'File added'
    #     # print("finish save file")
    #     return "Upload successfuly"
    return jsonify(response_object)


# if __name__ == '__main__':
#     # db = db_handler(
#     #     "mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
#     # db.connect_to_db("t")
#     app.run()

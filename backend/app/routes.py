
import uuid
import os
import tempfile
from flask import Blueprint, flash, redirect, request, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.excel_handler import get_data_from_excel
from app.models import User
file_handler = Blueprint('file_handler', __name__)

ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_handler.route('/upload', methods=['GET', 'POST'])
@jwt_required
def uploadFile():
    current_user = get_jwt_identity()
    response_object = {'status': 'failed'}
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('result_f'))
        file = request.files['file']
        t_dir = tempfile.TemporaryDirectory()
        path = os.path.join(t_dir.name, file.filename)
        file.save(path)

        transactions = get_data_from_excel(path)
        user = User.objects(user_name=current_user).first()
        print(user)
        user.set_transactions(transactions)
        user.save()
        # print("finish save file")
        return "Upload successfuly"
    return jsonify(response_object)


# if __name__ == '__main__':
#     # db = db_handler(
#     #     "mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
#     # db.connect_to_db("t")
#     app.run()

from flask import Flask, render_template, request, flash, redirect, url_for
import os
from db_handler import db_handler
from werkzeug.utils import secure_filename
from credit_backend import get_data_from_excel

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'xls', 'csv', 'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            data = get_data_from_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return data


if __name__ == '__main__':
    db = db_handler("mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test")
    db.connect_to_db("t")
    app.run()

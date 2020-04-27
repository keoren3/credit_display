from flask import Blueprint, jsonify, request
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User

profile = Blueprint('profile', __name__)


@profile.route('/register', methods=['POST'])
def register():
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    created = datetime.utcnow()
    hash_password = generate_password_hash(password)

    new_user = User(user_name=user_name,
                    password=hash_password, created=created)
    new_user.save()

    return 'Success'


@profile.route('/login', methods=['POST'])
def login():

    user_name = request.get_json()['user_name']
    password = request.get_json()['password']

    user = User.objects(user_name=user_name).first()

    if user is not None:
        if check_password_hash(user['password'], password):
            return jsonify({'token': create_access_token(identity=user_name)})
        else:
            return jsonify({'result': 'failed'})
    return 'ERROR 404'

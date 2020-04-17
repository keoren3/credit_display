from flask import Blueprint,jsonify,request
from app import mongo,bcrypt,jwt
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


profile = Blueprint('profile', __name__)

@profile.route('/register',methods=['POST'])
def register():
    print("got here")
    users = mongo.db.users
    print(users)
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    created = datetime.utcnow()
    print(users.insert
    (
    {'user_name': user_name,
    'password':generate_password_hash(password),
    'created':created}))
    return 'Success'

@profile.route('/login',methods=['POST'])
def login():
    users = mongo.db.users
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    user = users.find_one({'user_name':user_name}   )
    if user:
        if check_password_hash(user['password'],password):
            return jsonify({'token': create_access_token(identity = user_name)})
        else:
            return jsonify({'result':'failed'})
    return 'ERROR 404'


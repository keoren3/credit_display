from flask import Blueprint,jsonify,request
from app import mongo,bcrypt,jwt

profile = Blueprint('profile', __name__)

@profile.route('/register',methods=['POST'])
def register():
    users = mongo.db.users
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    users.insert({'user_name': user_name,'password':password})
    return 'Success'

@profile.route('/login',methods=['POST'])
def login():
    users = mongo.db.users
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    print(user_name , password)
    response = users.find_one({'user_name':user_name}   )
    if response:
        if password == response['password']:
            return jsonify({'result':'success'})
        else:
            return jsonify({'result':'failed'})
    return 'User client to login '


from flask_mongoengine import MongoEngine
db = MongoEngine()


class User(db.Document):
    user_name = db.StringField(required=True, unique=True)
    password = db.StringField(requited=True)
    created = db.DateTimeField(requited=False)

    meta = {'collection': 'users'}

    def __repr__(self):
        return '<User {}>'.format(self.user_name)

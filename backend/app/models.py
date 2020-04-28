from flask_mongoengine import MongoEngine
db = MongoEngine()


class Transaction(db.EmbeddedDocument):
    deal_date = db.StringField(required=True)
    business_name = db.StringField()
    deal_value = db.StringField()
    charge_value = db.StringField()
    more_details = db.StringField()


class User(db.Document):
    user_name = db.StringField(required=True, unique=True)
    password = db.StringField(requited=True)
    created = db.DateTimeField(requited=False)
    transactions = db.EmbeddedDocumentListField(Transaction)
    meta = {'collection': 'users'}

    def __repr__(self):
        return '<User {}>'.format(self.user_name)

    def set_transactions(self, transactions):
        for element in transactions:
            tr = Transaction(**element)
            self.transactions.append(tr)

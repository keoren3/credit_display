from pymongo import MongoClient


class db_handler:
    def __init__(self, url):
        """Initializes the data base handler"""
        self._url = url
        print("Connecting to client...")
        self._client = MongoClient(self._url)
        print("Connected!")

    def connect_to_db(self, db_name):
        print("Connecting to database {0}...".format(db_name))
        self._db = self._client[db_name]
        print("Connected to database {0}".format(db_name))

    def connect_to_collection(self, collection):
        print("Connecting to collection {0}...".format(collection))
        self._collection = self._db[collection]
        print("Connected to collection {0}".format(collection))

    def insert_transactions(self, data):
        """
        Inserts all the transactions to the database
        :param list data: List holding all the data (Every cell is in a JSON format)
        """
        print("Inserting many...")
        self._collection.insert_many(data)
        print("Finished inserting!")

    def remove_collection_from_db(self):
        print("Removing collection")
        self._collection.drop()

    def get_shop_and_amount(self):
        shop_amount_list = []
        for record in self._collection.find():
            shop_amount_list.append({record['business_name']: record['charge_value']})
        return shop_amount_list


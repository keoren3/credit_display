from pymongo import MongoClient


class db_handler:
    def __init__(self, url, collection):
        """Initializes the data base handler"""
        self._url = url
        self._collection = collection
        self._db = None


    def insert_transactions_db(self, data):
        """
        Inserts all the transactions to the database
        :param list data: List holding all the data (Every cell is in a JSON format)
        """
        print("Inserting many...")
        self._db[self._collection].insert_many(data)
        print("Finished inserting!")


    def connect_to_db(self):
        print("Connecting to database....")
        client = MongoClient(self._url)
        self._db = client[self._collection]

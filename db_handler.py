import ssl
from pymongo import MongoClient


class db_handler:
    def __init__(self, url):
        """Initializes the data base handler"""
        self._url = url
        print("Connecting to client...")
        self._client = MongoClient(self._url, ssl_cert_reqs=ssl.CERT_NONE)
        print("Connected!")

    def connect_to_db(self, db_name):
        print("Connecting to database {0}...".format(db_name))
        self._db = self._client[db_name]
        print("Connected to database {0}".format(db_name))

    def get_collections_list(self):
        return self._db.list_collection_names()

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

    def remove_collection_from_db(self, collection):
        print("Removing collection")
        drop_check = self._db[collection].drop()
        print("Collection was dropped: {0}".format(drop_check))

    def get_shop_and_amount(self):
        shop_amount_list = []
        for record in self._collection.find():
            shop_amount_list.append({record['business_name']: record['charge_value']})
        return shop_amount_list

    def update_shop_group(self, shop, group):
        print("Updating the shop group collection")
        print("Switching to the shop-group collection")
        self._shop_group_col = self._db["shop_group_col"]
        inserted_json = {"shop": shop, "group": group}
        print("Inserting: {0}".format(inserted_json))
        self._shop_group_col.insert_one(inserted_json)
        print("Inserted: {0}".format(inserted_json))

    def get_spent_by_date(self, spend_date):
        print("Getting all bought items on date: {0}".format(spend_date))
        bought_items = self._collection.find({"deal_date": "{0}".format(spend_date)})
        print("Collected the items.")
        return bought_items

import ssl
import logging

from pymongo import MongoClient

logger = logging.getLogger(__name__)


class db_handler:
    def __init__(self, url):
        """Initializes the data base handler"""
        self._url = url
        try:
            logger.info("Connecting to client...")

            self._client = MongoClient(self._url, ssl_cert_reqs=ssl.CERT_NONE)

            logger.info("Client Connected!")

        except:
            logger.error("Client Failed to connect ")

    def connect_to_db(self, db_name):
        logger.info("Connecting to database {0}...".format(db_name))

        self._db = self._client[db_name]

        logger.info("Connected to database {0}".format(db_name))

    def get_collections_list(self):
        return self._db.list_collection_names()

    def connect_to_collection(self, collection):
        logger.info("Connecting to collection {0}...".format(collection))

        self._collection = self._db[collection]

        logger.info("Connected to collection {0}".format(collection))

    def insert_transactions(self, data):
        """
        Inserts all the transactions to the database
        :param list data: List holding all the data (Every cell is in a JSON format)
        """
        logger.info("Inserting many...")

        self._collection.insert_many(data)

        logger.info("Finished inserting!")

    def remove_collection_from_db(self, collection):
        logger.info("Removing collection")

        drop_check = self._db[collection].drop()

        logger.info("Collection was dropped: {0}".format(drop_check))

    def get_shop_and_amount(self):
        shop_amount_list = []
        for record in self._collection.find():
            shop_amount_list.append(
                {record['business_name']: record['charge_value']})
        return shop_amount_list
    
    def insert(self,o):
        self._collection.insert_one(o)

    def update_shop_group(self, shop, group):
        logger.info("Updating the shop group collection")
        logger.info("Switching to the shop-group collection")

        self._shop_group_col = self._db["shop_group_col"]
        inserted_json = {"shop": shop, "group": group}

        logger.info("Inserting: {0}".format(inserted_json))

        self._shop_group_col.insert_one(inserted_json)

        logger.info("Inserted: {0}".format(inserted_json))

    def get_spent_by_date(self, spend_date):
        logger.info(
            "Getting all bought items on date: {0}".format(spend_date))

        bought_items = self._collection.find(
            {"deal_date": "{0}".format(spend_date)})

        logger.info("Collected the items.")

        return bought_items

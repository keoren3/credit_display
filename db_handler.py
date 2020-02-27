from pymongo import MongoClient


def insert_db(db, data):
	print("Inserting many!")
	db.insert_many(data)
	print("Finished inserting!")


def connect_to_db(url, collection):
	print("Connecting....")
	client = MongoClient(url)
	db = client[collection]
	return db.test_collection
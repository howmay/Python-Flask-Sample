from pymongo import collection
from app.application import mongo


class MongoDB(object):
    @staticmethod
    def Insert(collection: str, data) -> bool:
        c = _get_collection(collection)
        _id = c.insert_one(data).inserted_id
        if _id is not None:
            return True
        return False

    @staticmethod
    def InsertMany(collection: str, data):
        pass


def _get_collection(collection: str) -> collection:
    if collection == "test":
        return mongo.db.test

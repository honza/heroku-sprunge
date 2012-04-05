from datetime import datetime
from pymongo import Connection
from bson.objectid import ObjectId
from settings import MONGO_URI, MONGO_DB_NAME


try:
    connection = Connection(MONGO_URI)
    db = connection[MONGO_DB_NAME]
    snippets = db.snippets
except:
    print 'mongo error'


def now():
    return datetime.utcnow()


def insert(snippet):
    return snippets.insert({
        'content': snippet,
        'date': now()
    })


def find(name):
    return snippets.find_one({'_id': ObjectId(name)})

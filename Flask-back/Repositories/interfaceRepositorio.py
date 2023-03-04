import pymongo
import certifi
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar,Generic,List,get_origin,get_args
import json
T = TypeVar('T')
class interfaceRepositorio(Generic[T]):
    def __init__(self):
        ca = certifi.where()
        dataconfig = self.loadConfig()
        client = pymongo.MongoClient(dataconfig["data-db-connection"],tlsCAFile=ca)
        self.db = client[dataconfig["name-db"]]
        theClass = get_args(self.__orig_bases__[0])
        collection = theClass[0].__name__.lower()

    def loadConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data

    def save(self, item: T):
        self.db.list_collection_names()
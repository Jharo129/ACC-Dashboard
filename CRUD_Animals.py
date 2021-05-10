from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import loads, dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username: str, password: str) -> None:
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52259' % (username, password))
        self.database = self.client['AAC']
        self.collection = self.database['animals']

# Create Method.
    def create(self, data):
        if data is not None:
            try:
                #return self.collection.insert_one(data).inserted_id
                self.collection.insert_one(data)
                return True
            except:
                return False
                
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read Method. 
    def read(self, query, projection=None):
        if query is not None:        
            record = self.collection.find(query, projection)
            json_str = dumps(record)
            record2 = loads(json_str)
            return record2
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    
# Update Method. 
    def update(self,query, data):
        true = {"value" : True}
        false = {"value" : False}
        if query is not None:
            try:
                self.collection.update_one(query, data)
                return true
            except:
                return false     
        else:
            raise Exception("Nothing to save, because query parameter is empty")
    
# Delete Method. 
    def delete(self, query):
        true = {"value" : True}
        false = {"value" : False}
        if query is not None:
            try:
                self.collection.delete_one(query)
                return true
            except:
                return false          
        else:
            raise Exception("Nothing to save, because query parameter is empty")
from pymongo import MongoClient


client=MongoClient('localhost',27017)
db=client.test_database
collection=db.blog

collection.insert_one({'test':'233'})
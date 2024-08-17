from pymongo import MongoClient
from flask import current_app

def initialize_db(app):
    try:
        client=MongoClient(app.config['MONGO_URI'])
        app.db=client[app.config['MONGO_DBNAME']]
        print("Database connected successfully!")
    except Exception as e:
        print("Failed to connect to the database")
        # print(e)
        raise e
 
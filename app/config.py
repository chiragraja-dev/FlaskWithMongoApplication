# class Config:
#     MONGO_URI='mongodb://localhost:27017/'
#     MONGO_DBNAME ='flask-first-app'

# class DevelopmentConfig(Config):
#     DEBUG=True

class DevelopmentConfig:
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DBNAME = 'flask-first-app'
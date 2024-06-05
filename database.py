from mongoengine import connect

def init_db():
    connect(db="jkh_db", host="localhost", port=27017)

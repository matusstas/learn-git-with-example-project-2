from tinydb import TinyDB

db = TinyDB("db.json")

def insert_post(post):
    db.insert(post)

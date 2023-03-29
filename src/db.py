from tinydb import TinyDB

db = TinyDB("db.json")

def insert_post(post):
    """
    Insert post into db
    """
    db.insert(post)

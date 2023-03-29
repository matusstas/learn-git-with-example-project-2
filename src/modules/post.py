import db

def create_post(title, text):
    db.insert_post({title: "a", text: "b"})

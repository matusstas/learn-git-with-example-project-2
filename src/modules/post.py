import db

def create_post(title, text):
    """
    Create post
    """
    db.insert_post({title: "a", text: "b"})

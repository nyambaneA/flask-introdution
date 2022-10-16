import json


def load_db():
    with open('welcome_db.json') as f:
        return json.load(f)

def save_data():
    with open('welcome_db.json', 'w')as f:
        json.dump(db, f)


db = load_db()


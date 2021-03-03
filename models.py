import json


def load_db():
    with open("datab.json") as f:
        return json.load(f)


def save_db():
    with open("datab.json", 'w') as f:
        return json.dump(db, f)


db = load_db()
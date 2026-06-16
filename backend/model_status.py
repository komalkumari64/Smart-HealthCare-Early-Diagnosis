from backend.mongodb import db

def update_training(percent):

    db.training.update_one(
        {"name":"rf"},
        {"$set":{"progress":percent}},
        upsert=True
    )

def get_training():

    data=db.training.find_one({"name":"rf"})

    if data:
        return data["progress"]

    return 0
from backend.mongodb import db
from datetime import datetime

def log_search(query):

    db.searches.insert_one({

        "query":query,

        "time":
        datetime.now()

    })


def log_chat(message):

    db.chats.insert_one({

        "message":message,

        "time":
        datetime.now()

    })


def log_image(filename):

    db.images.insert_one({

        "file":filename,

        "time":
        datetime.now()

    })


def log_prediction(result):

    db.predictions.insert_one({

        "result":result,

        "time":
        datetime.now()

    })
def log_login(email):

    db.login_history.insert_one({

        "email": email,

        "time": datetime.now()

    })
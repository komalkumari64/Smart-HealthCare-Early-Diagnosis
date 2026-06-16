from backend.mongodb import db
from datetime import datetime

def user_online(email):

    db.users.update_one(
        {"email":email},
        {
            "$set":{
                "status":"active",
                "last_seen":datetime.now()
            }
        }
    )
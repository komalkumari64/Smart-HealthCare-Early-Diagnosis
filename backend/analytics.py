from backend.mongodb import db

# --------------------
# Dashboard Stats
# --------------------

def get_stats():

    return {

        "patients":
        db.users.count_documents({}),

        "active":
        db.users.count_documents({
            "status":"active"
        }),

        "searches":
        db.searches.count_documents({}),

        "images":
        db.images.count_documents({}),

        "chats":
        db.chats.count_documents({}),

        "predictions":
        db.predictions.count_documents({}),

        "logins":
        db.login_history.count_documents({})
    }


# --------------------
# Recent Activity
# --------------------

def recent_activity():

    activities=[]

    users=db.users.find().sort(
        "_id",-1
    ).limit(3)

    for user in users:

        activities.append(
            f"👤 New User : {user['email']}"
        )

    searches=db.searches.find().sort(
        "_id",-1
    ).limit(3)

    for search in searches:

        activities.append(
            f"🔍 Search : {search['query']}"
        )

    images=db.images.find().sort(
        "_id",-1
    ).limit(3)

    for image in images:

        activities.append(
            f"🖼 Image : {image['file']}"
        )

    return activities


# --------------------
# Last Active User
# --------------------

def last_active_user():

    user = db.login_history.find_one(
        sort=[("_id",-1)]
    )

    if user:

        return user["email"]

    return "No User"


# --------------------
# Login History
# --------------------

def login_history():

    return list(

        db.login_history.find()

        .sort("_id",-1)

        .limit(10)

    )
from backend.mongodb import db

def top_diseases():

    pipeline = [

        {
            "$group":{
                "_id":"$result",
                "count":{"$sum":1}
            }
        },

        {
            "$sort":{
                "count":-1
            }
        }

    ]

    return list(
        db.predictions.aggregate(
            pipeline
        )
    )
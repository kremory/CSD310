from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.550ivtl.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech
collection=db.students
result = collection.update_one(
    {"student_id": 1007},
    {"$set":
     {
            "last_name": "Malfoy"
            }
            }
            )
cursor=collection.find()
for record in cursor:
    print(record)

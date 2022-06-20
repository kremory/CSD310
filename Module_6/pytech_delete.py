from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.550ivtl.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech
collection=db.students
cursor=collection.find()
for record in cursor:

    print(record)
draco={
    "first_name": "Draco",
    "last_name": "Malfoy",
    "student_id": "1010"
}
draco_student_id=collection.insert_one(draco).inserted_id
doc=db.students.find_one({"student_id": "1010"})
print(doc["student_id"])
fordelete={"student_id": '1010'}
collection.delete_one(fordelete)
cursor=collection.find()
for record in cursor:

    print(record)
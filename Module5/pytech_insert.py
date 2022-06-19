from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.550ivtl.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech
fred = {"first_name": "Fred",
        "student_id":"1007",
        "last_name":"Weasely"}
harry={
    "first_name": "Harry",
        "student_id":"1008",
        "last_name":"Potter"
}
hermonie={"first_name": "Hermonie",
        "student_id":"1009",
        "last_name":"Granger"}
col=db.students
fred_student_id=col.insert_one(fred).inserted_id
col.insert_one(harry).inserted_id
col.insert_one(hermonie).inserted_id
print(fred_student_id)
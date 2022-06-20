from unittest import result
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.550ivtl.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech
collection=db.students
cursor=collection.find()
for record in cursor:

    print(record)
newname= { "$set": {'last_name':'Malfoy'}}
stud_id={'student_id':'1007'}
result=collection.update_one(stud_id, newname)
doc=collection.find_one({"student_id": "1007"})
print(doc["last_name"])

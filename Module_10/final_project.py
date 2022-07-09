import mysql.connector
from mysql.connector import errorcode
config ={
    "user" : "root",
    "password": "Romulos21!",
    "host" : "127.0.0.1",
    "database" : "final_project",
    "raise_on_warnings" : True
}
db=mysql.connector.connect(**config)
cursor=db.cursor()
query = "SELECT _revenue, bussiness_name, _address FROM business"
cursor.execute(query)
businesses=cursor.fetchall()

print("\n-- DISPLAYING BUSINESS RECORDS --\n")
for business in businesses:
    print(" Revenue: {}\nBussiness Name and Year: {} \nAddress:  {}\n".format(business[0], business[1], business[2]))
query = "SELECT employee_id, first_name, last_name,job_code,_salary FROM employee"
cursor.execute(query)
employees=cursor.fetchall()

print( "\n-- DISPLAYING EMPLOYEE RECORDS --\n")
for employee in employees:
    print("Employee ID: {}\n First Name: {} \n Last Name:  {}\n Job Code:  {}\n Salary:   {}\n".format(employee[0], employee[1], employee[2], employee[3], employee[4]))
query = "SELECT job_code, _functions, _title FROM roles"
cursor.execute(query)
roley=cursor.fetchall()

print("\n-- DISPLAYING ROLES--\n")
for roles in roley:
    print("Job Code: {}\n Functions: {} \n Title:  {}\n".format(roles[0], roles[1], roles[2]))
query = "SELECT client_id, _name, _company FROM clients"
cursor.execute(query)
clientt=cursor.fetchall()
print("\n-- DISPLAYING CLIENTS--\n")
for clients in clientt:
    print(" Client ID: {}\n Name: {} \n Company:  {}\n".format(clients[0], clients[1], clients[2])) 
query = "SELECT _value, _name, _code,client_id FROM transactions"
cursor.execute(query)
trans=cursor.fetchall()

print("\n-- DISPLAYING TRANSACTIONS--\n")
for transactions in trans:
    print(" Value: {}\n Name: {} \nCode:  {},\nClient ID:   {}\n".format(transactions[0], transactions[1], transactions[2],transactions[3]))
query = "SELECT client_id,_name,_value FROM assets"
cursor.execute(query)
assetss=cursor.fetchall()
print("\n-- DISPLAYING ASSETS--\n")
for assets in assetss:
    print("Client ID: {}\n Name: {} \n Value:  {}\n".format(assets[0], assets[1], assets[2]))     
cursor.close()
db.close()
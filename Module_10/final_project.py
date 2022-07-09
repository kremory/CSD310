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

print("\n-- DISPLAYING BUSINESS RECORDS --")
for business in businesses:
    print(" Revenue: {}\n Bussiness Name and Year: {} \n Address:  {}".format(business[0], business[1], business[2]))
query = "SELECT employee_id, first_name, last_name,job_code,_salary FROM employee"
cursor.execute(query)
employees=cursor.fetchall()

print( "\n-- DISPLAING EMPLOYEE RECORDS --")
for employee in employees:
    print(" Employee ID: {}\n First Name: {} \n Last Name:  {}\n Job Code:  {}\n Salary:   {}".format(employee[0], employee[1], employee[2], employee[3], employee[4]))
query = "SELECT job_code, _functions, _title FROM roles"
cursor.execute(query)
roley=cursor.fetchall()

print("\n-- DISPLAYING ROLES--")
for roles in roley:
    print(" Job Code: {}\n Functions: {} \n Title:  {}".format(roles[0], roles[1], roles[2]))
query = "SELECT client_id, _name, _company FROM clients"
cursor.execute(query)
clientt=cursor.fetchall()
print("\n-- DISPLAYING CLIENTS--")
for clients in clientt:
    print(" Client ID: {}\n Name: {} \n Company:  {}".format(clients[0], clients[1], clients[2])) 
query = "SELECT _value, _name, _code,client_id FROM transactions"
cursor.execute(query)
trans=cursor.fetchall()

print("\n-- DISPLAYING TRANSACTIONS--")
for transactions in trans:
    print(" Value: {}\n Name: {} \n Code:  {},\n Client ID:   {}".format(transactions[0], transactions[1], transactions[2],transactions[3]))
query = "SELECT client_id,_name,_value FROM assets"
cursor.execute(query)
assetss=cursor.fetchall()
print("-- DISPLAYING ASSETS--")
for assets in assetss:
    print(" Client ID: {}\n Name: {} \n Value:  {}".format(assets[0], assets[1], assets[2]))     
cursor.close()
db.close()
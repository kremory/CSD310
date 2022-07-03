import mysql.connector
from mysql.connector import errorcode
config ={
    "user" : "root",
    "password": "Romulos21!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True
}
db=mysql.connector.connect(**config)
# Create a cursor
cursor = db.cursor()

# Write the query
query = "SELECT team_id, team_name, mascot FROM team"
que= "SELECT player_id, first_name, last_name, team_id FROM player"
# Execute the query
cursor.execute(query)

teams=cursor.fetchall()
# Iterate over the cursor
print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print(" Team ID: {}\n Team Name: {} \n Mascot:  {}".format(team[0], team[1], team[2]))
# Close the cursor
cursor.execute(que)
players=cursor.fetchall()
print("--DISPLAING PLAYER RECORDS --")
for player in players:
    print(" Player ID: {}\n FirstName: {}\n Last Name: {}\n Team ID: {}".format(player[0],player[1],player[2],player[3]))
cursor.close()

# Close the database
db.close()
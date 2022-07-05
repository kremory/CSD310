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
cursor=db.cursor()
query="SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id=team.team_id;"
cursor.execute(query)
players=cursor.fetchall()
print(" -- DISPLAYING PLAYER RECORDS --")
for player in players:
    print(" Player ID: {}\n FirstName: {}\n Last Name: {}".format(player[0],player[1],player[2]))
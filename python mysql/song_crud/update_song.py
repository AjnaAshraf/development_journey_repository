from mysql import connector

#establish connection object
connection = connector.connect (

    user = "root",
    password="Password@123",
    host="localhost",
    database="song_db"

)

cursor = connection.cursor()

query ="""
update song set title = %s,track_number = %s,movie =%s,singers =%s where id =%s
"""
values = ("engotte",122,"balan", "sanjalii",6)

cursor.execute(query,values)

connection.commit()

print("records has been updated ")
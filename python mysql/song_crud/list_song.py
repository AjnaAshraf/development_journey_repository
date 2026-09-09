#import connector
from mysql import connector

#establish connection object
connection = connector.connect (

    user = "root",
    password="Password@123",
    host="localhost",
    database="song_db"

)

cursor = connection.cursor()

query="select * from song ; "

cursor.execute(query)

records = cursor.fetchall()

for song in records :

    print(song)
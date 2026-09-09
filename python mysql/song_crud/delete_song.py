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

query = " delete from song where id = %s;"

values=(3,) # one value tuple so , 

cursor.execute(query,values)

connection.commit()

print("the record has been deleted ...")


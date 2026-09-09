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

query = """

insert into song(title,track_number,movie,singers) values(%s,%s,%s,%s);

"""

values = ("kal ho na hoo",123,"kal ho na ho","A R Rahman")

cursor.execute(query,values)

connection.commit()
connection.close()

print("record has been inserted ......")

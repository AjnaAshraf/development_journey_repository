from mysql import connector

connection = connector.connect (

    user = "root",
    password="Password@123",
    host="localhost",
    database="book_db"

)

cursor = connection.cursor()

query = " select * from books where id = %s;"

values=(5,)

cursor.execute(query,values)

record = cursor.fetchone()

print(record)

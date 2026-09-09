from mysql import connector

connection = connector.connect (

    user = "root",
    password="Password@123",
    host="localhost",
    database="book_db"

)

cursor = connection.cursor()

query = """

update books set title = "Harry Potter" where id = %s;

"""
values=(4,)

cursor.execute(query,values)

connection.commit()
print("records has been updated ")
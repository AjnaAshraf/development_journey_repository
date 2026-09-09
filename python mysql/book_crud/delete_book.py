from mysql import connector

connection = connector.connect(

    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "book_db"

)

cursor = connection.cursor()

query="""

delete from books where id = %s;

"""

values = (6,)

cursor.execute(query,values)

connection.commit()

print("...... records has been succesfully deleted .....")
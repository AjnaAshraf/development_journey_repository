from mysql import connector

connection = connector.connect(

    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "book_db"

)

cursor = connection.cursor()

query="""

insert into books(title,author,genre,language,price) values(%s,%s,%s,%s,%s);

"""

values=("The Alchemist", "Paulo Coelho", "fiction", "English", 300.00)

cursor.execute(query,values)

connection.commit()
connection.close()

print("record has been inserted ......")


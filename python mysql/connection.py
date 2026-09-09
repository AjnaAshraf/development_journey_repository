# pip install mysql-connector-python

from mysql import connector


# to establish connection 

connection = connector.connect(
    user ="root",
    password = "Password@123",
    host = "localhost"
)

print(connection)


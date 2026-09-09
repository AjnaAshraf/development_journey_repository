"""
**Login System**: Verify username and password and display success or failure.


"""

db_username = "ajna@123"

db_password = 1234456778

username = input("enter the username: ")

if username == db_username:

    password = int(input("enter the password: "))

    if password == db_password:

        print("<<<<  LOGIN SUCESSFULL  >>>>")
    
    else:
        print("XXXX  INVALID PASSWORD XXXXX")

else:
    print("XXXXXX INVALID USERNAME XXXXX")


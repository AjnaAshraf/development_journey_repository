"""
 ✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"

"""

db_password = "aju@12345"

db_otp = 123456

password = input(" enter the password: ")

if password == db_password:

    otp = int(input(" enter OTP: "))

    if otp == db_otp:

        print("Login successful")

    else:

        print("incorrect OTP")

else:

    print("Incorrect password")
        

    

    

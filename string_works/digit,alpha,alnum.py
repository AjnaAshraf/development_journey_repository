"""
isalpha()
isdigit()
isalnum()

"""

password = "password124"

if password.isalpha():

    print(f"password is alphabet {password}")

elif password.isdigit():

    print(f"password is digit {password}")

elif password.isalnum():

    print(f"password is alphanumeric {password}")

else:

    print(f"password has special characters {password}")
employee = {"id":100,"name":"Ajna","dept":"cse"}

key = input("enter key: ")

try:
    print(employee[key])

except Exception as e:

    print(e)

finally:

    print("db commit")
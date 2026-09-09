try:

    fr = open("Error_handling\\keywords.txt","r")
    for line in fr:

        print(line)

except Exception as e:
    print(e)

finally:

    print("db commit")
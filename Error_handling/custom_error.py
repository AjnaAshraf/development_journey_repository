age = int(input("enter age"))

if age<18:

    raise Exception("invalid age")  #custom error throw cheyaan aan raise use akanath

else:

    print("eligible to vote")
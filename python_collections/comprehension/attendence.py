attendance = [1,-1,0,1,-1,1,-1,0,0]

result = ["p" if a==1 else "o" if a ==-1 else "h" for a in attendance]

print(result)
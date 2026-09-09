names =["John","","Alice","","David"]

new = ["unknown" if n == "" else n for n in names]

print(new)
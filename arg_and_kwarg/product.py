def product(*args):
    i=1
    for num in args:
        i = i * num
    return i

print(product(2,4))
print(product(1,2,1))
print(product(1,2,5))


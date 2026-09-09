arr = [10,11,1,10,11,2,3]

#display all no recursive

non_recursive=[num for num in arr if arr.count(num)==1]
print(non_recursive)

duplicate_numbers={num for num in arr if arr.count(num)>1}
print(duplicate_numbers)

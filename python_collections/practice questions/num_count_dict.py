arr = [10,10,1,1,1,1,3,4,2,3,3,2,4,6]

arr_set = set(arr)

num_count = {}

for num in arr_set:

    num_count[num]=arr.count(num)

print(num_count)
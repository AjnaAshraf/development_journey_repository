items = [
            ["potato",30,3],
            ["onion",30,4],
            ["carrot",40,1],
            ["beetroot",50,2],
            ["tomato",40,2]
        ]

print(items[-2][1])

print(items[-1][1:])

# for lst in items:

#     print(lst[0])

all_items = [lst[0] for lst in items]

print(all_items)
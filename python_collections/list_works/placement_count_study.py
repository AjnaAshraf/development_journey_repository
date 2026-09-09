#store last 6 month placement count 

placement_count = [10,15,22,9,17,18]

print()
#display feb month placement count

print("placement count of feb = ",placement_count[1])

#update jan month placement_count as 12
print()

placement_count[0]=12
print("updated placement count:",placement_count)

print()
#display placement_counts where count > 15

for count in placement_count:
    if count>15:
        print(count)

# display highest_placement_count without using max()
print()

highest=placement_count[0]

for count in range(0,len(placement_count)):

    if highest<=placement_count[count]:
        highest=placement_count[count]
print("highest placement count:",highest)

print()

# display lowest_placement_count without using min()
lowest = placement_count[0]

for count in range(0,len(placement_count)):

    if lowest>placement_count[count]:
        lowest=placement_count[count]
print("lowest placement count:",lowest)

print()


# display second_highest_placement_count without using sorted()

highest=0
second_highest = 0
for count in range(0,len(placement_count)): # count =0

    if highest<placement_count[count]:  
           # 
        second_highest=highest          
        highest=placement_count[count]

    elif placement_count[count]>second_highest:

        second_highest=placement_count[count]

print("second highest placement count:",second_highest)
        

   #


print()

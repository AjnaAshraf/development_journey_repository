"""
step1: set highest and second highest as 0
step2: repeat for each count in placement count
step3: check if count > highest:
step4: update second highest as highest and highest as count
step5: check if count > second highest
step6: update second highest as count
step7: display second highest

"""
#store last 6 month placement count 

placement_count = [10,15,22,9,17,18]


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

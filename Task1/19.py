"""

19. A pizza has 8 slices. 3 people eat 2 slices each. Find remaining slices.
"""

total_slice=int(input("enter the total slices of a pizza: "))
people= int(input("Enter the number of people: "))
slice_per_person=int(input("enter the slices of a pizza eaten per person: "))


remaining_slices=total_slice-(people*slice_per_person)
print("the remaining slice of pizza is: ",remaining_slices)
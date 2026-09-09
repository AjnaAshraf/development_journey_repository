"""
q3) attendance = ["p","p","a","a","o","o","h"]

    write a program to print attendance count
"""
attendance = ["p","p","a","a","o","o","h"]

attendence_set =set(attendance)

attendance_count = {}

for attend in attendence_set:

    attendance_count[attend] = attendance.count(attend)
    
print(attendance_count)
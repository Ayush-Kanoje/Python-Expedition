# Count Present students.
# Count Absent students.
# Print the attendance percentage.
# Present : 6
# Absent : 4
# Attendance : 60%
# The total number of students is the length of the list


attendance = [
    "Present",
    "Absent",
    "Present",
    "Present",
    "Absent",
    "Present",
    "Present",
    "Absent",
    "Present",
    "Absent"
]

count_present = 0
count_absent = 0

for presenty in attendance:
    if presenty == "Present":
        count_present += 1
    else:
        count_absent += 1
print(f"Total present student: {count_present}\nTotal Absent Student: {count_absent}")
print(count_present/len(attendance)*100)

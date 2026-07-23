# 6. Student Marks Report

# Marks:

# marks = [67, 45, 91, 76, 33, 58]

# Tasks:
# Print only passing marks (>=40).
# Count failed students.
# Find topper.
# Find average marks.

# Real-world:

# School management system.

marks = []

list_size = int(input("Enter size for list: "))

for i in range(list_size):
    marks_list= int(input(f"Enter marks of studednt{i+1}:"))
    marks.append(marks_list)
  
for i in marks:
    if i >= 40:
        print("passed")
        continue
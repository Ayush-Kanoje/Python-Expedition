# How many students?
# 5

# Enter marks: 78
# Enter marks: 45
# Enter marks: 90
# Enter marks: 55
# Enter marks: 20
# Expected Output
# Marks:
# 78
# 45
# 90
# 55
# 20

# Highest Mark : 90
# Lowest Mark : 20
# Average Mark : 57.6
# Students Passed : 3
def no_of_student(student):
    print("Total student: ",student)
    for student_mark in range(1,student+1):
        user = input(f"Enter marks for student {student_mark}: ")

# Take input from the user and convert it to an integer
num_students = int(input("How many students: "))
no_of_student(num_students)


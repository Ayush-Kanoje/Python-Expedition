marks = []

student_marks = int(input("Enter total no of student: "))

for x in range(student_marks):
    x = input("Enter marks: ")
    marks.append(x)

marks.sort()
print(marks)
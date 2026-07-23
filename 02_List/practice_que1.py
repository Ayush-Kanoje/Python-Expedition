# 1. Office Attendance Tracker ⭐

# A company stores employee names in a list.

# employees = ["Rahul", "Priya", "Amit", "Neha", "Rohan"]

# Tasks:

# Print every employee name.
# Print total number of employees.
# Print first employee.
# Print last employee.


employees = ["Rahul", "Priya", "Amit", "Neha", "Rohan","Ayush","Anushka"]
emp_count = 0
for name in range(len(employees)):
    print(f" {name+1}. Employe name: {employees[name]}" )
    emp_count += 1

print(emp_count)

print(employees[0],"\n",employees[-1])

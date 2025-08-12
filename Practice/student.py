students = []  # List to store student records


# 1. Accept student details
def accept():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    student = {"roll": roll, "name": name, "age": age, "course": course}
    students.append(student)
    print("Student added successfully!\n")


# 2. Display all students
def display():
    if not students:
        print("No student records found.\n")
    else:
        print("---- Student Records ----")
        for s in students:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
        print()


# 3. Search for a student
def search():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"Record found: Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}\n")
            return
    print("Student not found.\n")


# 4. Delete a student
def delete():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("Student record deleted successfully.\n")
            return
    print("Student not found.\n")


# 5. Update student details
def update():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s['roll'] == roll:
            s['name'] = input("Enter new Name: ")
            s['age'] = input("Enter new Age: ")
            s['course'] = input("Enter new Course: ")
            print("Student record updated successfully.\n")
            return
    print("Student not found.\n")


# Main Menu
while True:
    print("1. Accept")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        accept()
    elif choice == '2':
        display()
    elif choice == '3':
        search()
    elif choice == '4':
        delete()
    elif choice == '5':
        update()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.\n")

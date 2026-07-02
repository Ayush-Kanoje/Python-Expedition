# The librarian first enters how many books were borrowed today.

# Then, for each book, the librarian enters its title.

# Finally, your program should display:

# Total books borrowed.
# All book titles.
# The first book entered.
# The last book entered.
# User Input Example
# How many books were borrowed today?
# 4

# Enter book 1: Python Basics
# Enter book 2: Atomic Habits
# Enter book 3: Clean Code
# Enter book 4: Deep Work
# Expected Output
# Today's Library Report

# Total Books Borrowed : 4

# Books Borrowed:
# 1. Python Basics
# 2. Atomic Habits
# 3. Clean Code
# 4. Deep Work

# First Book : Python Basics
# Last Book : Deep Work
# Rules
# Ask the user for the number of books.
# Use a loop.
# Store the book names in a list.


total_no_of_books_borrowed = int(input("Enter total count of borrowed books: "))

def books(total_no_of_books_borrowed):
    for books_title in range(1,total_no_of_books_borrowed):
        books_list = input("Enter books title: ").append(books_list)
    print(books(books_list))

print(books(total_no_of_books_borrowed))
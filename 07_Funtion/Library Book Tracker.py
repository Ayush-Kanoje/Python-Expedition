# The librarian first enters how many books were borrowed today.

# Then, for each book, the librarian enters its title.

# Finally, your program should display:

# 📚 Today's Library Report

# Total Books Borrowed : 4

# Books Borrowed:
# 1. Python Basics
# 2. Atomic Habits
# 3. Clean Code
# 4. Deep Work

# First Book : Python Basics
# Last Book  : Deep Work


user_input = int(input("Enter total no of books borrowed: "))
def library_report(user_input):
    books_tiles = []
    for i in range(user_input):
        books_tiles.append(input("Enter title of books: "))
    print("Today Books report of borrowed books\n")
    print("Number of books borrowed: ", user_input)
    for i, books in enumerate(books_tiles, 1):
        print(f"\nBooks Borrowed: {i}. {books}")

    print(f"\nFirst Borrowed book: {books_tiles[0]}\nSecond Borrowed book: {books_tiles[-1]}")
    

library_report(user_input)

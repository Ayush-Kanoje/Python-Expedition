# Initialize an empty list to store movie names
movieList = []



# Add "spiderman" as the first movie in the list
movieList.append("spiderman")
print(movieList)  # Output: ['spiderman']




# Get the desired size of the list from user input
# Note: Size should be greater than 4 for slicing operations to work properly
list_size = int(input("Enter size of list, must be greater than 4: "))

# Use a loop to add movies to the list based on user input
for i in range(list_size):
    movie = input("Enter movie name: ")
    movieList.append(movie)




# LIST SLICING EXAMPLES:

# [1:3] - Slice from index 1 (inclusive) to index 3 (exclusive)
# This returns elements at index 1 and 2 (2 elements total)
print(movieList[1:3])  # Output: 2nd and 3rd movies



# Replace slice [1:3] with a string
# IMPORTANT: When assigning a string to a slice, Python iterates over each character
# So "lemon" becomes ['l', 'e', 'm', 'o', 'n'] - each character becomes a separate element!
# This replaces 2 elements (index 1, 2) with 5 individual characters
movieList[1:3] = "lemon" 
print(movieList)  # Shows the list with characters inserted



# [:-1] - Slice from start to the last element (exclusive), i.e., all elements except the last one
# Replace all elements except the last one with ["orange"]
movieList[:-1] = ["orange"]
print(movieList)  # Output: ['orange', last_element]



# Alternative approach using list comprehension (commented out)
Movie_list_size = int(input("Enter size: "))
my_list = [input(f"Enter item {i+1}: ") for i in range(size)]
print(my_list)






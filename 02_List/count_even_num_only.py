# Q1. Count even numbers
# Given a list, count how many elements are even.

# numbers1 = [3, 8, 2, 7, 10, 5, 6]

# count_even = 0
# for even_num in numbers1:
#     if even_num %2 == 0:
#         count_even += 1
# print(count_even)



# Q2. Find the second largest element
# Find the second largest number without using sort().

# numbers2 = [10, 5, 8, 20, 15,20]

# current = 0
# for val in numbers2:
#     if val < max(numbers2):
#         if val > current: 
#             current = val
   
# print(current)


# Q3. Find the first duplicate
# Return the first element that appears more than once.

# numbers3 = [1, 2, 7, 9, 4,15,9]

# numbers3.sort()

# for idx,val in enumerate(numbers3):
#     if idx+1 <len(numbers3) and val == numbers3[idx+1]:
#         print(f"duplicate value: {val}")
#         break


# Q4. Move all zeros to the end
# Move every 0 to the end while keeping the order of the other elements.

# numbers4 = [0, 1, 0, 3, 12]




# Q5. Remove duplicates
# Create a new list containing each number only once, while preserving order.

numbers = [1, 2, 2, 3, 1, 4, 3]





# Q1. Count even numbers
# Given a list, count how many elements are even.

numbers1 = [3, 8, 2, 7, 10, 5, 6]

count_even = 0
for even_num in numbers1:
    if even_num %2 == 0:
        count_even += 1
print(count_even)



# Q2. Find the second largest element
# Find the second largest number without using sort().

numbers2 = [10, 5, 8, 20, 15, 20]

sce_max = []

for val in numbers2:
    if val < max(numbers2):
        sce_max.append(val)
    
print(sce_max[-1])


# Q3. Find the first duplicate
# Return the first element that appears more than once.

numbers3 = [4, 2, 7, 2, 9, 4]


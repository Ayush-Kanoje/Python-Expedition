# Practice: Python List Basics



# 1. Print the first element

# 2. Print the last element

# 3. Print the length of the list

# 4. Change 30 to 35

# 5. Add 60 to the end

# 6. Remove 20

# 7. Print all elements using a for loop
#            +
# 8. Print all elements with their index

# 9. Find the sum of all elements without using sum()

# 10. Find the largest element without using max()


numbers = [10, 20, 100,30, 40, 50]


print(f"First element: {numbers[0]}, last element: {numbers[-1]}")

print(f"lenght of list: {len(numbers)}")

numbers.insert(2,35)
print(f"replace 30 with 35: {numbers[2]}")

numbers.append(60)
print(f"add 60 at end: {numbers[-1]}")

numbers.pop(1)
print(f"remove 20: {numbers}")


for i in range(len(numbers)):
    value = numbers[i]
    print(i,  value, end="\n")


total = 0
for num_sum in range(len(numbers)):
    total += numbers[num_sum]
print(total)


previous = 0

for maxVal in numbers:
    if maxVal > previous:
        previous = maxVal
    else:
        continue
print(f"max value is {previous}")    



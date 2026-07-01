user_input = int(input("Enter no to calculate sum of that number: "))
sum_even_no = 0
for i in range(1, user_input+1):
    if i%2 == 0:
        sum_even_no += 1

print(f"Sum of even no in {user_input} is: {sum_even_no}")
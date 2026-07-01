#using for loop
user_input = int(input("Enter no to know factorial: "))

result = 1
for i in range(1, user_input+1):
    result = result * i
    
    print(result)

#using while loop
num = 5
fact = 1

while num > 0:
    fact *= num
    num -= 1

print(fact)
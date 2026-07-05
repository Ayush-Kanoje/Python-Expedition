user = int(input("Enter number: "))

for i in range(0, user+1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
user = int(input("Enter number: "))

if user%3 == 0 and user%5 == 0:
    print("FizzBuzz")
elif user%3 == 0:
    print("Fizz")
elif user%5==0:
    print("Buzz")
    
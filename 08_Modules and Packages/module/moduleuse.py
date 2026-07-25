
import modulecode


# print(modulecode.add(a, b))
# print(modulecode.sub(a, b))
# print(modulecode.mul(a, b))
# print(modulecode.div(a, b))
# print(modulecode.div_f(a, b))


choice = input("Do you want to continue? (yes/no): ")

while choice.lower() == "yes":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Divide\n5. Divide with float")
    option = int(input("Enter your choice: "))

    if option == 1:
        print(modulecode.add(a, b))
    elif option == 2:
        print(modulecode.sub(a, b))
    elif option == 3:
        print(modulecode.mul(a, b))
    elif option == 4:
        print(modulecode.div(a, b))
    elif option == 5:
        print(modulecode.div_f(a, b))
    else:
        print("Invalid choice")

   
    
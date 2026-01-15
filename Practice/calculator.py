num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))


print("Please enter your required operation")
print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder")


choice = input("Enter your choice (1/2/3/4/5): ")


if choice == '1':
    print(f"Addition of 2no: {num1+num2}\n")

elif choice == '2':
    print(f"Subtraction of 2no: {num1-num2}\n") 

elif choice == '3':
    print(f"Multiplication of 2no: {num1*num2}")

elif choice == '4':
    print(f"Division of 2no: {num1/num2}") 

elif choice == '5':
    print(f"Reminder of 2no: {num1%num2}")

else:
    print("Invalid choice")   
# num1 = int(input("Enter First No:"))
# num2 = int(input("Enter Second No:"))
# num3 = int(input("Enter Third No:"))


# if(num1>num2 and num1>num3):
#     print("No 1 is greater")

# elif(num2>num1 and num2>num3):
#     print("No 2 is greater")

# elif(num3>num1 and num3>num2):
#     print("No 3 is greater")
# else:
#     print("You have entered wrong no or same no")



#code if user enter duplicate number
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if(num1 == num2 or num1 == num3 or num2 == num3):
    print("You have entered duplicate no")

elif(num1>num2 and num1>num3):
    print(f"First number is greter: {num1}")   

elif(num2>num1 and num2>num3):
        print(f"Second number is greater: {num2}")

else:
    print(f"Third numeber is greater: {num3}")        
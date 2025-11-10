num1 = int(input("Enter First No:"))
num2 = int(input("Enter Second No:"))
num3 = int(input("Enter Third No:"))


if(num1>num2 and num1>num3):
    print("No 1 is greater")

elif(num2>num1 and num2>num3):
    print("No 2 is greater")

elif(num3>num1 and num3>num2):
    print("No 3 is greater")
else:
    print("You have entered wrong no or same no")
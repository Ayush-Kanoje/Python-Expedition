import numbers

user_input = input("Enter number to check their sign: ")

if user_input != numbers:
    print("Enter valid no!")
    if int(user_input) > 0:
        print(f"Positive Number {user_input}")
    elif int(user_input) < 0:
        print(f"Negative Number {user_input}")
    else:
        print(f"You have enter {user_input}")
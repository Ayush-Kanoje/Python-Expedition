user_input = input("Enter your string value: ")

for char in user_input:
    print(char)
    if user_input.count(char) == 1:
        print(f"First non-repeating character is: {char}")
        break  #it will stop all next iteration in loop, when first non-repeating character will be found
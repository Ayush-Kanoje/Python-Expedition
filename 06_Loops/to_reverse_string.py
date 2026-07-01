user_input = str(input("Enter string to make it reverse: "))

for char in user_input:
    reverse_str = char + reverse_str
print(f"{reverse_str}")
#print table of user input no, but skip 5 ittertion

table_number = int(input("Enter table no: "))

for i in range(1,11):
    if i == 5:
        continue #used to skip itteration in loop based on condition
    multi = table_number*i
    print(f"{multi}")
    
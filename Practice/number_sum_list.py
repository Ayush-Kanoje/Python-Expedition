# take number list and calculate sum of all number inside of it

number_list = []
number = int(input("Enter total count of number you have to strore ans sum: "))

for no in range(0,number):
    no = int(input("Enter no: "))
    number_list.append(no)

print(f"{number_list}")

print(sum(number_list))
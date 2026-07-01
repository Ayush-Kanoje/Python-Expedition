year = int(input("Enter Year to check if it is a leap year or not: "))

if(year % 400 == 0):
    print("It is a leap year", year)
elif(year % 100 == 0):
    print("It is a leap year", year)
elif(year % 4 == 0):
    print("It is a leap year", year)
else:
    print("Not a leap year", year)
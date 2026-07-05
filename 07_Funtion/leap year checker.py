def is_leap(year):
    if year%400 ==0:
        print(True)
    elif year%100 == 0:
        print(True)
    elif year%4==0:
        print(True)
    else:
        print(False)

year = int(input())
is_leap(year)
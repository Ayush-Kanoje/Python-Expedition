while True:
    user = int(input("Enter no between 1 to 10: "))
    if user >= 0 and user <= 10:
        print("Access Appovied")
        break
    else:
        print("Access Denied")
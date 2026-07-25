number = int(input("Enter your value: "))

def even_odd_fun(no):
    if(no%2==0):
        print(f"{no} is a EVEN number")
    else:
        print(f"{no} is a ODD number")

even_odd_fun(number)
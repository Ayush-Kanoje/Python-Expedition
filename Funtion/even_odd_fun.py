number = int(input("Enter your value: "))

def even_odd_fun(no):
    if(no%2==0):
        print(f"Even no {no}")
    else:
        print(f"odd no {no}")

even_odd_fun(number)
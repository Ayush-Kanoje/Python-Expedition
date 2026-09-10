# Calculate factorial of N

def fact(num):
    if num == 0:
        return 1

    return num*fact(num-1)


x = fact(5)

print(x)


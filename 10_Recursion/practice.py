
# Head Recursion - its a work first then call funtion recursion
# Beacuse of this it will print value in desending order (based on code)
def printf(n):
    if n == 0:
        return
    print(n)
    printf(n-1)


printf(5)

print("------------------------------------------------------")


# Tail Recursion: Its first call then work recursion type
# Beacuse of this it will print value in asending order (based on code)
def printf(n):
    if n == 0:
        return
    printf(n-1)
    print(n)


printf(5)

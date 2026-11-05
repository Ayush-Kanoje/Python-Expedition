
# Head Recursion - it work first then call funtion recursion
# Beacuse of this it will print value in desending order (based on code)

#print No from 1 to N

def printf(n,i):
    if i > n:
        return

    print(i)
    printf(n,i+1)

printf(i = 1, n = 5)







print("------------------------------------------------------")





# Tail Recursion: It is first call then work recursion type
# Beacuse of this it will print value in asending order (based on code)

#print No from N to 1

def tailR(i,n):
    if i > n:
        return
    tailR(i+1,n)
    print(i)


tailR(i = 1, n = 5)







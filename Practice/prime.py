num_list = [4,5,645,46,486,464,12,34,12,561,112,51,2,37,821,0,2,245640,21]

for prime in num_list:
    if(prime%2 == 0):
        print(f"Prime no {prime}")
        print("----------------------------")

    else:
        print(f"Not a prime {prime}")
        print("----------------------------")
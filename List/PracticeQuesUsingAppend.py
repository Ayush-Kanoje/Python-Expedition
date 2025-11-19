#WAP to ask a user to enter name of their 3 fav movies and store them in list
# solution1 : 
moviesList1 = []

mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")

moviesList1.append(mov1)
moviesList1.append(mov2)
moviesList1.append(mov3)

print(moviesList1)

#solution2 : efficient code
moviesList2 = []

moviesList2.append(input("Enter 1st movie: "))
moviesList2.append(input("Enter 2nd movie: "))
moviesList2.append(input("Enter 3rd movie: "))

print(moviesList2)
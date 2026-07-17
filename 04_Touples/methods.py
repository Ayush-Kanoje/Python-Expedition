#Touples are immutable sequence of value. intialize using -> ()
tup = (1,2,3,4,5,6,1,5,2,1,7,2,1)
print(type(tup))

# 1. While creating tuple of single value we should use , after the value.
# 2. Without , python will treat that variable as a different data type.
# ex-
tup1 = (1) 
print(type(tup1)) # -> int

tup2 = (2.5) 
print(type(tup2)) # -> Float

tup3 = ("hello") 
print(type(tup3)) # -> str

#Correct way to create touples
correctTup = ("ayush",) 
print(type(correctTup))  # -> touple - reason -> ,


# Index Method -  find in which index does value is present
print(tup.index(3))

# Count Method - total occurence of a value inside touple
print(tup.count(2))

# To check if item exit in touple or not -> in

my_tup = (454,645,45,4,54,45,456,6,74,131,)
print(45 in my_tup) # O/P -> True 'if exit'

#to find length
print(len(my_tup))
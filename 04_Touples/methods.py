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
print(type(correctTup))  # -> touple


# Index Method -
print(tup.index(3))

# Count Method - 
print(tup.count(2))

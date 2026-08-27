# # method 1 to create list -> []

a = ["Ayush",21, 3.14, True, 2+3j, None ]

# print(a)

# #crating list with repetative element

num = ["Lovee mee"]*3

# print(num)

#methid 2 -> list constructor, list()
# this method convert data type like dist, str, touple into list data type
tou = (1,2,3,4)
str1 = "ANU"
dist = {
    "age": 21
}

# b = list((tou,"Ayush","kanoje"), tou2) -> wrong because list() can take only one argument

b = list((tou,"Ayush","kanoje",dist,str1))
# print(b)

#accessing value
# print(b[2], b[-3])


#Adding element in list
b.append(65) #added in last
b.insert(-4, bool) #use to add any specific index
b.extend(num) #concat 2 list
print(b)




#Updating value (list are mutable so we can update value by using index)

b[0] = 1*5
# print(b)


#removing element 

# 1. Remove -> first occurnace of a element 
b.remove("Lovee mee")
print(b)


# 2. pop -> remove element from specific index, and if index not provided remove last element
b.pop(-1)
print(b)



list =  "List are mutable"


#1.Append- used to add an item to the end of the list.
myList1 = [1,2,3,4,5,6,7,8,9,10,2,11,2]
myList1.append(3)
print(myList1)

#2 .extend() -> use to concat two list, can be used with set,touples,string
a = ['a','b','c']
b = ['d','e']
a.extend(b)
print(a)

#3.Sort- Arrange values in ascending order.
myList1.sort()
print(myList1)

#To arrange in decending order
myList1.sort(reverse=True)
print(myList1)

#It also work for variable
myList2 = ["anushka", "ayush", "akshad", "parikshita"]
myList2.sort()
print(myList2)

#Reverse- reverse all the value present inside list (does not sort the list)
myList2.reverse()
print(myList2)

#Insert- Used to insert values at any index of a list syntax - .inser(<index_value, <new value>)
myList2.insert(0, "jesus")
print(myList2)

#Remove- remove first occurance of any element
myList1.remove(2)
print(myList1)

#Pop- used to removed values using index position
myList2.pop(2)
print(myList2)
# print value at index 2
print(myList2.pop(2)) 


fruit = ["mango", "banana","apple", "pineapple", 66, 464, "sdf"]

fruit[3] = "chicken"
print(fruit)

#slicing
print(fruit[2:4])








#Declaration of stirng and Concatination (interconnecting two string)
str1 = "Ayush"
str2 = "ayu Kanoje"

# print(str1 + str2)

# print(len(str1)) #To check length of a string

# print(str1[0], str2[1]) #To find which character is present on perticular index of string

#SLICING
# print(str1[0:3], str2[0:5]) #Slicing - retrun combination of a character i.e startingIndexValue : endingIndexValue
# print(str1[0:], str2[4:]) 
# print(str1[-3:-1]) #negavtive slicing start from -1 index
# print(str2[:-1])

#endswith 
# print(str1.endswith("ANU")) #FALSE because str1 dosen't with ANU 
# print(str1.endswith("sh"))  #True 

#capitalize
# print(str1.capitalize())
# str2 = str2.capitalize() #capatilize only first letter
# print(str2)

#replace
# print(str2.replace("y", "n"))
# print(str2.replace("ayu", "anu").capitalize())
# print(str1.replace("A", "a"))

#Find
str3 = "freedom"
print(str3.find("e"))

#Count
print(str3.Count("E"))

#check in or not in
# str3 = "Ayu"
# if(str3 = "Sh")
#     print("Sh" in str3)

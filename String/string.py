#Declaration of string and Concatenation (interconnecting two string)
str1 = "Ayush"
str2 = "ayu Kanoje"

print(str1 + str2)

print(len(str1)) #To check length of a string

print(str1[0], str2[1]) #To find which character is present on which particular index

#SLICING
print(str1[0:3], str2[0:5]) #Slicing - retrun combination of a character i.e startingIndexValue : endingIndexValue
print(str1[0:], str2[4:]) 
print(str1[-3:-1]) #negative slicing start from -1 index
print(str2[:-1])

#endswith 
print(str1.endswith("ANU")) #FALSE because str1 dosen't end with ANU 
print(str1.endswith("sh"))  #True 

#capitalize
print(str1.capitalize()) #capitalize only for
str2 = str2.capitalize() #capitalize only first letter of every word preseny in string
print(str2)

#replace
print(str2.replace("y", "n"))
print(str2.replace("ayu", "anu").capitalize())
print(str1.replace("A", "a"))

#Find
str3 = "freedom"
print(str3.find("e"))

#Count
print(str3.count("E"))

#check in or not in
str4 = "Ayu"
if(str4 == "Sh"):
    print("true")
else:
    print("false")



#Reverse string [::-1]
varInput = input("enter value")

varInput2 = varInput[::-1]

if(varInput2 == varInput):
    print("palimdrome")
else:
    print("not palimdrome")    

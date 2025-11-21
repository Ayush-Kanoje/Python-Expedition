student = {
    "name" : "Ayush kanoje",
    "year"  : "3year, 5sem",
    "subject" : {
        "py" : 95,
        "cpp" : 75,
        "js" : 80,
    },
    "cgpa" : 9.5,
}
print(student)

#1 TO PRINT ALL THE KEY INSIDE OF DICT.
print(student.keys()) #nested dict key:value are not returned
print(student["subject"].keys())

#2 TO PRINT ALL THE VALUES INSIDE OF A DICT
print(student.values())
print(student["subject"].values())

#3 TO FIND LEN OF DICT
print(len(student)) #count inner dict as one key:value
print(len(student["subject"])) #inner dict len

#4 TO TYPE CAST
print(list(student))
print(list(student["subject"]))

#5 .itmes() -> IT RETURN VIEW OF A DICT IN OBJECT CONATINING KEY:VALUE PAIR AS A TOUPLES

print(student.items())

list_cating = list(student.items()) #converting into list
print(list_cating)


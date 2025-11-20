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

#1. TO PRINT ALL THE KEY INSIDE OF DICT.
print(student.keys()) #nested dict key:value are not returned

#2. TO FIND LEN OF DICT
print(len(student)) #count inner dict as one key:value
print(len(student["subject"])) #inner dict len

#3. TO TYPE CAST
print(list(student))


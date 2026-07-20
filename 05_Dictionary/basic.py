#RULES : 1. DISCT DOES NOT ALLOW KEY VALUE PAIR WITH EXISTING KEY NAME
#        2. THEY ARE UNORDERED (key:valyues does not have idx), MUTABLE.

bio = {
    "name" : "Ayush",
    "channel_name": "Pokedexz",
    "bio" : "Hello Dosto, Me hu apka param gyani pokedexz",
    "learning" : ["python", "linux", "aws cloud"],
    "todayTopic" : ("dist","set"),
    "age" : 20,
    "date" : "20/11/2025",
}
print(bio)

#TO GET ALL KEYS FROM DICTIONARY 
print(bio.keys())  #return both key and value
print(bio.items()) #return all values 


#TO ACCESS VALUE INSIDE OF A DICT WE NEED KEY NAME
print(bio["channel_name"], "\n")
print(bio["name"], bio["date"], "\n") #when need to access multiple values
print(bio["learning"], bio["todayTopic"], "\n")


#TO CHANGE,ASSINE OR TO ADD NEW KEY VALUE PAIR. 
bio["name"] = "AYUSH"
print(bio, "\n")


#add new
bio["surname"] = "kanoje"
print(bio, "\n")


#nested Distonary
student = {
    "name" : "Ayush kanoje",
    "subject" : {
        "py" : 95,
        "cpp" : 75,
        "js" : 80,
    },
    "cgpa" : 9.5,
}
print(student)
print(student.keys(), "\n")


#TO PRINT DIST PRESENT INSIDE OR A DICT
print(student["subject"], "\n")


#TO PRINT VALUES PRESENT INSDIDE OF DICT -> DICT
print(student["subject"]["py"], "\n")


#if wee need to search for specific key or value
# student["Add user input variable here without " " quotes"]

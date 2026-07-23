#RULES : 1. DISCT DOES NOT ALLOW KEY WITH EXISTING KEY NAME
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
print(bio["channel_name"])
print(bio["name"], bio["date"]) #when need to access multiple values
print(bio["learning"], bio["todayTopic"])


#TO CHANGE,ASSINE OR TO ADD NEW KEY VALUE PAIR. 
bio["name"] = "AYUSH"
print(bio)


#add new
bio["surname"] = "kanoje"
print(bio)


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
print(student.keys())


#TO PRINT DIST PRESENT INSIDE OR A DICT
print(student["subject"])


#TO PRINT VALUES PRESENT INSDIDE OF DICT -> DICT
print(student["subject"]["py"])


#if wee need to search for specific key or value
student["Add user input variable here without " " quotes"]

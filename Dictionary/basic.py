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


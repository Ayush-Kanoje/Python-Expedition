my_bio = {
    "name" : "Ayush kanoje",
    "age" : 21,
    "college" : "JIT"
}

print(my_bio) 
print(my_bio.get("age"))
print(my_bio.get("name1","NA")) # agar name1 key nhi mile to NA return kr do -> revent keyerror



my_bio.update({"year/sem" : "4th, 7sem"})
print(my_bio)
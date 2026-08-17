#print hello messgae for the person name start with S, present in list

lst = ["Ayush", "Anushka","Aksahd", "Sumit", "Sohil","Sahil","Ishant"]

for name in lst:
    if(name.startswith("S") or name.startswith("s")):
        print(f"hello {name}")
        
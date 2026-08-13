def split_and_join(line):
    return "-".join(line.split(" "))


line1 = "Ayush Kanoje"
print(split_and_join(line1))



def print_full_name(first, last):
    print(f"Hello {first} {last}!, Welcome")


name = "ayush"
last = "kanoje"
print_full_name(name, last)
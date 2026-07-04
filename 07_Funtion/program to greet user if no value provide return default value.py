# Expected output:
# Hello, Welcome Ayush!
# Hello, Welcome User!

def greet(name = "User"):
    return "Hello, Welcome "+ name + "!"


print(greet("Ayush"))
print(greet())

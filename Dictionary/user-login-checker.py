
username = input("Enter you username: ")
password = input("Enter your password: ")

users = {
  
   "Ayush" : "ayush@1234",
   "Anu" : "anu@1234",
   "Munni" : "munni@1234",
   "Aman" : "aman@1234"
}

if username in users:
    if(password != users[username] ):
        print("password is wrong")
    else:
        print("Login Conform")
else:
    print("Wrong username")


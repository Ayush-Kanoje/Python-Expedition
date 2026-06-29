username = input("Enter your username: ")
password = input("Enter password: ")

user = {
    "ayuxh" : "ayush1234",
    "anushka" : "anu1234",
    "akshad" : "nepali1234",
    "parikshita" : "greenflag"
}

def login_fun(username,password):
    if(username in user):
        if(password != user[username]):
            print(f"Wrong password")
        else:
            print(f"Login confrim, Welcome Back {username}")
    else:
        print(f"Wrong username {username}")

login_fun(username,password)
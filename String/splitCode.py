st = "Python language is very high level programming language"

s = st.split()

for word in s:
    if len (word)%2==0:
        print(word)
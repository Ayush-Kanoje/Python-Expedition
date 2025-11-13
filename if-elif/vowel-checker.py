userInput = input("Enter anything i will be check if it is a vowel, number or special character: ")

if(userInput .isalpha()):
    userInput = userInput.lower()
    if(userInput == 'a' or userInput == 'e' or userInput == 'i' or userInput == 'o' or userInput =='u'):
        print("It is a vowel", userInput)
    else:
        print("Its is not a vowel just a alphabet", userInput)  
elif(userInput .isdigit()):
    print("It is a number", userInput)
    
else:
    print("It is a special character:", userInput)

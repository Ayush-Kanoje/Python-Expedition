#to check input vslue is pslimdroneor not
varInput = input("enter value")

varInput2 = varInput[::-1]

if(varInput2 == varInput):
    print("palimdrone")
else:
    print("not palimdrone")    

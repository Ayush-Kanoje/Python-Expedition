#WAP to check if list contain a palindrome of element.
#A palindrome number is a number that reads the same forward and backward.

List1 = [1,2,"abc","abc",2,1]
copyList = List1.copy()
copyList.reverse()

if(copyList == List1):
    print("Palindrome")
else:
    print("Not a palindrome")


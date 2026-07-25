# to find double space from the string
# if not present it return -1

letter = "I Ayush  kanoje  "
print(letter.find("  "))

#replace double space with single space

print(letter.replace("  "," "))


# string are immutable which means even after performing string method it does not change original string value , they create new string
print(letter)

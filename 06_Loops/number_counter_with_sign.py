number_list = [1,-2,-4,6,-46,4,8,48,-61,23,15,-49,49,-44,64,-65,-465,46]
positive_number_counter = 0
negative_number_counter = 0

for num in number_list:
    if num > 0:
        positive_number_counter += 1  
    else:
        negative_number_counter += 1

print(f"Count of positive no are: {positive_number_counter}\nCount of negative no are: {negative_number_counter}")
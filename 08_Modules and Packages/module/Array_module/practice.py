
# In py to use array we need modules: there are two type of module for it - 
# 1.import numpy(best to use) - provide advance numeric opertion funtion
# 2. import array

# Example using import array

import array
val1 = array.array('i',[1,2,3,4,5,3,23,2,2]) # 'i' is typecode
for i in range(0,5): 
    # print(val2[i])
    print(val1[i], end=' ')

print(val1)
print("\n")


import array as arr
val2 = arr.array('b', [4,5,6,4,64,46,1])
print(val2)
for i in range(0,len(val2)): #to print array value, not dynamic but to make it we can do - range(0,len(val2))
    print(f"value of array 2: {val2[i,]}",end={','})
print("\n")


from array import *
val3 = array('I',[1,2,1,4,5,9])
print(val3)
for x in val3: 
    #1. using this format we dont need to define index like in above for loop
    #2. used when array size change dynamically
    print(x, end=',')




    
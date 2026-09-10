# Find the sum of all elements in an array

# Input: [2, 4, 6, 8]
# Output: 20


num_list = [2, 4, 6, 8]


def listSum(num, index = 0):

    if index == len(num):
        return 0

    return num[index] + listSum(num , index+1)

x = listSum(num_list)

print(x)
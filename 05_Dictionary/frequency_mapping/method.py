num = [1,5,56,2,15,6,1,3,4,6,8,7,8,7,9,2,1,5,78,6,4,3]

freq_map = dict()

for idx, val in enumerate(num) : #TC - O(N)
    if val in freq_map:  #TC - O(N)
        freq_map[val] += 1
    else:           #TC - O(N)
        freq_map[val] = 1
print(freq_map)


#TC - O(N)
#SC - O(N)
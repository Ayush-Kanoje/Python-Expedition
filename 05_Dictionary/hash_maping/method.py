num = [1,5,56,2,15,6,1,3,4,6,8,7,8,7,9,2,1,5,78,6,4,3]

hash_map = dict()

for i in range(0,len(num)): #TC - O(N)
    hash_map[num[i]] = hash_map.get(num[i],0) + 1 #TC - O(1)

print(hash_map)

#TC - O(N)
#TC - O(N)
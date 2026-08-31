# Q7. Two Sum — Easy 
# Find two numbers whose sum equals target and return their indices.

num = [5,9,8,7,5,5,4,8]

target = 12

seen = {}

for idx,val in enumerate(num):
    total = target - val 
    if total in seen:
        print(idx,seen[total])
        break
    else:
        seen[val] = idx



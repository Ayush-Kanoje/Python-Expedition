# itertools is a built-in Python module that provides fast, memory-efficient tools for looping through and combining data (like lists).

# When it is used
# It is used when you need to:

# Process very large amounts of data without running out of memory.
# Combine multiple lists, generate repeating sequences, or count infinitely.
# Find complex combinations or permutations of items easily.


import itertools as it

l1 = [1,2,3,4,'a','sd','e']
l2 = [1,2,3,4,5,'s','d','g']

a1 = "ayush"
b2 = "kanoje"
print(it.chain(a1,b2))
print(list(it.chain(a1,b2)))
print(list(it.chain(l1,l2)))

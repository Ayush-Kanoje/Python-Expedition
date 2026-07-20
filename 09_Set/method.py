# Set
# 1. No duplicates — automatically removes repeated values
# 2. Unordered — elements have no defined position, no indexing
# 3. Mutable — you can add/remove elements (but frozenset is the immutable version)
# 4. Elements must be immutable — strings, numbers, tuples allowed; lists/dicts not
# 5. Based on hashing — in check is O(1), much faster than a list
# 6. Supports math operations — union |, intersection &, difference -, symmetric difference ^


s = {1,2,3,4, "Ayush"} #dict and set both use {}

# set = {} -> dont use this method to create set, it will create dict not a set

#TO CREATE EMPTY SET
Set_variable_name = set()

#add
s.add(556)
print(s)

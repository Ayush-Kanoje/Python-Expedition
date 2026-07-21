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

#.add() -> Add one value at a time
s.add("Apple")
s.add("Banana")
print(s)

Set_variable_name.add("Me hu apka param Gyani")
Set_variable_name.add("Ayush")
Set_variable_name.add(1)
Set_variable_name.add("ayush")
print(Set_variable_name)


#.remove() -> Remove one value at time
s.remove("Banana")
print(s)


# .discard() -> Remove value : if exist, if not - return nothing (prevent keyerror)
s.discard("Apple")
s.discard("dcsdfsfs")
print(s)


# .union -> combine two set
set1 = {5455,4546,454,6456}
result = Set_variable_name.union(s,set1)
print(result)


# .intersection -> return same value present in one or more set
print(Set_variable_name.union(s,set1))
print(s.intersection(set1,Set_variable_name))

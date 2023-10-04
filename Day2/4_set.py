# Set Data Types
''' Set is an unordered data types. 
It helps to remove duplications. 
It cannot be accessed using index'''

set = {1,2,3,4,5,6,7,8,9,10,3,7}
print(set, type(set))

# add one item to the set
set.add("Samundra")
print(set)
# print(set[4]) # cant be accessed using index

# to access the items of a set
for x in set:
    print(x)

# add items from another set to current set
set1 = {"Samu","Sandesh"}
set2 = {"Kripa","Sharada"}
set1.update(set2) # from set2 into set1
print(set1)

# to remove an item we can use remove() or discard()
set1.remove("Sandesh")
print(set1)

# to remove last element
set1.pop()
print(set1)

# empties the set
set.clear()
print(set)

# to delete the set completely
# del set1
# print(set1)
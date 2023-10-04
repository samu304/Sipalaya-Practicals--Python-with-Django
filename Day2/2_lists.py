# Sequence Data Types
''' List, Set, Tuples, Dictionary'''

# List Data Types
data = [23,"Samundra",45.6,'Sipalaya']
print(data)
print(type(data))
print(data[1]) # From Beginning
print(data[-1]) # From last

#update the list
# add one item at the end of the list
data.append("Python")
print(data)

# add multiple elements to the end (add by making list)
data.extend([100,True,"Django"])
print(data)

# Insert at the specified index of the list
data.insert(4,"Hey There")
print(data)

# update the data of certain index
data[2] = 9.03
print(data)

# removes the specified index item
data.remove(1)
print(data)

# delete a single data from the list
del data[3]
print(data)

# delete the entire list
# del data
# print(data)

# retrieve the last item from a list and delete it
print(data.pop())
print(data)


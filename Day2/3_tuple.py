# tuples data Types
tup = (1,23,45,66,79,100)
print(tup,type(tup))
print(tup[2])

# tup[2] = 'Samundra' # not possible to modify the items
print(len(tup)) # number of items in the tuple

one = (4,) # tuple with only one item
empty = () # empty tuple
print(one, empty)

print(tup + one) # joining two tuples

# del one # deletes an emtire tuple
# print(one)

t = (1,2,3,4,5,3,5,6,2,6,3,2,2,3)
print(t.count(3)) # number of times a specified value occurs

print(t.index(3)) # returns the index/porition of item after searching it
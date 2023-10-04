# Dictionary Data Types

#create a dictionary 
data ={
    "name" : "Samundra",
    "age" : 22,
    "phone" : 9845988304
}
print(data, type(data))

# adding a new key:value to the dictionary
data["year"] = 2000
print(data)

# update a dictionary
data["phone"] = 9845097669
print(data)

# access values in a dictionary
print(data['name']) 
print(data.get("abcd","Sorry not found")) # "abcd" find garena vani "Sorry not found" dekhauxa

# returns list of all keys
print(data.keys())

# returns list of all values
print(data.values())

# to return the key value pair in form of a tuple
print(data.items())

# delete items from a dictionary

data.pop("year") # del data["year"] # removes item with specified key names
print(data)

data.popitem() # removes the last item
print(data)

data.clear() # empties the dictionary
print(data)

# del data # removes the dictionary completely
# print(data)

# copy a dictionary into another
data1 = data.copy()
print(data)
print(data1)

d = {
    101: "code",
    "name": "Sipalaya",
    "courses": ["Python","MERN","React"]
}
print(d["courses"][2][0]) # returns R
d["courses"].append("Java")  # adds to the end of the courses
print(d)
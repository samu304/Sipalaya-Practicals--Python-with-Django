# 8. Write a Python function that takes a dictionary as input and returns a new dictionary where the keys are sorted alphabetically and the values are sorted in descending order.


marks = {
    "english" : 45,
    "maths" : 90,
    "science" : 84,
    "nepali" : 66,
    "social" : 86,
    "health" : 73,
    "computer" : 95
}

def sort_key(a):
    k = list(a.keys()) # extracts the keys from the dictionary in form of a list
    n = len(k)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if k[j] > k[j + 1]: # ascending order
                k[j],k[j + 1] = k[j + 1],k[j]
    return k

key = sort_key(marks)
print(key) # prints the list of keys in ascending order

def sort_value(b):
    v = list(b.values())  # extracts the values from the dictionary in form of a list
    n = len(v)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if v[j] < v[j + 1]: # desscending order
                v[j],v[j + 1] = v[j + 1],v[j]
    return v

val = sort_value(marks)
print(val) # prints the list of values in descending order

result = zip(key,val)
print(dict(result))


# def sorting(d):
#     sorted_keys = sorted(d.keys())
#     sorted_value = sorted(d.values(),reverse = True)
#     sorted_dict = dict(zip(sorted_keys,sorted_value))
#     return sorted_dict

# result = sorting(marks)
# print(result)

# for key,value in result.items():
#     print(key,value)
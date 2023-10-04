# Exercise related to the loops

# Program to find sum of given numbers in a list

""" 
list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for num in list:
    sum = sum + num
print(sum) """


# Program to add the strings into the dictionary in the form of : ('alphabet': 'number of occurance')
""" 
string = "aeayfejafaevjvvavhvvavhfvheva"
output = {}
for char in string:
    if char in output:
        output[char] += 1
    else:
        output[char] = 1
print(output) """

# program to sort the given numbers in ascending order (<), For descending (>)

num = [1,5,89,34,25,4,14,]
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] > num[j]:
            num[i],num[j] = num[j],num[i]
print(num)

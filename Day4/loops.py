# For Loop in Python
# (We use for loop in those condition when how many times to repeat the loop is already known)
'''
for var_name in sequence:
    for loops body

range() function
range(start, end, step)

range(10) -- 0,1,2,3,....,9
range(3,8) -- 3,4,5,6,7
range(10,40,5) -- 10,15,20,25,30,35

'''

# print numbers from 1 to 50 
""" for num in range(1,51):
    print(num) """

# print even numbers from 10 to 100
""" for i in range(10,100):
    if i % 2 == 0:
        print(i)
 """

# print the characters in a string
""" for char in "Samundra":
    print(char) """

# print the elements of a list
""" numbers = [12,True,45.5,"Sipalaya",None,False]
for char in numbers:
    print(char) """

# Nested For Loops in Python
""" for i in range(4):
    for j in range(3):
        print(i,j) """

""" num1 = [2,4,6,8]
num2 = [1,3,5]
for i in num1:
    for j in num2:
        print(i,j) """

# Program to reverse the given string
""" string = input("Enter any String: ")
reverse = ""

for char in string:
    reverse = char + reverse
print("The reversed string is :" + reverse) """


# While loops in Python 
# (We use for loop in those condition when how many times to repeat the loop is not known)

# Comparing for and while loops
""" 
for i in range(10):
    print("Samundra")

i = 0
while i < 10:
    print("Khanal")
    i = i+1 """

# the break statement (come out of the loop)
for i in range(10):
    print(i)
    if i == 6:
        break

# the continue statement (stops the current iteration and starts with the new one)
for i in range(10):
    if i == 6:
        continue
    print(i)

# the pass statement (it just skips the block and does nothing)
for i in range(10):
    pass
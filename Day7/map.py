# map() function in python
# map(function,iterable)


# to square the elements
num = [1,2,3,4,5]
square = map(lambda a: a**2,num)
print(list(square))

# to change characters to uppercase
name = ["samu","sanu","sandesh","ram"]
result = map(str.upper,name)
print(list(result))

# using the round and range function
area = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
rounded = map(round, area,range(1,7))
print(list(rounded))

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
out = map(lambda a : round(a ** 2,3), my_floats)
print(list(out))
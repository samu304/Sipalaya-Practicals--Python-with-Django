# reduce() function in python
# the reduce has to be imported from the functools module
# reduce(function, iterable)

from functools import reduce

# adding the numbers
num = [1,2,3,4,5]
sum = reduce(lambda a,b: a + b, num)
print(sum)

# using initial value
num1 = [1,2,3,4,5]
def sum(a,b):
    return a + b
add = reduce(sum, num1, 10) # adding starts from 10
print(add)

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
product = reduce(lambda a,b: a * b, my_numbers)
print(product)
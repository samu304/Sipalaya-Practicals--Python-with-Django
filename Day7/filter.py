# filter() function in python
# filter(function, iterable)

# to filter out even numbers
""" 
nums = [23,56,33,89,46,21,93]
def oddeven():
    for i in nums:
        if i % 2 == 0:
            print(f"{i} is Even Number")
        else:
            print(f"{i} is Odd number")
output = filter(oddeven(),nums)
print(output) """

# to filter out palindrome numbers from a list of strings

strings = ["samundra","madam","khanal","racecar","wow","php","rewire"]
palindrome = filter(lambda word: word == word[::-1], strings)
print(list(palindrome))

# filter out marks greater than 80
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
first = filter(lambda a : a >= 80, scores)
print(list(first))


# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
name = filter(lambda word: len(word) <= 7, my_names)
print(list(name))
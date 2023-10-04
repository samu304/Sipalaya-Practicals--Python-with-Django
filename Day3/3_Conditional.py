# Conditional Statements 
# (if, if-else, if-elif-else)

'''
num = int(input("Enter any number:"))
if num > 20:
    print(f"{num} is greater than 20")
else:
    print(f"{num} is less than 20")

# A program to find the Greatest of 3 numbers

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

if a > b and a > c:
    print(f"The greatest Number is {a}")
elif b > a and b > c:
    print(f"The greatest number is {b}")
else:
    print(f"The greatest number is {c}")
'''
# Nested-If Conditional

x = 34
if x > 20:
    print("Above 20")
    if x > 40:
        print(f"{x} is above 40 as well")
    else:
        print(f"{x} is above 20 but less than 40")
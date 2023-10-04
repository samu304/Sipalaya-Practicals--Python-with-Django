# exception handling in python

try: 
    number = int(input("Enter any  number:")) 
    print(number)
except ValueError as v:
    print("Please enter a right format ")
else:
    print("This statment is executed when no error occurs")
finally:
    print("Immediately executed after exception handling")

# Functions in Python
'''
def func_name(formal argument): # function definition
    function body
funnc_name(actual argument) # function call
'''

# concept 1
""" 
def show():
    a = 12
    b = 64
    print(a + b)

show() """

# concept 2
""" 
def add(num1,num2):
    print(num1 + num2)

add(12,64) # 76
add(12) # missing one argument error
add(12,45,65) # Takes 3 but 3 were given """

# concept 3
""" 
def add(n1,n2=10):
    print(n1 + n2)
add(20) # 30
add(20,30) # 50 """

# concept 4
""" 
def add(*num): # takes all the values as a tuple
    print(num)
    sum = 0
    for i in num:
        sum += i
    print(f"The total sum is {sum}")
add(1,34,54,24,15) """

# concept 5
""" 
def details(**data): # takes inputs in the form of key:value pair(dictionary)
    print(data['age'])
    for key,value in data.items():
        print(f"{key} : {value}")

details(age = 22, name = "Sipalaya", phone = 9845988304) """

# concept 6
""" 
def details(name,age):
    print("Name is : ",name)
    print("Age is :",age)
details("Samundra",22)
details(34,"samu")  """

# concept 7
""" 
def details(name,age):
    print("Name is: ",name)
    print("Age is: ",age)
details(age = 22, name = "Samundra") """

# concept 8
""" 
def add(n1,*n2):
    print(n1)
    print(n2)
    print(n2[2])
    sum = 0
    for i in n2:
        sum += i
    print("The sum of numbers in n2 is ",sum)

add(12,4,15,6,32,2,7,45) """

# program to find factorial of a number
""" 
def fact(num):
    f = 1
    for i in range(1,num + 1):
        f = f*i
    print(f"The factorial of {num} is {f}")

num = int(input("Enter any number:"))
fact(num) """

# concept of enumerate function
""" 
nums = [1,2,3,4,5,6,7,8]
for count,num in enumerate(nums,11): 
    print(count,num) """

""" 
mbluser={
    'jeevan':{'key':1234,'group':"Admin",'balance':25000},
    'ram':{'key':2345,'group':"Admin",'balance':15000}
}
print(mbluser['jeevan']['key']) """
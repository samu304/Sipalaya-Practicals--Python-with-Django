# Operators in Python
'''
# Arithmetic Operators (+,-,/,*,//,**,%,+=,-=)
print(50 + 5) # 55
print(50 - 5) # 45
print(50 * 5) # 250
print(5 ** 3) # 125
print(50 / 5) # 10.0
print(53 // 5) # 10
print(50 % 4) # 2

# Relational Operators (<,>,<=,>=)
print(34 > 89) 
print(34 <= 89) 
print(34 >= 89) 
print(34 < 89) 

# Logical Operators (and, or, not)
print(2 > 1 and 45 < 34 and 56 > 89) # False
print(2 > 1 or 45 < 34 or 56 > 89) # True
print(not True) # False
'''


# Membership Operators (in, not in)
friend = ["Samundra","Sandesh","Kripa","Sharada","Shanta","Narayan"]
print("Kripa" in friend) # True
print("Kripa" not in friend) # False
print("Samu" not in friend) # True

dict = {"a" : 1, "b" : 2, "c" : 3}
print('a' in dict) # True

name = "Samundra Khanal"
print('a' in name) # True
print('dra' in name) # True
print('unda' in name) # unda sanai hunu parxaa True auna laai


# Identity Operator ( is, is not)
# if two objwcts locations are same then it returns true
num1 = 23
num2 = 23
print(num1 is num2) # True 
print(id(num1), id(num2)) 

num1 = '23'
num2 = 23
print(num1 is num2) # False 
print(id(num1), id(num2)) 
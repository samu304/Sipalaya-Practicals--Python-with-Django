# Single Inheritance in Python
""" 
class Parent:
    def __init__(self):
        print("Parent class init method called")
    def show(self):
        print("Parent class show method")

class Son (Parent):
    def __init__(self):
        print("Son class init method called")
samu = Son()
samu.show() """


# Multilevel Inheritance in Python
""" 
class Parent:
    def __init__(self):
        print("Parent class init method")
    def show(self):
        print("Parent clas show method")

class Son (Parent):
    def __init__(self):
        print("Child Class init method")

class GrandSon (Son):
    def __init__(self):
        print("GrandSon class init method")

samu = GrandSon()
samu.show() """

# Multiple Inheritance in Python
""" 
class Father:
    money = 2000
    def __init__(self):
        print("Father init method")
    def show(self):
        print("Father Show Method")

class Mother:
    money = 5000
    def __init__(self):
        print("Mother init method")
    def show(self):
        print("Mother Show Method")

class Son (Mother,Father):
    def __init__(self):
        print("Son class init method")

s1 = Son()
s1.show() """


# Decorators in python
""" 
def show():
    print("Outer Function")
    def result():
        print("Inner Function")
    return result

result = show()
result() """


def Animal(func): # using func we pass the Bird function as an argument
    print("Animal Function")
    def wild():
        print("Wild Animals Function")
        print("Additional Features")
        func() # calling the Bird() function
    return wild

@Animal # Decorator Function here
def Bird():
    print("Bird Function")

Bird()

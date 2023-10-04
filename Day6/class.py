# Class in Python

class Employee:
    def __init__(self,id,name,depart,address):
        self.id = id
        self.name = name
        self.depart = depart
        self.address = address

    def display_info(self):
        print("Employee id is: ",self.id)
        print("Employee name is: ",self.name)
        print("Employee Works in: ",self.depart)
        print("Employee lives is: ",self.address)

first = Employee(101,"Samundra","Python","Chitwan")
first.display_info()
first.name

class Vehicle:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def display(self):
        print(self.model,self.color)

class Bus (Vehicle):
    def __init__(self,model,color,wheel):
        self.wheel = wheel
        Vehicle.__init__(self,model,color)
        
    def show(self):
        print(self.model,self.color,self.wheel)

b1 = Bus("Volvo V1","white",4)
b1.show()

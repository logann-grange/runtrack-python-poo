class Operation() :
    def __init__(self) :
        self.nombre1 = 10
        self.nombre2 = 1
    
    def addition(self):
        print(f"{self.nombre1} + {self.nombre2} = {self.nombre1 + self.nombre2}")


op = Operation()
op.addition()
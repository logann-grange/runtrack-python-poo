from job04 import Forme, Rectangle

class Cercle(Forme) :

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def aire(self) :
        return self.radius**2*3.14
    
rect = Rectangle(10, 5)
cercle = Cercle(10)

print(rect.aire())
print(cercle.aire())
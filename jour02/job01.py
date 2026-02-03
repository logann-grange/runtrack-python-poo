class Rectangle() :
    def __init__(self, longueur, largeur) :
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self) :
        return self.__longueur
    
    def get_largeur(self) :
        return self.__largeur
    
    def set_longueur(self, l) :
        self.__longueur = l

    def set_largeur(self, L) :
        self.__largeur = L

rect = Rectangle(10, 5)
rect.set_longueur(20)
rect.set_largeur(10)
print(f"Rectangle de longueur {rect.get_longueur()} et de largeur {rect.get_largeur()}")
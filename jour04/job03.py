class Rectangle() :
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self) :
        return (self.__longueur+self.__largeur)*2
    
    def surface(self) :
        return self.__largeur*self.__longueur
    
    def get_largeur(self) :
        return self.__largeur
    
    def get_longueur(self) :
        return self.__longueur
    
    def set_largeur(self, largeur) :
        self.__largeur = largeur

    def set_longueur(self, longueur) :
        self.__longueur = longueur

class Parrallelepipede(Rectangle) :

    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self) :
        return self.hauteur*self.get_largeur()*self.get_longueur()
    

rect = Rectangle(5, 10)
para = Parrallelepipede(5, 10, 4)
print("Périmètre :",rect.perimetre())
print("Surface :", rect.surface())
print("Volume :", para.volume())


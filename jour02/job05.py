class Voiture() :
    def __init__(self, marque, modele, annee, km, reservoir) :
        self.__marque = marque
        self.__modele = modele
        self.__annee =  annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = reservoir

    def get_marque(self) :
        return self.__marque
    
    def get_modele(self) :
        return self.__modele
    
    def get_annee(self) :
        return self.__annee
    
    def get_km(self) :
        return self.__km
    
    def get_en_marche(self) :
        return self.__en_marche
    
    def get_reservoir(self) :
        return self.__reservoir
    
    def set_marque(self, marque) :
        self.__marque = marque

    def set_modele(self, modele) :
        self.modele = modele

    def set_annee(self, annee) :
        self.__annee = annee

    def set_km(self, km) :
        self.__marque = km
    
    def set_en_marche(self, marche) :
        self.__en_marche = marche

    def set_reservoir(self, reservoir) :
        self.__reservoir = reservoir

    def demarrer(self) :
        if self.get_reservoir() > 5:
            self.__en_marche = True

    def arreter(self) :
        self.__en_marche = False


vroom = Voiture("Renault", "Twingo", 2003, 275000, 5.1)

vroom.demarrer()
if vroom.get_en_marche:
    print("Vroom !!!")
else :
    print("Brrrr")




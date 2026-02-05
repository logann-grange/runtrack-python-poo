class Vehicule() :

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def info_vehicule(self) :
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}")
    
    def demarrer(self) :
        print("Attention je roule !!!")

    
class Voiture(Vehicule) :

    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def info_vehicule(self) :
        print(f"\nMarque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\nNombre de portes : {self.portes}\n")

    def demarrer(self):
        print("Vrooooom !!!")

class Moto(Vehicule) :

    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def info_vehicule(self) :
        print(f"\nMarque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\nNombre de roue : {self.roue}\n")

    def demarrer(self):
        print("Vroom vroom !")

voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.info_vehicule()
voiture.demarrer()

moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.info_vehicule()
moto.demarrer()
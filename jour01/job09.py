class Produit() :
    def __init__(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = prixHT*0.2
    
    def CalculerPrixTTC(self) :
        return self.prixHT+self.TVA
    
    def afficher(self) :
        return[self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC()]
    
    def changerNom(self, nom):
        self.nom = nom

    def changerPrix(self, prix) :
        self.prixHT = prix

    def afficherNom(self) :
        return self.nom
        
    def afficherPrixHT(self) :
        return self.prixHT
    
    def afficherTVA(self) :
        return self.TVA

#======== JOB 9 ========#
prod1 = Produit("produit1", 3)
prod2 = Produit("produit2", 11)
print(prod1.afficher())
print(prod2.afficher())
prod2.changerNom("produit3")
prod2.changerPrix(2)
print(prod1.afficher())
prod2.changerNom("produit4")
prod2.changerPrix(9)
print(prod2.afficher())

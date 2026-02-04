class CompteBancaire() :

    def __init__(self, ID, nom, prenom, solde, decouvert) :
        self.__ID = ID
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = decouvert

    def get_nom(self) :
        return self.__nom
    
    def get_prenom(self) :
        return self.__prenom
    
    def get_solde(self) :
        return self.__solde

    def set_solde(self, val) :
        self.__solde = val

    def afficher(self) :
        print(f"ID : {self.__ID}\nnom : {self.__prenom} {self.__nom}\nsolde : {self.__solde}\n")

    def afficher_solde(self) :
        print(f"Solde de {self.__prenom} {self.__nom} : {self.__solde}")

    def versement(self, val) :
        self.__solde += val
        self.afficher_solde()

    def retrait(self, val) :
        if self.__solde - val > 0 or self.decouvert: 
            self.__solde -= val
            self.afficher_solde()
        else :
            print("retrait impossible, vous êtes trop PAUVRE !")

    def virement(self, compte, montant) :
        if self.__solde - montant > 0 or self.decouvert :
            self.__solde -= montant
            compte.set_solde(compte.get_solde() + montant)
            print(f"Votre virement de {montant} à bien été envoyé à {compte.get_prenom()} {compte.get_nom()}\n")
        
    def agios(self, val) :
        if self.solde < 0 :
            self.__solde += val


compte = CompteBancaire(666, "Némar", "Jean", 1000000, False)
compte2 = CompteBancaire(897, "Perlimpinpin", 'Emanuel', -100, True)
compte.afficher()
compte.versement(1000)
compte.retrait(200000)
compte.virement(compte2, 100)
compte2.afficher()

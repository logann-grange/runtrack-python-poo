class Commande() :

    def __init__(self, num, list_plats:dict, statut) :
        self.__num = num
        self.__list_plats = list_plats
        self.__status = statut

    def add_plats(self, plat, prix) :
        self.__list_plats[plat] = prix

    def annule_commande(self) :
        self.__status = "annulée"

    def afficher_prix(self) :
        prix_total = 0
        tva_total = 0
        for plat, prix in self.__list_plats.items() :
            prix_total += prix
            tva_total += self.calcul_tva(plat)
            print(f"{plat} : {self.__list_plats[plat]}€    TVA : {self.calcul_tva(plat)}")
        print(f"total : {prix_total}€    TVA : {tva_total}")

    def calcul_tva(self, plat) :
        return self.__list_plats[plat] * 0.2


list_plat = {"Pâtes" : 8.8 , "Pizza" : 9.5, "Tacos" : 9.7}
commande = Commande(29, list_plat, "en cours")
commande.add_plats("Entrecôte", 16.5)
commande.afficher_prix()
class Commande() :

    def __init__(self, num, list_plats:dict, statut) :
        self.__num = num
        self.__list_plats = list_plats
        self.__status = statut

    def add_plats(self, plat, prix) :
        self.list_plats["plat"].append(plat)
        self.__list_plats["prix"].append(prix)

    def annule_commande(self) :
        self.__status = "annulée"

    def afficher_prix(self) :
        prix_total = 0
        tva_total = 0
        for i in range(len(self.__list_plats["prix"])) :
            prix_total += self.__list_plats["prix"][i]
            tva_total += self.calcul_tva(i)
            print(f"{self.__list_plats['plat'][i]} : {self.__list_plats['prix'][i]}€    TVA : {self.calcul_tva(i)}")
        print(f"total : {prix_total}€    TVA : {tva_total}")

    def calcul_tva(self, index) :
        return self.__list_plats['prix'][index] * 0.2


        



list_plat = ["Pâtes", "Pizza", "Tacos"]
list_prix = [9.5, 7.6, 9.7]
dict_commande = {
    "plat" : list_plat,
    "prix" : list_prix
}

commande = Commande(29, dict_commande, "en cours")   
commande.afficher_prix()
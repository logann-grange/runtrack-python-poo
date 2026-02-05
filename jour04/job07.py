from random import randint
import time

class Carte() :
    
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def return_carte(self) :
        match self.valeur :
            case 100 :
                return 'as'
            case 13 :
                return "roi"
            case 12 :
                return "dame"
            case 11 :
                return "vallet"
        return str(self.valeur)


class Jeu() :

    def __init__(self):
        self.tour = 0
        self.cartes_joueur = []
        self.cartes_croupier = []
        self.paquet = []
        self.point_joueur = 0
        self.point_croupier = 0

    def piocher(self, joueur) :
        carte = self.paquet[randint(0, len(self.paquet)-1)]
        if joueur : 
            self.cartes_joueur.append(carte)
        else : 
            self.cartes_croupier.append(carte)
        self.paquet.remove(carte)

    def compte_points(self, joueur) :
        if joueur :
            list_carte = self.cartes_joueur
        else :
            list_carte = self.cartes_croupier

        cumul = 0
        nb_as = 0
        for carte in list_carte :
            if carte.valeur == 100 :#si as
                nb_as +=1
            else :
                cumul += carte.valeur
        cumul_plus_as = cumul
        # attribut la valeur de l'as (1 ou 100)
        for a in range(nb_as) :
            if cumul_plus_as + 11 + nb_as-1 > 21 :
                cumul += 1
            else :
                cumul += 11
        
        if joueur :
            self.point_joueur = cumul
        else : 
            self.point_croupier = cumul

    def verif_fin(self) :
        if self.point_joueur > 21 or (self.point_croupier > self.point_joueur and self.point_croupier <= 21) :
            print("Vous avez PERDU !")
        else : 
            print("Vous avez gagné !")
    
    def reset_paquet(self) :
        list_valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100]
        list_couleur = ["coeur", "carreau", "pique", "trefle"]

        for valeur in list_valeur :
            for couleur in list_couleur :
                self.paquet.append(Carte(valeur, couleur))
    
    def lancer_jeu(self) :
        self.reset_paquet()

        for i in range(2) :
            self.piocher(True) #joueur
            self.piocher(False) #croupier

    def afficher_cartes(self) :
        carte_croupier = "Croupier : "
        carte_joueur = "Joueur : "
        for carte in self.cartes_croupier :
            carte_croupier += carte.return_carte() + ","

        for carte in self.cartes_joueur :
            carte_joueur += carte.return_carte() + ","
        
        print(carte_croupier)
        print(carte_joueur, "\n")   


jeu = Jeu()
jeu.lancer_jeu()
jeu.afficher_cartes()
fini = False
tour_joueur = True

while not fini :
    jeu.compte_points(True)
    jeu.compte_points(False)

    if jeu.point_joueur < 21 and jeu.point_croupier < 21 :
    
        if tour_joueur :
            if jeu.point_joueur >= 21 :
                fini = True
            else :
                piocher = input("Voulez vous piocher (oui/non) : ")
                if piocher == "oui" :
                    jeu.piocher(True)
                    jeu.afficher_cartes()
                    time.sleep(1)
            tour_joueur = False
        else :
            if jeu.point_croupier < 17 :
                print("Le croupier pioche...")
                jeu.piocher(False)
                tour_joueur = True
                jeu.afficher_cartes()
                time.sleep(1)
            else :
                fini = True
    else : fini = True
    

jeu.verif_fin()

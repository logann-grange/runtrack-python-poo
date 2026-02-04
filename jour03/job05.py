import time
from random import randint

class Personnage() :
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def soin(self) :
        print(f"{self.nom} se soigne !")
        self.vie += 60

    def attaquer(self, ennemi):
        print(f"{self.nom} attaque !")
        if ennemi.vie > 20 :
            ennemi.vie -= 20
        else :
            ennemi.vie = 0

    def action(self, action, ennemi) :
        if action == "a" :
            self.attaquer(ennemi)
        elif action == "s" :
            self.soin()

    
class Jeu() :

    niveau : int
    joueur : Personnage
    ennemi : Personnage

    def choisir_niveau(self) :
        self.niveau = input("Entrez le niveau de difficulté : ")

    def lancer_jeu(self) :
        nom_j = "Joueur"
        vie_j = 0
        nom_e = "Ennemi"
        vie_e = 0
        
        match self.niveau :
            case "Facile" :
                vie_j = 200
                vie_e = 50
            case "Normal" :
                vie_j = 100
                vie_e = 100
            case "Difficile" :
                vie_j = 75
                vie_e = 125
            case _ :
                print("Mauvaise saisie")

        self.joueur = Personnage(nom_j, vie_j)
        self.ennemi = Personnage(nom_e, vie_e)
            

    def verif_fin(self) :
        if self.joueur.vie <= 0 :
            print("Vous avez perdu !")
            return True
        elif self.ennemi.vie <= 0 :
            print("Vous avez gagné !")
            return True
        return False

    def afficher_vie(self) :
        print(f"Joueur : {self.joueur.vie}        Ennemi : {self.ennemi.vie}")


jeu = Jeu()
jeu.choisir_niveau()
jeu.lancer_jeu()
tour_joueur = True
list_action = ["a", "a", "a", "s"]

while not jeu.verif_fin() :
            time.sleep(1)
            if tour_joueur :
                jeu.joueur.action(input("Votre tour :\na : attaquer    |   s : se soigner --> "), jeu.ennemi)
                tour_joueur = False
            else :
                #print("L'ennemi attaque !")
                time.sleep(1)
                jeu.ennemi.action(list_action[randint(0, 3)], jeu.joueur)
                #jeu.ennemi.attaquer(jeu.joueur)
                tour_joueur = True
            jeu.afficher_vie()

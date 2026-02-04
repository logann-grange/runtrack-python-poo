class Joueur() :
    def __init__(self, nom, num, pos, but, passe_d, cart_jaune, cart_rouge) :
        self.nom =nom
        self.num = num
        self.pos =  pos
        self.but = but
        self.passe_d = passe_d
        self.cart_jaune = cart_jaune
        self.cart_rouge = cart_rouge

    def marquer_but(self) :
        self.but += 1

    def effectuer_passe_d(self) :
        self.passe_d += 1

    def recevoir_cart_jaune(self) :
        self.cart_jaune += 1

    def recevoir_cart_rouge(self) :
        self.cart_rouge += 1

    def afficher_stats(self) :
        print(f"{self.nom}\nnuméro : {self.num}\nposition : {self.pos}\nbut : {self.but}\npasse décisives : {self.passe_d}\ncarton jaune : {self.cart_jaune}\ncarton rouge : {self.cart_rouge}")

class Equipe() :
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur) :
        self.joueurs.append(joueur)

    def afficher_stats_joueurs(self) :
        print(self.nom)
        for joueur in self.joueurs :
            joueur.afficher_stats()
            print("\n")

    def mettre_a_jour_stats_joueur(self, joueur, but, passe_d, cart_jaune, cart_rouge) :
        for j in self.joueurs :
            if j == joueur :
                j.but = but
                j.pass_d = passe_d
                j.cart_jaune = cart_jaune
                j.carte_rouge = cart_rouge
            pass

e1 = Equipe("Equipe 1")
j1 = Joueur("j1", 10, "attaquant", 0, 1, 36, 12)
j2 = Joueur("j2", 4, "defensseur", 0, 0, 5, 1)
j3 = Joueur("j3", 1, "gardien", 0, 0, 0, 0)
e1.ajouter_joueur(j1)
e1.ajouter_joueur(j2)
e1.ajouter_joueur(j3)
e1.afficher_stats_joueurs()

e2 = Equipe("Equipe 2")
j4 = Joueur("j4", 10, "attaquant", 0, 1, 36, 12)
j5 = Joueur("j5", 4, "defensseur", 0, 0, 5, 1)
j6 = Joueur("j6", 1, "gardien", 0, 0, 0, 0)
e2.ajouter_joueur(j4)
e2.ajouter_joueur(j5)
e2.ajouter_joueur(j6)
e1.afficher_stats_joueurs()

j1.recevoir_cart_jaune()
j1.recevoir_cart_rouge()
j4.marquer_but()
j5.recevoir_cart_jaune()

e1.afficher_stats_joueurs()
e2.afficher_stats_joueurs()



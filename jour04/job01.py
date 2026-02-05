class Personne() :

    def __init__(self):
        self.age = 14

    def afficher_age(self) :
        print(self.age)

    def modifier_age(self, age:int) :
        if age >= 0 :
            self.age = age
        else : 
            print("l'âge doit être un entier positif")

    def bonjour(self) :
        print("Hello")

class Eleve(Personne) :
    def __init__(self) :
        super().__init__()

    def aller_en_cours(self) :
        print("Je vais en cours")

    def afficher_age(self) :
        print(f"J'ai {self.age} ans")

class Professeur(Personne) :

    def __init__(self, matiere) :
        super().__init__()
        self.__matiere = matiere

    def enseigner(self) :
        print("Le cours va commencer")


pers = Personne()
eleve = Eleve() 

eleve.afficher_age()
        
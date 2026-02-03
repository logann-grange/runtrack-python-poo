class Personne() :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self) :
        return self.nom + " " + self.prenom
    

#======= JOB 4 ========#
pers1 = Personne('John', 'Doe')
pers2 = Personne('Jean', 'Dupont')
print(f"Je suis {pers1.SePresenter()}")
print(f"Je suis {pers2.SePresenter()}")

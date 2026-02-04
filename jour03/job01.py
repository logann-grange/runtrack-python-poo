class Ville() :

    def __init__(self, nom, nb_habitant) :
        self.__nom = nom
        self.__nb_habitant = nb_habitant
    
    def get_nb_habitant(self) :
        return self.__nb_habitant
    
    def set_nb_habitant(self, nb) :
        self.__nb_habitant = nb


class Personne() :

    def __init__(self, nom, age, ville:Ville) :
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self) : 
        self.__ville.set_nb_habitant(self.__ville.get_nb_habitant() + 1)

ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)
pers1 = Personne("John", 45, ville1)
pers2 = Personne("Myrtille", 4, ville1)
pers3 = Personne("Cloe", 18, ville2)

print(f"Paris : {ville1.get_nb_habitant()}")
print(f"Marseille : {ville2.get_nb_habitant()}")

pers1.ajouter_population()
pers2.ajouter_population()
pers3.ajouter_population()

print(f"Paris : {ville1.get_nb_habitant()}")
print(f"Marseille : {ville2.get_nb_habitant()}")



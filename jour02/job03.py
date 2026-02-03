class Livre() :
    
    def __init__(self, title, auteur, nb_page) :
        self.__title = title
        self.__auteur = auteur
        self.__nb_page = nb_page
        self.__disponible = True

    def get_title(self) :
        return self.__title
    
    def get_auteur(self) :
        return self.__auteur
    
    def get_nb_page(self) :
        return self.__nb_page
    
    def set_title(self, title) :
        self.__title = title

    def set_auteur(self, auteur) :
        self.__auteur = auteur


    def set_nb_page(self, nb_page) :
        if isinstance(nb_page, int) and nb_page > 0:
            self.__nb_page = nb_page
        else :
            print("ERREUR : le nombre de page doit être un nombre entier positif")
    
    def verification(self) :
        return self.__disponible
    
    def emprunter(self) :
        if self.verification() :
            self.__disponible = False

    def rendre(self) :
        if not self.verification() :
            self.__disponible = True

livre = Livre("Titre", "Quelqu'un", 444)

print(f"Disponible : {livre.verification()}")
livre.emprunter()
print(f"Disponible : {livre.verification()}")
livre.rendre()
print(f"Disponible : {livre.verification()}")



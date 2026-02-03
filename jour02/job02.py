class Livre() :
    
    def __init__(self, title, auteur, nb_page) :
        self.__title = title
        self.__auteur = auteur
        self.__nb_page = nb_page

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

livre = Livre("Titre", "Quelqu'un", 444)
print(f"Titre : {livre.get_title()}\nAuteur : {livre.get_auteur()}\nNombre de pages : {livre.get_nb_page()}")

livre.set_auteur("Quelqu'2")
livre.set_title("Ti-Tre")
livre.set_nb_page(666)
print(f"Titre : {livre.get_title()}\nAuteur : {livre.get_auteur()}\nNombre de pages : {livre.get_nb_page()}\n")



class Tache() :

    def __init__(self, titre, description,) :
        self.titre = titre
        self.description = description
        self.statut = "à faire"

    
class ListeTache() :
    
    def __init__(self, taches:list) :
        self.taches = taches

    def get_list(self) :
        return self.taches

    def ajouter_tache(self, tache) :
        self.taches.append(tache)

    def supprimer_tache(self, tache) :
        self.taches.remove(tache)

    def marquer_comme_finie(self, tache) :
        for t in self.taches :
            if t == tache :
                t.statut = "terminée"
    
    def afficher_liste(self) :
        for t in self.taches :
            print(f"{t.titre} : '{t.description}' ({t.statut})")
        print("\n")

    def filtrer_liste(self, statut) :
        liste_statut = ListeTache([])
        liste_non_statut = []
        for tache in self.taches :
            if tache.statut == statut :
                liste_statut.taches.append(tache)
            else :
                liste_non_statut.append(tache)
        for tache in liste_non_statut :
            liste_statut.taches.append(tache)
        return liste_statut
    

t1 = Tache("Test1", "desc 1",)
t2 = Tache("Test2", "desc 2",)
t3 = Tache("Test3", "desc 3",)
list_t = ListeTache([t1, t2, t3])
list_t.marquer_comme_finie(t2)
list_t.ajouter_tache(Tache("Test4", "desc 4",))
list_t.afficher_liste()
list_t.filtrer_liste("à faire").afficher_liste()
list_t.supprimer_tache(t2)
list_t.afficher_liste()



    
        
class Cercle() :
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon) :
        self.rayon = rayon
    
    def afficherInfos(self) :
        print(f"Rayon : {self.rayon}\nCirconference : {self.circonference()}\nAire : {self.aire()}\nDiametre : {self.diametre()}")

    def circonference(self) :
        return 2*self.rayon*3.14
    
    def aire(self) :
        return 3.14*self.rayon**2
    
    def diametre(self) :
        return 2*self.rayon
    
#======= JOB 8 ========#
c1 = Cercle(4)
c2 = Cercle(7)
c1.afficherInfos()
c2.afficherInfos()

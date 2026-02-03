class Point() :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def afficherLesPoints(self) :
        print(self.x, self.y)
    
    def afficherX(self) :
        print(self.x)
    
    def afficherY(self) :
        print(self.y)

    def changerX(self, x) :
        self.x = x

    def changerY(self, y) :
        self.y = y

#====== JOB 5 =======#
point = Point(4, 7)
point.afficherX()
point.afficherY()
point.changerX(5)
point.changerY(11)
point.afficherX()
point.afficherY()

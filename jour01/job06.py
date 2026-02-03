class Animal() :
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self) :
        self.age += 1
    
    def nommer(self, nom) :
        self.prenom = nom

#======= JOB 6 ========#
animal = Animal()
print(animal.age)
animal.vieillir()
print(animal.age)
animal.nommer("test")
print(animal.prenom)
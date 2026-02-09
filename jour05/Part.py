class Part() :
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, material) :
        self.material = material

    def __str__(self) :
        return f"{self.name} en {self.material}"
from Ship import Ship

class RacingShip(Ship) :

    def __init__(self, name, parts, max_speed):
        super().__init__(name, parts)
        self.max_speed = max_speed

    def display_speed(self) :
        print(f"Vitesse max : {self.max_speed}")

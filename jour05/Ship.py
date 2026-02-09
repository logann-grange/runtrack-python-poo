from Part import Part

class Ship() :
    def __init__(self, name, parts:dict):
        self.name = name
        self.__parts = parts
    
    def get_parts(self) :
        return self.__parts

    def display_state(self) :
        info = "" 
        for part in self.__parts :
            print(self.__parts[part])
            info += f"{self.__parts[part].name} en {self.__parts[part].material}\n"
        return info

    def replace_part(self, part_name, new_part:Part) :
        self.__parts[part_name] = new_part
        self.__parts[new_part.name] = self.__parts.pop(part_name)

    def change_part(self, part_name, new_material) :
        self.__parts[part_name].material = new_material
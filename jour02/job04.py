class Student() :
    def __init__(self, name, firstname, number) :
        self.__name = name
        self.__firstname = firstname
        self.__number = number
        self.__credits = 0
        self.__level = self.__student_eval()

    def get_name(self) :
        return self.__name
    
    def get_firstname(self) :
        return self.__firstname
    
    def get_number(self) :
        return self.__number
    
    def get_credits(self) :
        return self.__credits
    
    def get_level(self) :
        return self.__student_eval()
     

    def add_credits(self, credits) :
        if credits > 0 :
            self.__credits += credits

    def __student_eval(self) :
        if self.__credits >= 90 :
            return "Excellent"
        elif self.__credits >= 80 :
            return "Très bien"
        elif self.__credits >= 70 :
            return "Bien"
        elif self.__credits >= 60 :
            return "Passable"
        elif self.__credits < 60 :
            return "Insuffisans"
        
    def student_info(self) :
        print(f"Nom : {self.get_name()}\nPrénom : {self.get_firstname()}\nID : {self.get_number()}\nNiveau : {self.get_level()}")


stud = Student("Doe", "John", 145)
stud.add_credits(10)
stud.add_credits(75)
stud.add_credits(15)
print(f"Le nombre de crédits de {stud.get_firstname()} {stud.get_name()} est de {stud.get_credits()} points")
stud.student_info()
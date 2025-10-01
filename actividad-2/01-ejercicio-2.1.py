class Person:
    def __init__(self, name, surname, dni, birthYear):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.birthYear = birthYear
        
    def name(self):
        return self.name
    
    def surname(self):
        return self.surname
    
    def dni(self):
        return self.dni
    
    def birthYear(self):
        return self.birthYear
    
    def __str__(self):
        return f'Nombre = {self.name}' \
            + f'\nApellidos = {self.surname}' \
            + f'\nNúmero de documento de identidad = {self.dni}' \
            + f'\nAño de nacimiento = {self.birthYear}'
    
    def print(self):
        print(self)


p1 = Person("Pedro", "Pérez", 1053121010, 1998)
p2 = Person("Luis", "León", 1053223344, 2001)
p1.print()
p2.print()
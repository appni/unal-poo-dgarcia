class Programmer:
    def __init__(self, name, last_names):
        self.name = name
        self.last_names = last_names


class ProgrammingMarathonTeam:
    def __init__(self, team_name, university, programming_language):
        self.team_name = team_name
        self.university = university
        self.programming_language = programming_language
        self.team_size = 0
        self.programmers = [None] * 3

    def is_full(self):
        return self.team_size == len(self.programmers)

    def add(self, programmer):
        if self.is_full():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programmers[self.team_size] = programmer
        self.team_size += 1

    @staticmethod
    def validate_field(field):
        for c in field:
            if c.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(field) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

    @staticmethod
    def main():
        print("Nombre del equipo = ")
        name = input()
        print("Universidad = ")
        university = input()
        print("Lenguaje de programación = ")
        language = input()
        team = ProgrammingMarathonTeam(name, university, language)
        print("Datos de los integrantes del equipo")
        for i in range(3):
            print("Nombre del integrante = ")
            programmer_name = input()
            ProgrammingMarathonTeam.validate_field(programmer_name)
            print("Apellidos del integrante = ")
            programmer_last_names = input()
            ProgrammingMarathonTeam.validate_field(programmer_last_names)
            programmer = Programmer(programmer_name, programmer_last_names)
            team.add(programmer)

ProgrammingMarathonTeam.main()
class Seller:
    def __init__(self, name, last_names):
        self.name = name
        self.last_names = last_names
        self.age = None

    def print_info(self):
        print(f"Nombre del vendedor = {self.name}")
        print(f"Apellidos del vendedor = {self.last_names}")
        print(f"Edad del vendedor = {self.age}")

    def verify_age(self, age):
        if age < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= age < 120:
            self.age = age
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

    @staticmethod
    def main():
        print("Nombre del vendedor = ")
        n = input()
        print("Apellidos del vendedor = ")
        a = input()
        seller = Seller(n, a)
        print("Edad del vendedor = ")
        e = int(input())
        seller.verify_age(e)
        seller.print_info()

Seller.main()
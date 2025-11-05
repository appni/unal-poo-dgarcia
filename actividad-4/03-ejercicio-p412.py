import math

class NumericalCalculations:
    @staticmethod
    def calculate_natural_logarithm(value):
        try:
            if value < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            result = math.log(value)
            print(f"Resultado = {result}")
        except ArithmeticError as e:
            print("El valor debe ser un número positivo para calcular el logaritmo")
        except ValueError as e:
            print("El valor debe ser numérico para calcular el logaritmo")

    @staticmethod
    def calculate_square_root(value):
        try:
            if value < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            result = math.sqrt(value)
            print(f"Resultado = {result}")
        except ArithmeticError as e:
            print("El valor debe ser un número positivo para calcular la raíz cuadrada")
        except ValueError as e:
            print("El valor debe ser numérico para calcular la raíz cuadrada")

    @staticmethod
    def main():
        print("Valor numérico = ", end="")
        value = float(input())
        NumericalCalculations.calculate_natural_logarithm(value)
        NumericalCalculations.calculate_square_root(value)

NumericalCalculations.main()
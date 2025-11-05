class ExceptionsTest:
    @staticmethod
    def run():
        try:
            print("Ingresando al primer try")
            quotient = 10000/0
            print("Después de la división")
        except ArithmeticError as e:
            print("División por cero")
        finally:
            print("Ingresando al primer finally")

        try:
            print("Ingresando al segundo try")
            object_var = None
            object_var.toString()
            print("Imprimiendo objeto")
        except ArithmeticError as e:
            print("División por cero")
        except Exception as e:
            print("Ocurrió una excepción")
        finally:
            print("Ingresando al segundo finally")

ExceptionsTest.run()
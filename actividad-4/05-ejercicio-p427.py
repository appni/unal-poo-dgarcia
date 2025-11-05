class ReadFile:
    @staticmethod
    def main():
        file_name = "C:/prueba.txt"
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.readline()
                while line:
                    print(line, end='')
                    line = file.readline()
        except IOError as e:
            print("No se pudo leer el archivo.")

ReadFile.main()
from enum import Enum
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class TipoCargo(Enum):
    DIRECTIVO = "Directivo"
    ESTRATEGICO = "Estratégico"
    OPERATIVO = "Operativo"


class TipoGenero(Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"


class Empleado:
    def __init__(self, nombre, apellidos, cargo, genero, salario_dia, 
                 dias_trabajados, otros_ingresos, pagos_salud, aporte_pensiones):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.pagos_salud = pagos_salud
        self.aporte_pensiones = aporte_pensiones

    def calcular_nomina(self):
        return ((self.salario_dia * self.dias_trabajados) + self.otros_ingresos - 
                self.pagos_salud - self.aporte_pensiones)


class ListaEmpleados:
    def __init__(self):
        self.lista = []
        self.total_nomina = 0

    def agregar_empleado(self, empleado):
        self.lista.append(empleado)

    def calcular_total_nomina(self):
        self.total_nomina = sum(e.calcular_nomina() for e in self.lista)
        return self.total_nomina

    def obtener_matriz(self):
        datos = []
        self.total_nomina = 0
        for e in self.lista:
            datos.append([e.nombre, e.apellidos, f"{e.calcular_nomina():.2f}"])
            self.total_nomina += e.calcular_nomina()
        return datos

    def convertir_texto(self):
        texto = ""
        for e in self.lista:
            texto += (f"Nombre = {e.nombre}\n"
                     f"Apellidos = {e.apellidos}\n"
                     f"Cargo = {e.cargo.value}\n"
                     f"Género = {e.genero.value}\n"
                     f"Salario = ${e.salario_dia}\n"
                     f"Días trabajados = {e.dias_trabajados}\n"
                     f"Otros ingresos = ${e.otros_ingresos}\n"
                     f"Pagos salud = ${e.pagos_salud}\n"
                     f"Aportes pensiones = ${e.aporte_pensiones}\n"
                     f"---------\n")
        texto += f"Total nómina = ${self.calcular_total_nomina():.2f}"
        return texto


class VentanaAgregarEmpleado(tk.Toplevel):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        self.title("Agregar Empleado")
        self.geometry("300x400")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Nombre:").place(x=20, y=20, width=135, height=23)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=160, y=20, width=100, height=23)

        tk.Label(self, text="Apellidos:").place(x=20, y=50, width=135, height=23)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=160, y=50, width=100, height=23)

        tk.Label(self, text="Cargo:").place(x=20, y=80, width=135, height=23)
        self.campo_cargo = ttk.Combobox(self, values=["Directivo", "Estratégico", "Operativo"], state="readonly")
        self.campo_cargo.current(0)
        self.campo_cargo.place(x=160, y=80, width=100, height=23)

        tk.Label(self, text="Género:").place(x=20, y=110, width=100, height=30)
        self.genero_var = tk.StringVar(value="Masculino")
        tk.Radiobutton(self, text="Masculino", variable=self.genero_var, value="Masculino").place(x=160, y=110, width=100, height=30)
        tk.Radiobutton(self, text="Femenino", variable=self.genero_var, value="Femenino").place(x=160, y=140, width=100, height=30)

        tk.Label(self, text="Salario por día:").place(x=20, y=170, width=135, height=23)
        self.campo_salario_dia = tk.Entry(self)
        self.campo_salario_dia.place(x=160, y=170, width=100, height=23)

        tk.Label(self, text="Días trabajados al mes:").place(x=20, y=200, width=135, height=23)
        self.campo_dias = tk.Spinbox(self, from_=1, to=31, value=30)
        self.campo_dias.place(x=160, y=200, width=40, height=23)

        tk.Label(self, text="Otros ingresos:").place(x=20, y=230, width=135, height=23)
        self.campo_otros_ingresos = tk.Entry(self)
        self.campo_otros_ingresos.place(x=160, y=230, width=100, height=23)

        tk.Label(self, text="Pagos por salud:").place(x=20, y=260, width=135, height=23)
        self.campo_aportes_salud = tk.Entry(self)
        self.campo_aportes_salud.place(x=160, y=260, width=100, height=23)

        tk.Label(self, text="Aportes pensiones:").place(x=20, y=290, width=135, height=23)
        self.campo_pensiones = tk.Entry(self)
        self.campo_pensiones.place(x=160, y=290, width=100, height=23)

        tk.Button(self, text="Agregar", command=self.anadir_empleado).place(x=20, y=320, width=100, height=23)
        tk.Button(self, text="Borrar", command=self.limpiar_campos).place(x=160, y=320, width=80, height=23)

    def limpiar_campos(self):
        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.campo_salario_dia.delete(0, tk.END)
        self.campo_dias.delete(0, tk.END)
        self.campo_otros_ingresos.delete(0, tk.END)
        self.campo_aportes_salud.delete(0, tk.END)
        self.campo_pensiones.delete(0, tk.END)

    def anadir_empleado(self):
        try:
            cargo_texto = self.campo_cargo.get()
            tipo_cargo = {"Directivo": TipoCargo.DIRECTIVO, 
                         "Estratégico": TipoCargo.ESTRATEGICO, 
                         "Operativo": TipoCargo.OPERATIVO}[cargo_texto]
            
            tipo_genero = TipoGenero.MASCULINO if self.genero_var.get() == "Masculino" else TipoGenero.FEMENINO

            empleado = Empleado(
                self.campo_nombre.get(),
                self.campo_apellidos.get(),
                tipo_cargo,
                tipo_genero,
                float(self.campo_salario_dia.get()),
                int(self.campo_dias.get()),
                float(self.campo_otros_ingresos.get()),
                float(self.campo_aportes_salud.get()),
                float(self.campo_pensiones.get())
            )
            
            self.lista.agregar_empleado(empleado)
            messagebox.showinfo("Mensaje", "El empleado ha sido agregado")
            self.limpiar_campos()
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaNomina(tk.Toplevel):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        self.title("Nómina de Empleados")
        self.geometry("350x250")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Lista de empleados:").place(x=20, y=10, width=135, height=23)

        datos = self.lista.obtener_matriz()
        columnas = ("NOMBRE", "APELLIDOS", "SUELDO")
        
        tree = ttk.Treeview(self, columns=columnas, show="headings", height=5)
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        for fila in datos:
            tree.insert("", tk.END, values=fila)
        
        tree.place(x=20, y=50, width=310, height=100)

        tk.Label(self, text=f"Total nómina mensual = $ {self.lista.total_nomina:.2f}").place(x=20, y=160, width=250, height=23)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.empleados = ListaEmpleados()
        self.title("Nómina")
        self.geometry("280x380")
        self.resizable(False, False)
        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Agregar empleado", command=self.abrir_agregar_empleado)
        menu_opciones.add_command(label="Calcular nómina", command=self.abrir_nomina)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Guardar archivo", command=self.guardar_archivo)
        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.config(menu=barra_menu)

    def abrir_agregar_empleado(self):
        VentanaAgregarEmpleado(self.empleados)

    def abrir_nomina(self):
        VentanaNomina(self.empleados)

    def guardar_archivo(self):
        directorio = filedialog.askdirectory()
        if directorio:
            try:
                contenido = self.empleados.convertir_texto()
                ruta = f"{directorio}/Nomina.txt"
                with open(ruta, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                messagebox.showinfo("Mensaje", f"El archivo de la nómina Nomina.txt se ha creado en {directorio}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar el archivo: {str(e)}")

app = VentanaPrincipal()
app.mainloop()
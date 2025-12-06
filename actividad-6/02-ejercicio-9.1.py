import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class Contacto:
    def __init__(self, nombres, apellidos, fecha_nacimiento, direccion, telefono, correo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo


class ListaContactos:
    def __init__(self):
        self.lista = []

    def agregar_contacto(self, contacto):
        self.lista.append(contacto)


class VentanaContacto(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detalles del contacto")
        self.geometry("650x320")
        self.resizable(False, False)
        self.lista_contactos = ListaContactos()
        self.crear_widgets()

    def crear_widgets(self):
        main_frame = tk.Frame(self, relief=tk.SOLID, borderwidth=2, padx=10, pady=10, bg='lightgreen')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        grid_frame = tk.Frame(main_frame, bg='white')
        grid_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        tk.Label(grid_frame, text="Nombres:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.campo_nombres = tk.Entry(grid_frame, width=25)
        self.campo_nombres.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(grid_frame, text="Apellidos:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.campo_apellidos = tk.Entry(grid_frame, width=25)
        self.campo_apellidos.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(grid_frame, text="Fecha nacimiento (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        fecha_frame = tk.Frame(grid_frame)
        fecha_frame.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
        self.campo_year = ttk.Spinbox(fecha_frame, from_=1900, to=2100, width=6, format='%04.0f')
        self.campo_year.set(datetime.now().year)
        self.campo_year.pack(side=tk.LEFT, padx=2)
        
        tk.Label(fecha_frame, text="-").pack(side=tk.LEFT)
        
        self.campo_month = ttk.Spinbox(fecha_frame, from_=1, to=12, width=4, format='%02.0f')
        self.campo_month.set(datetime.now().month)
        self.campo_month.pack(side=tk.LEFT, padx=2)
        
        tk.Label(fecha_frame, text="-").pack(side=tk.LEFT)
        
        self.campo_day = ttk.Spinbox(fecha_frame, from_=1, to=31, width=4, format='%02.0f')
        self.campo_day.set(datetime.now().day)
        self.campo_day.pack(side=tk.LEFT, padx=2)

        tk.Label(grid_frame, text="Dirección:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.campo_direccion = tk.Entry(grid_frame, width=25)
        self.campo_direccion.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(grid_frame, text="Teléfono:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.campo_telefono = tk.Entry(grid_frame, width=25)
        self.campo_telefono.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(grid_frame, text="Correo:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.campo_correo = tk.Entry(grid_frame, width=25)
        self.campo_correo.grid(row=5, column=1, padx=5, pady=5)

        list_frame = tk.Frame(main_frame)
        list_frame.grid(row=0, column=2, rowspan=7, sticky='nsew', padx=5, pady=5)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, width=45, height=14)
        self.lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista.yview)

        button_frame = tk.Frame(grid_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky='ew')

        self.boton_agregar = tk.Button(button_frame, text="Agregar", command=self.mostrar_datos,
                                        bg='green', fg='white', font=('Arial', 10, 'bold'))
        self.boton_agregar.pack(fill=tk.X, padx=5)

        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)

    def obtener_fecha(self):
        try:
            year = int(self.campo_year.get())
            month = int(self.campo_month.get())
            day = int(self.campo_day.get())
            return datetime(year, month, day).date()
        except ValueError:
            return None

    def mostrar_datos(self):
        nombres = self.campo_nombres.get().strip()
        apellidos = self.campo_apellidos.get().strip()
        fecha = self.obtener_fecha()
        direccion = self.campo_direccion.get().strip()
        telefono = self.campo_telefono.get().strip()
        correo = self.campo_correo.get().strip()

        if not nombres or not apellidos or not direccion or not telefono or not correo:
            messagebox.showinfo("Mensaje", 
                              "Error en ingreso de datos\n\nNo se permiten campos vacíos")
        elif not fecha:
            messagebox.showerror("Error", "Fecha inválida. Por favor ingrese una fecha válida.")
        else:
            contacto = Contacto(nombres, apellidos, fecha, direccion, telefono, correo)
            self.lista_contactos.agregar_contacto(contacto)

            data = f"{nombres}-{apellidos}-{fecha}-{direccion}-{telefono}-{correo}"
            self.lista.insert(tk.END, data)

            self.campo_nombres.delete(0, tk.END)
            self.campo_apellidos.delete(0, tk.END)
            now = datetime.now()
            self.campo_year.set(now.year)
            self.campo_month.set(now.month)
            self.campo_day.set(now.day)
            self.campo_direccion.delete(0, tk.END)
            self.campo_telefono.delete(0, tk.END)
            self.campo_correo.delete(0, tk.END)


if __name__ == "__main__":
    app = VentanaContacto()
    app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime


class Habitacion:
    def __init__(self, numero_habitacion, disponible, precio_dia):
        self.numero_habitacion = numero_habitacion
        self.disponible = disponible
        self.precio_dia = precio_dia
        self.huesped = None


class Huesped:
    def __init__(self, nombres, apellidos, documento_identidad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento_identidad = documento_identidad
        self.fecha_ingreso = None
        self.fecha_salida = None

    def obtener_dias_alojamiento(self):
        if self.fecha_ingreso and self.fecha_salida:
            return (self.fecha_salida - self.fecha_ingreso).days
        return 0


class Hotel:
    def __init__(self):
        self.lista_habitaciones = [
            Habitacion(i, True, 120000 if i <= 5 else 160000)
            for i in range(1, 11)
        ]

    def buscar_fecha_ingreso_habitacion(self, numero):
        for habitacion in self.lista_habitaciones:
            if habitacion.numero_habitacion == numero and habitacion.huesped:
                return habitacion.huesped.fecha_ingreso.strftime("%Y/%m/%d")
        return ""

    def buscar_habitacion_ocupada(self, numero):
        for habitacion in self.lista_habitaciones:
            if habitacion.numero_habitacion == numero and not habitacion.disponible:
                return True
        return False

    def obtener_habitacion(self, numero):
        for habitacion in self.lista_habitaciones:
            if habitacion.numero_habitacion == numero:
                return habitacion
        return None


class VentanaPrincipal(tk.Tk):
    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.title("Hotel")
        self.geometry("280x380")
        self.resizable(False, False)
        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Consultar habitaciones", command=self.abrir_habitaciones)
        menu_opciones.add_command(label="Salida de huéspedes", command=self.abrir_salida)
        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.config(menu=barra_menu)

    def abrir_habitaciones(self):
        VentanaHabitaciones(self.hotel)

    def abrir_salida(self):
        try:
            numero_habitacion = simpledialog.askinteger("Salida de huéspedes", 
                                                           "Ingrese número de habitación",
                                                           minvalue=1, maxvalue=10)
            if numero_habitacion is None:
                return
                
            if numero_habitacion < 1 or numero_habitacion > 10:
                messagebox.showinfo("Mensaje", "El número de habitación debe estar entre 1 y 10")
            elif self.hotel.buscar_habitacion_ocupada(numero_habitacion):
                VentanaSalida(self.hotel, numero_habitacion)
            else:
                messagebox.showinfo("Mensaje", "La habitación ingresada no ha sido ocupada")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaHabitaciones(tk.Toplevel):
    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.title("Habitaciones")
        self.geometry("760x260")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        for i, habitacion in enumerate(self.hotel.lista_habitaciones):
            col = i % 5
            row = i // 5
            x = 20 + col * 140
            y = 30 + row * 90

            tk.Label(self, text=f"Habitación {habitacion.numero_habitacion}").place(x=x, y=y, width=130, height=23)
            estado = "Disponible" if habitacion.disponible else "No disponible"
            tk.Label(self, text=estado).place(x=x, y=y+20, width=100, height=23)

        tk.Label(self, text="Habitación a reservar:").place(x=250, y=180, width=135, height=23)
        self.campo_habitacion = tk.Spinbox(self, from_=1, to=10, value=1)
        self.campo_habitacion.place(x=380, y=180, width=40, height=23)

        tk.Button(self, text="Aceptar", command=self.aceptar).place(x=500, y=180, width=100, height=23)

    def aceptar(self):
        numero = int(self.campo_habitacion.get())
        if not self.hotel.buscar_habitacion_ocupada(numero):
            self.destroy()
            VentanaIngreso(self.hotel, numero)
        else:
            messagebox.showinfo("Mensaje", "La habitación está ocupada")


class VentanaIngreso(tk.Toplevel):
    def __init__(self, hotel, numero_habitacion):
        super().__init__()
        self.hotel = hotel
        self.numero_habitacion = numero_habitacion
        self.title("Ingreso")
        self.geometry("290x250")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        frame = ttk.Frame(self, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text=f"Habitación: {self.numero_habitacion}").grid(row=0, column=0, columnspan=2, pady=5)

        ttk.Label(frame, text="Fecha (aaaa-mm-dd):").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.campo_fecha = ttk.Entry(frame)
        self.campo_fecha.grid(row=1, column=1, pady=3)

        ttk.Label(frame, text="Huésped").grid(row=2, column=0, columnspan=2, pady=5)

        ttk.Label(frame, text="Nombre:").grid(row=3, column=0, sticky=tk.W, pady=3)
        self.campo_nombre = ttk.Entry(frame)
        self.campo_nombre.grid(row=3, column=1, pady=3)

        ttk.Label(frame, text="Apellidos:").grid(row=4, column=0, sticky=tk.W, pady=3)
        self.campo_apellidos = ttk.Entry(frame)
        self.campo_apellidos.grid(row=4, column=1, pady=3)

        ttk.Label(frame, text="Doc. Identidad:").grid(row=5, column=0, sticky=tk.W, pady=3)
        self.campo_documento = ttk.Entry(frame)
        self.campo_documento.grid(row=5, column=1, pady=3)

        ttk.Button(frame, text="Aceptar", command=self.aceptar).grid(row=6, column=0, pady=10)
        ttk.Button(frame, text="Cancelar", command=self.destroy).grid(row=6, column=1, pady=10)

    def aceptar(self):
        try:
            fecha_str = self.campo_fecha.get()
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

            huesped = Huesped(
                self.campo_nombre.get(),
                self.campo_apellidos.get(),
                int(self.campo_documento.get())
            )
            huesped.fecha_ingreso = fecha

            habitacion = self.hotel.obtener_habitacion(self.numero_habitacion)
            habitacion.huesped = huesped
            habitacion.disponible = False

            messagebox.showinfo("Mensaje", "El huésped ha sido registrado")
            self.destroy()
        except ValueError:
            messagebox.showerror("Error", "La fecha no está en el formato solicitado")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaSalida(tk.Toplevel):
    def __init__(self, hotel, numero_habitacion):
        super().__init__()
        self.hotel = hotel
        self.numero_habitacion = numero_habitacion
        self.habitacion = hotel.obtener_habitacion(numero_habitacion)
        self.title("Salida huéspedes")
        self.geometry("260x260")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        frame = ttk.Frame(self, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text=f"Habitación: {self.numero_habitacion}").grid(row=0, column=0, pady=5)

        fecha_ingreso = self.hotel.buscar_fecha_ingreso_habitacion(self.numero_habitacion)
        ttk.Label(frame, text=f"Fecha de ingreso: {fecha_ingreso}").grid(row=1, column=0, pady=5)

        ttk.Label(frame, text="Fecha de salida (aaaa-mm-dd):").grid(row=2, column=0, pady=3)
        self.campo_fecha_salida = ttk.Entry(frame)
        self.campo_fecha_salida.grid(row=3, column=0, pady=3)

        ttk.Button(frame, text="Calcular", command=self.calcular).grid(row=4, column=0, pady=10)

        self.label_dias = ttk.Label(frame, text="Cantidad de días:")
        self.label_dias.grid(row=5, column=0, pady=3)

        self.label_total = ttk.Label(frame, text="Total: $")
        self.label_total.grid(row=6, column=0, pady=3)

        self.boton_registrar = ttk.Button(frame, text="Registrar Salida", command=self.registrar_salida)
        self.boton_registrar.grid(row=7, column=0, pady=10)
        self.boton_registrar.config(state=tk.DISABLED)

    def calcular(self):
        try:
            fecha_salida_str = self.campo_fecha_salida.get()
            fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d")

            if self.habitacion.huesped.fecha_ingreso >= fecha_salida:
                messagebox.showerror("Mensaje", "La fecha de salida es menor que la de ingreso")
                return

            self.habitacion.huesped.fecha_salida = fecha_salida
            dias = self.habitacion.huesped.obtener_dias_alojamiento()
            total = dias * self.habitacion.precio_dia

            self.label_dias.config(text=f"Cantidad de días: {dias}")
            self.label_total.config(text=f"Total: ${total:.2f}")
            self.boton_registrar.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Mensaje", "La fecha no está en el formato solicitado")

    def registrar_salida(self):
        self.habitacion.huesped = None
        self.habitacion.disponible = True
        messagebox.showinfo("Mensaje", "Se ha registrado la salida del huésped")
        self.destroy()

hotel = Hotel()
app = VentanaPrincipal(hotel)
app.mainloop()
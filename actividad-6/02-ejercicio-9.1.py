import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import calendar


class DatePicker(tk.Toplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        self.title("Seleccionar Fecha")
        self.geometry("300x280")
        self.resizable(False, False)
        self.grab_set()
        
        self.selected_date = datetime.now()
        self.create_widgets()
        
    def create_widgets(self):
        control_frame = tk.Frame(self)
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="◀", command=self.prev_month, width=3).pack(side=tk.LEFT, padx=5)
        
        self.month_year_label = tk.Label(control_frame, text="", font=("Arial", 12, "bold"), width=15)
        self.month_year_label.pack(side=tk.LEFT, padx=10)
        
        tk.Button(control_frame, text="▶", command=self.next_month, width=3).pack(side=tk.LEFT, padx=5)
        
        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.pack(padx=10, pady=10)
        
        self.update_calendar()
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Hoy", command=self.select_today, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancelar", command=self.destroy, width=10).pack(side=tk.LEFT, padx=5)
        
    def update_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
            
        month_name = calendar.month_name[self.selected_date.month]
        self.month_year_label.config(text=f"{month_name} {self.selected_date.year}")
        
        days = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sá", "Do"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 9, "bold"), width=4).grid(row=0, column=i)
        
        cal = calendar.monthcalendar(self.selected_date.year, self.selected_date.month)
        
        for week_num, week in enumerate(cal, start=1):
            for day_num, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="", width=4).grid(row=week_num, column=day_num)
                else:
                    btn = tk.Button(self.calendar_frame, text=str(day), width=4,
                                  command=lambda d=day: self.select_day(d))
                    
                    if (day == self.selected_date.day and 
                        datetime.now().month == self.selected_date.month and 
                        datetime.now().year == self.selected_date.year):
                        btn.config(bg="lightblue")
                    
                    btn.grid(row=week_num, column=day_num, padx=1, pady=1)
    
    def prev_month(self):
        if self.selected_date.month == 1:
            self.selected_date = self.selected_date.replace(year=self.selected_date.year - 1, month=12, day=1)
        else:
            self.selected_date = self.selected_date.replace(month=self.selected_date.month - 1, day=1)
        self.update_calendar()
    
    def next_month(self):
        if self.selected_date.month == 12:
            self.selected_date = self.selected_date.replace(year=self.selected_date.year + 1, month=1, day=1)
        else:
            self.selected_date = self.selected_date.replace(month=self.selected_date.month + 1, day=1)
        self.update_calendar()
    
    def select_day(self, day):
        self.selected_date = self.selected_date.replace(day=day)
        self.callback(self.selected_date)
        self.destroy()
    
    def select_today(self):
        self.selected_date = datetime.now()
        self.callback(self.selected_date)
        self.destroy()


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

        tk.Label(grid_frame, text="Fecha nacimiento:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        
        fecha_input_frame = tk.Frame(grid_frame)
        fecha_input_frame.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
        self.campo_fecha = tk.Entry(fecha_input_frame, width=18, state='readonly')
        self.campo_fecha.pack(side=tk.LEFT)
        self.set_fecha(datetime.now())
        
        tk.Button(fecha_input_frame, text="📅", command=self.abrir_calendario, 
                 font=("Arial", 10), width=3).pack(side=tk.LEFT, padx=2)

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
    
    def abrir_calendario(self):
        DatePicker(self, self.set_fecha)
    
    def set_fecha(self, fecha):
        self.fecha_seleccionada = fecha
        self.campo_fecha.config(state='normal')
        self.campo_fecha.delete(0, tk.END)
        self.campo_fecha.insert(0, fecha.strftime("%Y-%m-%d"))
        self.campo_fecha.config(state='readonly')

    def obtener_fecha(self):
        return self.fecha_seleccionada.date() if hasattr(self, 'fecha_seleccionada') else None

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
            self.set_fecha(datetime.now())
            self.campo_direccion.delete(0, tk.END)
            self.campo_telefono.delete(0, tk.END)
            self.campo_correo.delete(0, tk.END)

app = VentanaContacto()
app.mainloop()
import tkinter as tk
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def get_area(self):
        return self._area
    
    def set_area(self, area):
        self._area = area
    
    def get_volume(self):
        return self._volume
    
    def set_volume(self, volume):
        self._volume = volume

class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.calculate_area()
        self.calculate_volume()
    
    def calculate_area(self):
        self._area = 2 * math.pi * self.radius * (self.radius + self.height)
    
    def calculate_volume(self):
        self._volume = math.pi * self.radius ** 2 * self.height

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.calculate_area()
        self.calculate_volume()
    
    def calculate_area(self):
        self._area = 4 * math.pi * self.radius ** 2
    
    def calculate_volume(self):
        self._volume = (4/3) * math.pi * self.radius ** 3

class Pyramid(Shape):
    def __init__(self, base, height, apothem):
        self.base = base
        self.height = height
        self.apothem = apothem
        self.calculate_area()
        self.calculate_volume()
    
    def calculate_area(self):
        perimeter = 4 * self.base
        lateral_area = (perimeter * self.apothem) / 2
        base_area = self.base ** 2
        self._area = lateral_area + base_area
    
    def calculate_volume(self):
        base_area = self.base ** 2
        self._volume = (base_area * self.height) / 3

class CylinderWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Cilindro")
        self.window.geometry("350x300")
        self.window.resizable(False, False)
        
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(main_frame, text="Cálculo de Cilindro", font=("Arial", 12, "bold"))
        title.pack(pady=(0, 15))
        
        radius_frame = tk.Frame(main_frame)
        radius_frame.pack(fill=tk.X, pady=5)
        tk.Label(radius_frame, text="Radio:", width=10).pack(side=tk.LEFT)
        self.radius_var = tk.StringVar()
        tk.Entry(radius_frame, textvariable=self.radius_var, width=15).pack(side=tk.LEFT)
        
        height_frame = tk.Frame(main_frame)
        height_frame.pack(fill=tk.X, pady=5)
        tk.Label(height_frame, text="Altura:", width=10).pack(side=tk.LEFT)
        self.height_var = tk.StringVar()
        tk.Entry(height_frame, textvariable=self.height_var, width=15).pack(side=tk.LEFT)
        
        tk.Button(main_frame, text="Calcular", command=self.calculate).pack(pady=15)
        
        self.area_label = tk.Label(main_frame, text="Área: --", font=("Arial", 10))
        self.area_label.pack(pady=5)
        
        self.volume_label = tk.Label(main_frame, text="Volumen: --", font=("Arial", 10))
        self.volume_label.pack(pady=5)
    
    def calculate(self):
        try:
            radius = float(self.radius_var.get())
            height = float(self.height_var.get())
            cylinder = Cylinder(radius, height)
            self.area_label.config(text=f"Área: {cylinder.get_area():.2f}")
            self.volume_label.config(text=f"Volumen: {cylinder.get_volume():.2f}")
        except ValueError:
            self.area_label.config(text="Área: Error")
            self.volume_label.config(text="Volumen: Error")

class SphereWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Esfera")
        self.window.geometry("350x250")
        self.window.resizable(False, False)
        
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(main_frame, text="Cálculo de Esfera", font=("Arial", 12, "bold"))
        title.pack(pady=(0, 15))
        
        radius_frame = tk.Frame(main_frame)
        radius_frame.pack(fill=tk.X, pady=5)
        tk.Label(radius_frame, text="Radio:", width=10).pack(side=tk.LEFT)
        self.radius_var = tk.StringVar()
        tk.Entry(radius_frame, textvariable=self.radius_var, width=15).pack(side=tk.LEFT)
        
        tk.Button(main_frame, text="Calcular", command=self.calculate).pack(pady=15)
        
        self.area_label = tk.Label(main_frame, text="Área: --", font=("Arial", 10))
        self.area_label.pack(pady=5)
        
        self.volume_label = tk.Label(main_frame, text="Volumen: --", font=("Arial", 10))
        self.volume_label.pack(pady=5)
    
    def calculate(self):
        try:
            radius = float(self.radius_var.get())
            sphere = Sphere(radius)
            self.area_label.config(text=f"Área: {sphere.get_area():.2f}")
            self.volume_label.config(text=f"Volumen: {sphere.get_volume():.2f}")
        except ValueError:
            self.area_label.config(text="Área: Error")
            self.volume_label.config(text="Volumen: Error")

class PyramidWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Pirámide")
        self.window.geometry("350x350")
        self.window.resizable(False, False)
        
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(main_frame, text="Cálculo de Pirámide", font=("Arial", 12, "bold"))
        title.pack(pady=(0, 15))
        
        base_frame = tk.Frame(main_frame)
        base_frame.pack(fill=tk.X, pady=5)
        tk.Label(base_frame, text="Base:", width=10).pack(side=tk.LEFT)
        self.base_var = tk.StringVar()
        tk.Entry(base_frame, textvariable=self.base_var, width=15).pack(side=tk.LEFT)
        
        height_frame = tk.Frame(main_frame)
        height_frame.pack(fill=tk.X, pady=5)
        tk.Label(height_frame, text="Altura:", width=10).pack(side=tk.LEFT)
        self.height_var = tk.StringVar()
        tk.Entry(height_frame, textvariable=self.height_var, width=15).pack(side=tk.LEFT)
        
        apothem_frame = tk.Frame(main_frame)
        apothem_frame.pack(fill=tk.X, pady=5)
        tk.Label(apothem_frame, text="Apotema:", width=10).pack(side=tk.LEFT)
        self.apothem_var = tk.StringVar()
        tk.Entry(apothem_frame, textvariable=self.apothem_var, width=15).pack(side=tk.LEFT)
        
        tk.Button(main_frame, text="Calcular", command=self.calculate).pack(pady=15)
        
        self.area_label = tk.Label(main_frame, text="Área: --", font=("Arial", 10))
        self.area_label.pack(pady=5)
        
        self.volume_label = tk.Label(main_frame, text="Volumen: --", font=("Arial", 10))
        self.volume_label.pack(pady=5)
    
    def calculate(self):
        try:
            base = float(self.base_var.get())
            height = float(self.height_var.get())
            apothem = float(self.apothem_var.get())
            pyramid = Pyramid(base, height, apothem)
            self.area_label.config(text=f"Área: {pyramid.get_area():.2f}")
            self.volume_label.config(text=f"Volumen: {pyramid.get_volume():.2f}")
        except ValueError:
            self.area_label.config(text="Área: Error")
            self.volume_label.config(text="Volumen: Error")

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras")
        self.root.geometry("400x150")
        self.root.resizable(False, False)
        
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        cylinder_btn = tk.Button(button_frame, text="Cilindro", width=12, command=self.show_cylinder)
        cylinder_btn.pack(side=tk.LEFT, padx=10)
        
        sphere_btn = tk.Button(button_frame, text="Esfera", width=12, command=self.show_sphere)
        sphere_btn.pack(side=tk.LEFT, padx=10)
        
        pyramid_btn = tk.Button(button_frame, text="Pirámide", width=12, command=self.show_pyramid)
        pyramid_btn.pack(side=tk.LEFT, padx=10)
    
    def show_cylinder(self):
        CylinderWindow()
    
    def show_sphere(self):
        SphereWindow()
    
    def show_pyramid(self):
        PyramidWindow()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
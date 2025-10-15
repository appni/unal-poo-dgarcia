import tkinter as tk
import statistics

class Grades:
    def __init__(self, grades):
        self.grades = grades
    
    def calculate_average(self):
        if self.grades:
            return statistics.mean(self.grades)
        return None
    
    def calculate_std(self):
        if len(self.grades) > 1:
            return statistics.stdev(self.grades)
        return None
    
    def calculate_min(self):
        if self.grades:
            return min(self.grades)
        return None
    
    def calculate_max(self):
        if self.grades:
            return max(self.grades)
        return None

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("280x360")
        self.root.resizable(False, False)
        
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.grade_vars = []
        self.entries = []
        
        for i in range(1, 6):
            frame = tk.Frame(main_frame)
            frame.pack(fill=tk.X, pady=5)
            
            label = tk.Label(frame, text=f"Nota {i}:", width=10)
            label.pack(side=tk.LEFT, padx=(0, 10))
            
            var = tk.StringVar(value="")
            self.grade_vars.append(var)
            
            entry = tk.Entry(frame, textvariable=var, width=15)
            entry.pack(side=tk.LEFT)
            self.entries.append(entry)
        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=15)
        
        calculate_btn = tk.Button(button_frame, text="Calcular", command=self.calculate)
        calculate_btn.pack(side=tk.LEFT, padx=5)
        
        clean_btn = tk.Button(button_frame, text="Limpiar", command=self.clean)
        clean_btn.pack(side=tk.LEFT, padx=5)
        
        footer = tk.Frame(root, relief=tk.SUNKEN, height=80, bd=1)
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=1, pady=1)
        
        stats_frame = tk.Frame(footer)
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.average_label = tk.Label(stats_frame, text="Promedio: --", font=("Arial", 10))
        self.average_label.pack(anchor=tk.W)
        
        self.std_label = tk.Label(stats_frame, text="Desviación Estándar: --", font=("Arial", 10))
        self.std_label.pack(anchor=tk.W)
        
        self.max_label = tk.Label(stats_frame, text="Máximo: --", font=("Arial", 10))
        self.max_label.pack(anchor=tk.W)
        
        self.min_label = tk.Label(stats_frame, text="Mínimo: --", font=("Arial", 10))
        self.min_label.pack(anchor=tk.W)
    
    def calculate(self):
        try:
            grades = []
            for var in self.grade_vars:
                try:
                    grade = float(var.get())
                    grades.append(grade)
                except (tk.TclError, ValueError):
                    pass
            
            if grades and len(grades) == 5:
                calculator = Grades(grades)
                
                average = calculator.calculate_average()
                std_dev = calculator.calculate_std()
                maximum = calculator.calculate_max()
                minimum = calculator.calculate_min()
                
                self.average_label.config(text=f"Promedio: {average:.2f}")
                self.std_label.config(text=f"Desviación Estándar: {std_dev:.2f}")
                self.max_label.config(text=f"Máximo: {maximum:.2f}")
                self.min_label.config(text=f"Mínimo: {minimum:.2f}")
            else:
                self.average_label.config(text="Promedio: --")
                self.std_label.config(text="Desviación Estándar: --")
                self.max_label.config(text="Máximo: --")
                self.min_label.config(text="Mínimo: --")
                
        except (ValueError, statistics.StatisticsError):
            self.average_label.config(text="Promedio: --")
            self.std_label.config(text="Desviación Estándar: --")
            self.max_label.config(text="Máximo: --")
            self.min_label.config(text="Mínimo: --")
    
    def clean(self):
        for var in self.grade_vars:
            var.set("")
        
        self.average_label.config(text="Promedio: --")
        self.std_label.config(text="Desviación Estándar: --")
        self.max_label.config(text="Máximo: --")
        self.min_label.config(text="Mínimo: --")
        
        self.entries[0].focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
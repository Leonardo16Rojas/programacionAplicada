import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variables para los números
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.resultado = tk.StringVar()
        
        # Crear interfaz
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Etiquetas y entradas
        tk.Label(main_frame, text="Primer número:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(main_frame, textvariable=self.num1).grid(row=0, column=1, pady=5)
        
        tk.Label(main_frame, text="Segundo número:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(main_frame, textvariable=self.num2).grid(row=1, column=1, pady=5)
        
        # Botones de operaciones
        tk.Button(main_frame, text="Sumar", command=self.add).grid(row=2, column=0, pady=5, sticky="we")
        tk.Button(main_frame, text="Restar", command=self.subtract).grid(row=2, column=1, pady=5, sticky="we")
        tk.Button(main_frame, text="Multiplicar", command=self.multiply).grid(row=3, column=0, pady=5, sticky="we")
        tk.Button(main_frame, text="Dividir", command=self.divide).grid(row=3, column=1, pady=5, sticky="we")
        tk.Button(main_frame, text="Módulo", command=self.modulo).grid(row=4, column=0, columnspan=2, pady=5, sticky="we")
        
        # Resultado
        tk.Label(main_frame, text="Resultado:").grid(row=5, column=0, sticky="w", pady=10)
        tk.Label(main_frame, textvariable=self.resultado, font=('Arial', 12, 'bold')).grid(row=5, column=1, sticky="e")
        
        # Botón de limpiar
        tk.Button(main_frame, text="Limpiar", command=self.clear).grid(row=6, column=0, columnspan=2, pady=10, sticky="we")
    
    def get_numbers(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
            return None, None
    
    def add(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            self.resultado.set(f"{a + b:.2f}")
    
    def subtract(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            self.resultado.set(f"{a - b:.2f}")
    
    def multiply(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            self.resultado.set(f"{a * b:.2f}")
    
    def divide(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            if b == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
            else:
                self.resultado.set(f"{a / b:.2f}")
    
    def modulo(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            if b == 0:
                messagebox.showerror("Error", "No se puede calcular el módulo por cero")
            else:
                self.resultado.set(f"{a % b:.2f}")
    
    def clear(self):
        self.num1.set("")
        self.num2.set("")
        self.resultado.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
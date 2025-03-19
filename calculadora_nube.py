import tkinter as tk
from tkinter import messagebox

class CloudCostCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Costos en la Nube")

        # Precios de ejemplo (en USD)
        self.prices = {
            "storage": 0.023,  # Precio por GB
            "instance": 0.0416,  # Precio por hora
            "data_transfer": 0.09  # Precio por GB
        }

        # Crear la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Título
        tk.Label(self.root, text="Calculadora de Costos en la Nube", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Entrada para almacenamiento
        tk.Label(self.root, text="Almacenamiento (GB):").grid(row=1, column=0, sticky="w", padx=10)
        self.storage_entry = tk.Entry(self.root)
        self.storage_entry.grid(row=1, column=1, padx=10)

        # Entrada para instancias
        tk.Label(self.root, text="Horas de Instancia EC2:").grid(row=2, column=0, sticky="w", padx=10)
        self.instance_entry = tk.Entry(self.root)
        self.instance_entry.grid(row=2, column=1, padx=10)

        # Entrada para transferencia de datos
        tk.Label(self.root, text="Transferencia de Datos (GB):").grid(row=3, column=0, sticky="w", padx=10)
        self.data_transfer_entry = tk.Entry(self.root)
        self.data_transfer_entry.grid(row=3, column=1, padx=10)

        # Botón para calcular
        self.calculate_button = tk.Button(self.root, text="Calcular", command=self.calculate_cost)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar el costo
        self.result_label = tk.Label(self.root, text="Costo Total: $0.00", font=("Arial", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_cost(self):
        try:
            # Obtener los valores de las entradas
            storage = float(self.storage_entry.get())
            instance_hours = float(self.instance_entry.get())
            data_transfer = float(self.data_transfer_entry.get())

            # Calcular el costo
            storage_cost = storage * self.prices["storage"]
            instance_cost = instance_hours * self.prices["instance"]
            data_transfer_cost = data_transfer * self.prices["data_transfer"]

            total_cost = storage_cost + instance_cost + data_transfer_cost

            # Mostrar el resultado
            self.result_label.config(text=f"Costo Total: ${total_cost:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CloudCostCalculator(root)
    root.mainloop()

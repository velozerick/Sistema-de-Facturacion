import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF

def submit_data():
    try:
        # Crear instancia de FPDF que representa el PDF
        pdf = FPDF()
        pdf.add_page()

        # Configurar fuente
        pdf.set_font("Arial", size=12)

        # Datos del formulario
        data = {
            "RFC": rfc_entry.get(),
            "Nombre o razón social": name_entry.get(),
            "Calle": street_entry.get(),
            "Número exterior": ext_number_entry.get(),
            "Número interior": int_number_entry.get(),
            "Colonia": suburb_entry.get(),
            "Código Postal": zip_entry.get(),
            "Delegación o Municipio": municipality_entry.get(),
            "Ciudad o Localidad": city_entry.get(),
            "Estado": state_combobox.get(),
            "País": country_combobox.get()
        }

        # Verificar campos obligatorios
        for key, value in data.items():
            if not value:
                messagebox.showerror("Error", f"El campo '{key}' es obligatorio")
                return

        # Agregar datos al PDF
        y = 10
        for label, value in data.items():
            pdf.set_xy(10, y)
            pdf.cell(200, 10, f"{label}: {value}", 0, 1)
            y += 10  # Incrementar posición y para la siguiente línea

        # Guardar el PDF
        pdf.output("Factura.pdf")
        messagebox.showinfo("Éxito", "Factura generada con éxito en formato PDF.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al generar la factura: {str(e)}")

# Configuración de la ventana
root = tk.Tk()
root.title("Datos Fiscales para Facturación")

# Etiquetas y campos de entrada
labels = [
    "RFC", "Nombre o razón social", "Calle", "Número exterior",
    "Número interior", "Colonia", "Código Postal", "Delegación o Municipio",
    "Ciudad o Localidad", "Estado", "País"
]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, sticky="w")
    if label in ["Estado", "País"]:  # Usar combobox para Estado y País
        entry = ttk.Combobox(root, values=["--Seleccione una opción--", "Opción 1", "Opción 2"])  # Agregar valores reales
        entry.grid(row=i, column=1, pady=2, padx=10, sticky="ew")
        entry.set("--Seleccione una opción--")
    else:
        entry = tk.Entry(root)
        entry.grid(row=i, column=1, pady=2, padx=10, sticky="ew")
    entries.append(entry)

# Alias para cada entrada para un acceso más fácil
rfc_entry, name_entry, street_entry, ext_number_entry, int_number_entry, \
suburb_entry, zip_entry, municipality_entry, city_entry, state_combobox, country_combobox = entries

# Botón para enviar datos
submit_button = tk.Button(root, text="Facturar", command=submit_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Configurar la ventana para ajustar el contenido
root.grid_columnconfigure(1, weight=1)

# Ejecutar el bucle principal de la aplicación
root.mainloop()

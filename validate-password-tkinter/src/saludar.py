# type: ignore

import tkinter as tk

# === Functions ===
def saludar_usuarios():
    nombre = entrada.get()
    label_saludo.config(text=f"Saludos {nombre}!!!")


# === TKINTER ===
ventana = tk.Tk()
ventana.title("Aprendiendo Tkinter")
ventana.geometry("400x400")


# Label
label = tk.Label(ventana, text="Inserta tu nombre:", font=("Arial", 20))
label.pack()

# Campo de entrada
entrada = tk.Entry(ventana)
entrada.pack()

# Botón
boton = tk.Button(ventana, text="Capturar",
                  command=saludar_usuarios, font=("Arial", 20))
boton.pack()

label_saludo = tk.Label(text="")
label_saludo.pack()

ventana.mainloop()

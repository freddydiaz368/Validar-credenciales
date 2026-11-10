import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

email = os.getenv("EMAIL_USER")
password = os.getenv("PASSWORD_USER")

# === FUNCTIONS ===
def capturar_credenciales():
    return entry_email.get(), entry_password.get()

def validar_credenciales(correo_ingresado, contraseña_ingresada):
    if correo_ingresado == email and contraseña_ingresada == password:
        return True
    return False

def mostrar_mensaje(es_valido):
    if es_valido:
        label_mensaje.config(text="Acceso correcto", fg="green")
    else:
        label_mensaje.config(text="Credenciales Incorrectas", fg="red")

def get_user_password():
    """Aquí debe validar el email del usuario y su contraseña"""
    correo_ing, contrasena_ing = capturar_credenciales()
    valido = validar_credenciales(correo_ing, contrasena_ing)
    mostrar_mensaje(valido)

# === TKINTER ===
ventana = tk.Tk()
ventana.title("Validar contraseñas")
ventana.geometry("300x300")

label_mensaje = tk.Label(ventana, text="")
label_mensaje.pack()

# == Email ==
label_email = tk.Label(ventana, text="Ingrese su correo electrónico")
label_email.pack()

entry_email = tk.Entry(ventana)
entry_email.pack()

# == Password ==
label_password = tk.Label(ventana, text="Ingrese su contraseña")
label_password.pack()

entry_password = tk.Entry(ventana, show="*")
entry_password.pack()


# == Butón ==
button = tk.Button(ventana, text="Ingresar", command=get_user_password)
button.pack()


ventana.mainloop()
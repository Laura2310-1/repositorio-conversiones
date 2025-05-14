import tkinter as tk

def longitud(tipo, num):
    if tipo == "metros a kilometros":
        return num /100
    elif tipo == "pulgadas a metros":
        return num * 0.0254
    
def masa():
    return


def mostrar_conversiones():
    ventana_conv = tk.Tk()
    ventana_conv.title("Ventana de conversiones")
    ventana_conv.geometry("600x200")

    ventana_conv.configure(bg="#c0d9e6")

    tk.Button(ventana_conv, text="Longuitud", bg="#5cb85c", fg="white").pack(pady=10)


mostrar_conversiones()

import tkinter as tk


def metros_a_kilometros():
    try:
        metros = float(entrada_valor.get())
        resultado = metros / 1000
        etiqueta_resultado.config(text=f"resultado: {resultado:.3f} km", fg="green")
    except ValueError:
        etiqueta_resultado.config(text="rrror: ingresa un numero valido", fg="red")

def pulgadas_a_metros():
    try:
        pulgadas = float(entrada_valor.get())
        resultado = pulgadas * 0.0254
        etiqueta_resultado.config(text=f"resultado: {resultado:.3f} m", fg="green")
    except ValueError:
        etiqueta_resultado.config(text="rrror: ingresa un numero valido", fg="red")

def kilogramos_a_gramos():
    try:
        kg = float(entrada_valor.get())
        resultado = kg * 1000
        etiqueta_resultado.config(text=f"resultado: {resultado:.2f} g", fg="green")
    except ValueError:
        etiqueta_resultado.config(text="rrror: ingresa un numero valido", fg="red")

def libras_a_kilogramos():
    try:
        libras = float(entrada_valor.get())
        resultado = libras * 0.453592
        etiqueta_resultado.config(text=f"resultado: {resultado:.3f} kg", fg="green")
    except ValueError:
        etiqueta_resultado.config(text="rrror: ingresa un numero valido", fg="red")

def segundos_a_minutos():
    try:
        segundos = float(entrada_valor.get())
        resultado = segundos / 60
        etiqueta_resultado.config(text=f"resultado: {resultado:.2f} min", fg="green")
    except ValueError:
        etiqueta_resultado.config(text="rrror: ingresa un numero valido", fg="red")

def horas_a_dias():
    try:
        horas = float(entrada_valor.get())
        resultado = horas / 24
        etiqueta_resultado.config(text=f"resultado: {resultado:.2f} días", fg="green")
    except ValueError:
        etiqueta_resultado.config(text="rrror: ingresa un numero valido", fg="red")



def abrir_longitud():
    ventana = tk.Toplevel()
    ventana.title("conversion de longitud")
    ventana.configure(bg="#f0f0f0")

    tk.Label(ventana, text="ingrese valor:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
    global entrada_valor
    entrada_valor = tk.Entry(ventana)
    entrada_valor.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(ventana, text="Metros a Kilómetros", command=metros_a_kilometros, bg="#ffa500", fg="white").grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Pulgadas a Metros", command=pulgadas_a_metros, bg="#ffa500", fg="white").grid(row=2, column=0, columnspan=2, pady=5)

    global etiqueta_resultado
    etiqueta_resultado = tk.Label(ventana, text="Resultado:", bg="#f0f0f0", font=("Arial", 12))
    etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

def abrir_masa():
    ventana = tk.Toplevel()
    ventana.title("Conversion de Masa")
    ventana.configure(bg="#f0f0f0")

    tk.Label(ventana, text="Ingrese valor:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
    global entrada_valor
    entrada_valor = tk.Entry(ventana)
    entrada_valor.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(ventana, text="Kg a Gramos", command=kilogramos_a_gramos, bg="#ffa500", fg="white").grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Libras a Kg", command=libras_a_kilogramos, bg="#ffa500", fg="white").grid(row=2, column=0, columnspan=2, pady=5)

    global etiqueta_resultado
    etiqueta_resultado = tk.Label(ventana, text="Resultado:", bg="#f0f0f0", font=("Arial", 12))
    etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

def abrir_tiempo():
    ventana = tk.Toplevel()
    ventana.title("Conversion de Tiempo")
    ventana.configure(bg="#f0f0f0")

    tk.Label(ventana, text="Ingrese valor:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
    global entrada_valor
    entrada_valor = tk.Entry(ventana)
    entrada_valor.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(ventana, text="Segundos a Minutos", command=segundos_a_minutos, bg="#ffa500", fg="white").grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Horas a Días", command=horas_a_dias, bg="#ffa500", fg="white").grid(row=2, column=0, columnspan=2, pady=5)

    global etiqueta_resultado
    etiqueta_resultado = tk.Label(ventana, text="Resultado:", bg="#f0f0f0", font=("Arial", 12))
    etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)




ventana_principal = tk.Tk()
ventana_principal.title("Conversor de Unidades")
ventana_principal.configure(bg="#e6f2ff")
ventana_principal.geometry("300x250")

tk.Label(ventana_principal, text="Escoja una opción", font=("Arial", 14), bg="#80aec3").grid(row=0, column=0, columnspan=2, pady=20)

tk.Button(ventana_principal, text="Longitud", command=abrir_longitud, width=20, height=2, bg="#27576a", fg="white").grid(row=1, column=0, columnspan=2, pady=10)
tk.Button(ventana_principal, text="Masa", command=abrir_masa, width=20, height=2, bg="#457387", fg="white").grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(ventana_principal, text="Tiempo", command=abrir_tiempo, width=20, height=2, bg="#6290a4", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

ventana_principal.mainloop()

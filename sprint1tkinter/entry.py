import tkinter as tk


def saludar():
    nombre = entrada.get()
    if nombre.strip():
        etiqueta_saludo.config(text=f"¡Hola, {nombre}!")
    else:
        etiqueta_saludo.config(text="Por favor, escribe tu nombre.")


root = tk.Tk()
root.title("Ejercicio 3: Entry")
root.geometry("350x200")


etiqueta_instruccion = tk.Label(root, text="Escribe tu nombre:")
etiqueta_instruccion.pack(pady=5)


entrada = tk.Entry(root)
entrada.pack(pady=5)


boton_saludar = tk.Button(root, text="Saludar", command=saludar)
boton_saludar.pack(pady=10)


etiqueta_saludo = tk.Label(root, text="")
etiqueta_saludo.pack(pady=10)


root.mainloop()
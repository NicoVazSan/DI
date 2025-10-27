import tkinter as tk


def cambiar_texto():
    etiqueta3.config(text="¡El texto ha cambiado!")


root = tk.Tk()
root.title("Ejercicio 1: Label")
root.geometry("300x200")


etiqueta1 = tk.Label(root, text="¡Bienvenido a mi aplicación!")
etiqueta1.pack(pady=10)

etiqueta2 = tk.Label(root, text="Nicolás Vázquez Santos")
etiqueta2.pack(pady=10)

etiqueta3 = tk.Label(root, text="Texto original")
etiqueta3.pack(pady=10)


boton_cambiar = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton_cambiar.pack(pady=10)

root.mainloop()
import tkinter as tk


def mostrar_mensaje():
    etiqueta.config(text="¡Has presionado el botón!")


root = tk.Tk()
root.title("Ejercicio 2: Button")
root.geometry("300x200")


etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=20)


boton_mostrar = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=10)

root.mainloop()
import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 6: Listbox - Frutas")
root.geometry("300x250")


def mostrar_fruta():
    seleccion = lista.curselection()
    if seleccion:
        fruta = lista.get(seleccion)
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")
    else:
        etiqueta.config(text="No has seleccionado ninguna fruta")


lista = tk.Listbox(root, selectmode=tk.SINGLE, height=5)
lista.insert(1, "Manzana")
lista.insert(2, "Banana")
lista.insert(3, "Naranja")
lista.pack(pady=10)


boton = tk.Button(root, text="Mostrar selección", command=mostrar_fruta)
boton.pack(pady=5)


etiqueta = tk.Label(root, text="Selecciona una fruta y pulsa el botón")
etiqueta.pack(pady=10)


root.mainloop()
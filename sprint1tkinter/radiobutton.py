import tkinter as tk

def cambiar_color():
    color = var_color.get()
    root.config(var_color.set(color))
    etiqueta.config(text=f"Color seleccionado: {color.capitalize()}")

root = tk.Tk()
root.title("Ejercicio 5: Radiobutton")
root.geometry("300x200")


var_color = tk.StringVar()
var_color.set("")


etiqueta = tk.Label(root, text="Elige tu color favorito:")
etiqueta.pack(pady=10)


radio_rojo = tk.Radiobutton(root, text="Rojo", variable=var_color, value="red", command=cambiar_color)
radio_verde = tk.Radiobutton(root, text="Verde", variable=var_color, value="green", command=cambiar_color)
radio_azul = tk.Radiobutton(root, text="Azul", variable=var_color, value="blue", command=cambiar_color)

radio_rojo.pack(pady=10)
radio_verde.pack(pady=10)
radio_azul.pack(pady=10)


root.mainloop()
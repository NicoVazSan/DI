import tkinter as tk

def actualizar():
    aficiones = []
    if var_leer.get() == 1:
        aficiones.append("Leer")
    if var_deporte.get() == 1:
        aficiones.append("Deporte")
    if var_musica.get() == 1:
        aficiones.append("Música")


    if aficiones:
        texto = "Aficiones seleccionadas: " + ", ".join(aficiones)
    else:
        texto = "No se ha seleccionado ninguna afición."

    etiqueta.config(text=texto)


root = tk.Tk()
root.title("Ejercicio 4: Checkbutton")
root.geometry("300x200")


var_leer = tk.IntVar()
var_deporte = tk.IntVar()
var_musica = tk.IntVar()


check_leer = tk.Checkbutton(root, text="Leer", variable=var_leer, command=actualizar)
check_deporte = tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=actualizar)
check_musica = tk.Checkbutton(root, text="Música", variable=var_musica, command=actualizar)


check_leer.pack(pady=10)
check_deporte.pack(pady=10)
check_musica.pack(pady=10)


etiqueta = tk.Label(root, text="Selecciona tus aficiones.")
etiqueta.pack(pady=10)


root.mainloop()
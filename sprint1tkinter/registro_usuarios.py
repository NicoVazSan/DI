import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ejercicio 12: Registro de usuarios ")
root.geometry("900x650")

var_genero = tk.StringVar()
var_genero.set("")

var_usuario = tk.StringVar()
var_usuario.set("")

var_edad = tk.IntVar()
var_edad.set(0)
var_index = tk.IntVar()
var_index.set(1)



def mensaje():
    messagebox.showinfo("Acerca de", "Hola, soy un mensaje")

def salir ():
    root.destroy()

def borrar():
        seleccion = lista.curselection()
        if seleccion:
            persona = lista.get(seleccion)
            lista.delete(seleccion)

def guardar():
    usuario = var_usuario.get()
    edad = var_edad.get()
    genero = var_genero.get()

    lista.insert(tk.END, f"{usuario} - {genero} - {edad} años")
    var_index.set(var_index.get() + 1)


def actualizar_valor(valor):
    etiqueta_valor.config(text=f"Valor seleccionado: {valor}")
    var_edad.set(valor)


def cambiar_genero():
    genero = var_genero.get()
    root.config(var_genero.set(genero))
    etiqueta_genero.config(text=f"Genero seleccionado: {genero.capitalize()}")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=mensaje)
menu_archivo.add_command(label="Cargar Lista", command=mensaje)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

lista = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=100)
lista.pack(pady=10)


scroll = tk.Scrollbar(root, orient="vertical", command=lista.yview)
scroll.pack(side="right", fill="y")


lista.config(yscrollcommand=scroll.set)


etiqueta_instruccion = tk.Label(root, text="Escribe tu nombre:")
etiqueta_instruccion.pack(pady=5)

entrada = tk.Entry(root, textvariable=var_usuario)
entrada.pack(pady=5)

etiqueta_instruccion = tk.Label(root, text="Escribe tu edad:")
etiqueta_instruccion.pack(pady=5)

escala = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    length=250,
    command=actualizar_valor
)
escala.pack(pady=5)


etiqueta_valor = tk.Label(root, text="Valor seleccionado: 0")
etiqueta_valor.pack(pady=5)

hombre = tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino", command=cambiar_genero)
mujer = tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino", command=cambiar_genero)
otro = tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro", command=cambiar_genero)

hombre.pack(pady=10)
mujer.pack(pady=10)
otro.pack(pady=10)

etiqueta_genero = tk.Label(root, text="¿Cual es tu genero?")
etiqueta_genero.pack(pady=10)

boton_anadir = tk.Button(root, text="Añadir", command=guardar)
boton_anadir.pack(pady=10)

boton_borrar = tk.Button(root, text="Borrar", command=borrar)
boton_borrar.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.pack(pady=10)

root.mainloop()
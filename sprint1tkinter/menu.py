import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ejercicio 9: Menú")
root.geometry("400x250")

def salir():
    root.quit()

def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Hola, soy un mensaje")


barra_menu = tk.Menu(root)
root.config(menu=barra_menu)


menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)


menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

root.mainloop()
import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 8: Frame")
root.geometry("400x250")


frame_superior = tk.Frame(root, bg="#e6f2ff", pady=10)
frame_superior.pack(fill="x")


tk.Label(frame_superior, text="Introduce tu nombre:", bg="#e6f2ff").grid(row=0, column=0, padx=5, pady=5)
entrada = tk.Entry(frame_superior, width=25)
entrada.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Resultado:", bg="#e6f2ff").grid(row=1, column=0, padx=5, pady=5)
etiqueta_resultado = tk.Label(frame_superior, text="", bg="#e6f2ff", fg="blue")
etiqueta_resultado.grid(row=1, column=1, padx=5, pady=5)


frame_inferior = tk.Frame(root, bg="#f2f2f2", pady=15)
frame_inferior.pack(fill="x")


def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=texto)

def borrar_texto():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")


btn_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar_texto)
btn_mostrar.grid(row=0, column=0, padx=10)

btn_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar_texto)
btn_borrar.grid(row=0, column=1, padx=10)


root.mainloop()
import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 11: Scale")
root.geometry("350x250")


def actualizar_valor(valor):
    etiqueta_valor.config(text=f"Valor seleccionado: {valor}")


escala = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    length=250,
    command=actualizar_valor
)
escala.pack(pady=20)


etiqueta_valor = tk.Label(root, text="Valor seleccionado: 0")
etiqueta_valor.pack(pady=10)


root.mainloop()
import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 7: Canvas")
root.geometry("400x400")


canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(pady=10)

tk.Label(root, text="x1:").pack()
entrada_x1 = tk.Entry(root)
entrada_x1.pack()

tk.Label(root, text="y1:").pack()
entrada_y1 = tk.Entry(root)
entrada_y1.pack()

tk.Label(root, text="x2:").pack()
entrada_x2 = tk.Entry(root)
entrada_x2.pack()

tk.Label(root, text="y2:").pack()
entrada_y2 = tk.Entry(root)
entrada_y2.pack()


def dibujar():
    try:
        x1 = int(entrada_x1.get())
        y1 = int(entrada_y1.get())
        x2 = int(entrada_x2.get())
        y2 = int(entrada_y2.get())


        canvas.delete("all")


        canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)
        canvas.create_oval(x1, y1, x2, y2, outline="red", width=2)
    except ValueError:
        print("Por favor, introduce solo números válidos.")


boton = tk.Button(root, text="Dibujar figuras", command=dibujar)
boton.pack(pady=10)

root.mainloop()

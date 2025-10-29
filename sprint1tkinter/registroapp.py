import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14: Registro de Usuarios")
        self.root.geometry("600x600")

        # ----- VARIABLES -----
        self.var_genero = tk.StringVar(value="Otro")
        self.var_usuario = tk.StringVar()
        self.var_edad = tk.IntVar(value=0)

        # ----- MENÚ -----
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Guardar Lista", command=self.mensaje)
        menu_archivo.add_command(label="Cargar Lista", command=self.mensaje)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        # ----- LISTBOX + SCROLLBAR -----
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10)

        self.lista = tk.Listbox(frame_lista, selectmode=tk.SINGLE, height=8, width=60)
        self.lista.pack(side="left", padx=5)

        scroll = tk.Scrollbar(frame_lista, orient="vertical", command=self.lista.yview)
        scroll.pack(side="right", fill="y")

        self.lista.config(yscrollcommand=scroll.set)

        # ----- ENTRADA NOMBRE -----
        tk.Label(self.root, text="Escribe tu nombre:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.var_usuario).pack(pady=5)

        # ----- SCALE EDAD -----
        tk.Label(self.root, text="Selecciona tu edad:").pack(pady=5)
        self.etiqueta_valor = tk.Label(self.root, text="Valor seleccionado: 0")
        self.etiqueta_valor.pack()

        escala = tk.Scale(
            self.root,
            from_=0,
            to=100,
            orient="horizontal",
            length=300,
            variable=self.var_edad,
            command=self.actualizar_valor
        )
        escala.pack(pady=5)


        tk.Label(self.root, text="Selecciona tu género:").pack(pady=5)
        tk.Radiobutton(self.root, text="Masculino", variable=self.var_genero, value="Masculino", command=self.cambiar_genero).pack()
        tk.Radiobutton(self.root, text="Femenino", variable=self.var_genero, value="Femenino", command=self.cambiar_genero).pack()
        tk.Radiobutton(self.root, text="Otro", variable=self.var_genero, value="Otro", command=self.cambiar_genero).pack()

        self.etiqueta_genero = tk.Label(self.root, text="Género seleccionado: Otro")
        self.etiqueta_genero.pack(pady=5)


        tk.Button(self.root, text="Añadir", command=self.guardar).pack(pady=5)
        tk.Button(self.root, text="Borrar", command=self.borrar).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.salir).pack(pady=5)


    def mensaje(self):
        messagebox.showinfo("Acerca de", "Hola, soy un mensaje")

    def salir(self):
            self.root.destroy()

    def borrar(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)
        else:
            messagebox.showwarning("Aviso", "Selecciona un usuario para borrar")

    def guardar(self):
        usuario = self.var_usuario.get().strip()
        edad = self.var_edad.get()
        genero = self.var_genero.get()


        self.lista.insert(tk.END, f"{usuario} - {genero} - {edad} años")


    def actualizar_valor(self, valor):
        self.etiqueta_valor.config(text=f"Valor seleccionado: {valor}")
        self.var_edad.set(int(valor))

    def cambiar_genero(self):
        genero = self.var_genero.get()
        self.etiqueta_genero.config(text=f"Género seleccionado: {genero}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
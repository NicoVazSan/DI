import customtkinter as ctk

# python
import customtkinter as ctk

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro de Usuarios (CTk + MVC) - Fase 2")
        self.geometry("900x500")


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # PANEL IZQUIERDO
        self.frame_lista = ctk.CTkFrame(self, corner_radius=10)
        self.frame_lista.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)
        self.frame_lista.grid_rowconfigure(1, weight=1)

        titulo_lista = ctk.CTkLabel(self.frame_lista, text="Usuarios", font=("Arial", 20))
        titulo_lista.grid(row=0, column=0, padx=10, pady=10)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.frame_lista)
        self.lista_usuarios_scrollable.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


        self.btn_add = ctk.CTkButton(self.frame_lista, text="Añadir Usuario")
        self.btn_add.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # PANEL DERECHO
        self.frame_detalles = ctk.CTkFrame(self, corner_radius=10)
        self.frame_detalles.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        titulo_detalles = ctk.CTkLabel(self.frame_detalles, text="Detalles del Usuario", font=("Arial", 20))
        titulo_detalles.grid(row=0, column=0, padx=10, pady=10)


        self.avatar_label = ctk.CTkLabel(self.frame_detalles, text="")
        self.avatar_label.grid(row=1, column=0, padx=10, pady=10)


        self.lbl_nombre = ctk.CTkLabel(self.frame_detalles, text="Nombre: -", anchor="w")
        self.lbl_nombre.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.lbl_edad = ctk.CTkLabel(self.frame_detalles, text="Edad: -", anchor="w")
        self.lbl_edad.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.lbl_genero = ctk.CTkLabel(self.frame_detalles, text="Género: -", anchor="w")
        self.lbl_genero.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.lbl_avatar = ctk.CTkLabel(self.frame_detalles, text="Avatar: -", anchor="w")
        self.lbl_avatar.grid(row=5, column=0, padx=10, pady=5, sticky="w")


    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):

        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()


        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=5)



    def mostrar_detalles_usuario(self, usuario, image=None):

        if image:
            self.avatar_label.configure(image=image, text="")

            self.avatar_label.image = image
        else:
            self.avatar_label.configure(image="", text="")

        self.lbl_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.lbl_edad.configure(text=f"Edad: {usuario.edad}")
        self.lbl_genero.configure(text=f"Género: {usuario.genero}")
        self.lbl_avatar.configure(text=f"Avatar: {usuario.avatar if usuario.avatar else '-'}")

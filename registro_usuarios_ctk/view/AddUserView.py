import customtkinter as ctk

class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x380")
        self.window.grab_set()  # modal


        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=(10, 2))
        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.pack(padx=20, fill="x")


        ctk.CTkLabel(self.window, text="Edad:").pack(pady=(10, 2))
        self.edad_entry = ctk.CTkEntry(self.window)
        self.edad_entry.pack(padx=20, fill="x")


        ctk.CTkLabel(self.window, text="Género:").pack(pady=(10, 2))
        self.genero_var = ctk.StringVar(value="Otro")
        ctk.CTkRadioButton(self.window, text="Masculino", variable=self.genero_var, value="Masculino").pack(anchor="w", padx=30)
        ctk.CTkRadioButton(self.window, text="Femenino", variable=self.genero_var, value="Femenino").pack(anchor="w", padx=30)
        ctk.CTkRadioButton(self.window, text="Otro", variable=self.genero_var, value="Otro").pack(anchor="w", padx=30)


        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=(10, 2))
        self.avatar_var = ctk.StringVar(value="-")
        ctk.CTkRadioButton(self.window, text="Avatar 1", variable=self.avatar_var, value="Avatar1.png").pack(anchor="w", padx=30)
        ctk.CTkRadioButton(self.window, text="Avatar 2", variable=self.avatar_var, value="Avatar2.png").pack(anchor="w", padx=30)
        ctk.CTkRadioButton(self.window, text="Avatar 3", variable=self.avatar_var, value="avatar3.png").pack(anchor="w", padx=30)


        self.guardar_button = ctk.CTkButton(self.window, text="Guardar")
        self.guardar_button.pack(pady=(15, 5), padx=20, fill="x")

        self.cancelar_button = ctk.CTkButton(self.window, text="Cancelar", command=self.window.destroy)
        self.cancelar_button.pack(pady=(0, 10), padx=20, fill="x")

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get().strip(),
            "edad": self.edad_entry.get().strip(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_var.get() or "-"
        }
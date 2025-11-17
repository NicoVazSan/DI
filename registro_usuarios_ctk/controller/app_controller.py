from pathlib import Path
from tkinter import messagebox
from PIL import Image, ImageTk

from registro_usuarios_ctk.model.usuario_model import GestorUsuarios, Usuario
from registro_usuarios_ctk.view.AddUserView import AddUserView
from registro_usuarios_ctk.view.main_view import MainView

class AppController:
    def __init__(self):

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"


        self.avatar_images = {}

        self.modelo = GestorUsuarios()
        self.vista = MainView()

        if hasattr(self.vista, "btn_add"):
            self.vista.btn_add.configure(command=self.abrir_ventana_añadir)


        self._preload_avatar_images()

        self.refrescar_lista_usuarios()

    def iniciar(self):
        self.vista.mainloop()

    def _find_asset_file(self, filename):

        candidate = self.ASSETS_PATH / filename
        if candidate.exists():
            return candidate
        for p in self.ASSETS_PATH.iterdir():
            if p.is_file() and p.name.lower() == filename.lower():
                return p
        return None

    def _load_avatar_for_index(self, index, avatar_filename):
        if not avatar_filename or avatar_filename == "-":
            return
        avatar_path = self._find_asset_file(avatar_filename)
        if avatar_path:
            try:
                img = Image.open(avatar_path).convert("RGBA")
                img = img.resize((120, 120), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.avatar_images[index] = photo
            except Exception:

                pass

    def _preload_avatar_images(self):
        for idx, usuario in enumerate(self.modelo.listar()):
            if usuario.avatar and usuario.avatar != "-":
                self._load_avatar_for_index(idx, usuario.avatar)

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.vista.actualizar_lista_usuarios(
            usuarios,
            self.seleccionar_usuario
        )

    def seleccionar_usuario(self, indice):
        usuario = self.modelo.obtener(indice)
        image = self.avatar_images.get(indice)
        self.vista.mostrar_detalles_usuario(usuario, image)

    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.vista)
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))

    def añadir_usuario(self, add_view):
        data = add_view.get_data()

        try:
            edad = int(data["edad"])
        except Exception:
            messagebox.showerror("Error", "Edad inválida. Introduce un número entero.")
            return

        nombre = data["nombre"] or "Sin nombre"
        genero = data["genero"]
        avatar_filename = data["avatar"] if data["avatar"] != "-" else "-"

        usuario = Usuario(nombre, edad, genero, avatar_filename)
        self.modelo._usuarios.append(usuario)
        index = len(self.modelo._usuarios) - 1


        if avatar_filename != "-":
            self._load_avatar_for_index(index, avatar_filename)

        self.refrescar_lista_usuarios()
        add_view.window.destroy()
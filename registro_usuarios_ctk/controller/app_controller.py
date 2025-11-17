from registro_usuarios_ctk.model.usuario_model import GestorUsuarios
from registro_usuarios_ctk.view.main_view import MainView


class AppController:
    def __init__(self):
        self.modelo = GestorUsuarios()
        self.vista = MainView()

        self.refrescar_lista_usuarios()

    def iniciar(self):
        self.vista.mainloop()

    # --- CARGA LA LISTA INICIAL ---
    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.vista.actualizar_lista_usuarios(
            usuarios,
            self.seleccionar_usuario   # callback
        )

    # --- CALLBACK CUANDO SE HACE CLIC ---
    def seleccionar_usuario(self, indice):
        usuario = self.modelo.obtener(indice)
        self.vista.mostrar_detalles_usuario(usuario)
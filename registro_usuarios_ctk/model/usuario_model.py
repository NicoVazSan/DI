class Usuario:
    def __init__(self, nombre, edad, genero, avatar="-"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 28, "Femenino"))
        self._usuarios.append(Usuario("Luis Pérez", 34, "Masculino"))
        self._usuarios.append(Usuario("Sofía Romero", 22, "Femenino"))

    def listar(self):
        return self._usuarios

    def obtener(self, indice):
        return self._usuarios[indice]
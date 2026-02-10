import csv
from pathlib import Path

class Usuario:
    def __init__(self, nombre, edad, genero, avatar="-"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

        self.DATA_DIR = Path(__file__).resolve().parent.parent / "data"
        self.DATA_DIR.mkdir(exist_ok=True)
        self.CSV_PATH = self.DATA_DIR / "usuarios.csv"

        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 28, "Femenino", "Avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 34, "Masculino", "Avatar2.png"))
        self._usuarios.append(Usuario("Sofía Romero", 22, "Femenino", "avatar3.png"))

    def listar(self):
        return self._usuarios

    def obtener(self, indice):
        return self._usuarios[indice]

    def guardar_csv(self):
        try:
            with self.CSV_PATH.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["nombre", "edad", "genero", "avatar"])
                for u in self._usuarios:
                    writer.writerow([u.nombre, u.edad, u.genero, u.avatar])
            return True
        except Exception:
            return False

    def cargar_csv(self):
        if not self.CSV_PATH.exists():

            return False
        try:
            with self.CSV_PATH.open("r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                try:
                    next(reader)
                except StopIteration:
                    return True

                self._usuarios.clear()
                for i, row in enumerate(reader, start=1):
                    try:
                        if not row:
                            continue
                        nombre = row[0].strip() if len(row) > 0 else "Sin nombre"
                        edad = int(row[1]) if len(row) > 1 and row[1].strip() != "" else 0
                        genero = row[2].strip() if len(row) > 2 else "Otro"
                        avatar = row[3].strip() if len(row) > 3 and row[3].strip() != "" else "-"
                        self._usuarios.append(Usuario(nombre, edad, genero, avatar))
                    except Exception:

                        continue
            return True
        except FileNotFoundError:
            return False
        except Exception:
            return False
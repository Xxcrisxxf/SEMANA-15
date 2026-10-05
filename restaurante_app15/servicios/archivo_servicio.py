import json
import os
from pathlib import Path
from typing import List, Dict

class ArchivoServicio:
    def __init__(self, 
                 ruta_productos: str = "datos/productos.json", 
                 ruta_usuarios: str = "datos/usuarios.json",
                 ruta_ventas: str = "datos/ventas.json"):
        base = Path(__file__).resolve().parents[1]
        self.ruta_productos = str(base / ruta_productos)
        self.ruta_usuarios = str(base / ruta_usuarios)
        self.ruta_ventas = str(base / ruta_ventas)

    def _asegurar_directorio(self, ruta: str):
        directorio = os.path.dirname(ruta)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def cargar_datos_productos(self) -> List[Dict]:
        if not os.path.exists(self.ruta_productos):
            return []
        try:
            with open(self.ruta_productos, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as error:
            raise ValueError(f"No se pudieron leer los datos: {error}") from error

    def guardar_datos_productos(self, lista_diccionarios: List[Dict]) -> bool:
        try:
            self._asegurar_directorio(self.ruta_productos)
            with open(self.ruta_productos, "w", encoding="utf-8") as f:
                json.dump(lista_diccionarios, f, indent=4, ensure_ascii=False)
            return True
        except OSError:
            return False

    def cargar_datos_usuarios(self) -> List[Dict]:
        if not os.path.exists(self.ruta_usuarios):
            return []
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as error:
            raise ValueError(f"No se pudieron leer los datos: {error}") from error

    def cargar_datos_ventas(self) -> List[Dict]:
        if not os.path.exists(self.ruta_ventas):
            return []
        try:
            with open(self.ruta_ventas, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as error:
            raise ValueError(f"No se pudieron leer los datos: {error}") from error

    def guardar_datos_ventas(self, lista_diccionarios: List[Dict]) -> bool:
        try:
            self._asegurar_directorio(self.ruta_ventas)
            with open(self.ruta_ventas, "w", encoding="utf-8") as f:
                json.dump(lista_diccionarios, f, indent=4, ensure_ascii=False)
            return True
        except OSError:
            return False

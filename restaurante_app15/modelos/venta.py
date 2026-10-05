from datetime import datetime

class Venta:
    def __init__(self, usuario_id: int, producto_codigo: str, cantidad: int, fecha: str = None):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def usuario_id(self) -> int:
        return self.__usuario_id

    @usuario_id.setter
    def usuario_id(self, nuevo_id: int):
        if nuevo_id <= 0:
            raise ValueError("El ID de usuario debe ser un número entero positivo.")
        self.__usuario_id = nuevo_id

    @property
    def producto_codigo(self) -> str:
        return self.__producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, nuevo_codigo: str):
        if not nuevo_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        self.__producto_codigo = nuevo_codigo.strip()

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        self.__cantidad = nueva_cantidad

    @property
    def fecha(self) -> str:
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha: str):
        self.__fecha = nueva_fecha

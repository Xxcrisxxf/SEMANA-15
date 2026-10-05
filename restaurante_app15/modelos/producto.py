import math

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo: str):
        if not nuevo_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        self.__codigo = nuevo_codigo.strip()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self.__nombre = nuevo_nombre.strip()

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str):
        if not nueva_categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = nueva_categoria.strip()

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: float):
        if not math.isfinite(nuevo_precio) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número finito mayor o igual a cero.")
        self.__precio = nuevo_precio

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        if isinstance(nuevo_stock, bool) or not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero mayor o igual a cero.")
        self.__stock = nuevo_stock

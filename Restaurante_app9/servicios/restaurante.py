from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self):
        # Lista (list) para manejar colecciones dinámicas de productos y usuarios
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

    # --- Operaciones para Productos ---
    def agregar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False
        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        return self.productos

    # Conjunto (set) para evitar categorías duplicadas
    def obtener_categorias_unicas(self) -> Set[str]:
        return {p.categoria for p in self.productos}

    # --- Operaciones para Usuarios ---
    def agregar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion):
            return False
        self.usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: int) -> Optional[Usuario]:
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios
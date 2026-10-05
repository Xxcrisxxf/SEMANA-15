from typing import List, Optional, Tuple
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, archivo_servicio: ArchivoServicio):
        self.archivo_servicio = archivo_servicio
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []
        self.ventas: List[Venta] = []
        self._cargar_informacion()

    def _cargar_informacion(self):
        # Cargar productos
        datos_prod = self.archivo_servicio.cargar_datos_productos()
        for item in datos_prod:
            try:
                p = Producto(
                    codigo=str(item["codigo"]),
                    nombre=str(item["nombre"]),
                    categoria=str(item["categoria"]),
                    precio=float(item["precio"]),
                    stock=int(item.get("stock", 0))
                )
                self.productos.append(p)
            except (KeyError, ValueError):
                continue

        # Cargar usuarios
        datos_user = self.archivo_servicio.cargar_datos_usuarios()
        for item in datos_user:
            try:
                u = Usuario(
                    identificacion=int(item["identificacion"]),
                    nombre=str(item["nombre"]),
                    correo=str(item["correo"]),
                    clave=str(item.get("clave", ""))
                )
                self.usuarios.append(u)
            except (KeyError, ValueError):
                continue

        # Cargar ventas
        datos_ventas = self.archivo_servicio.cargar_datos_ventas()
        for item in datos_ventas:
            try:
                v = Venta(
                    usuario_id=int(item["usuario_id"]),
                    producto_codigo=str(item["producto_codigo"]),
                    cantidad=int(item["cantidad"]),
                    fecha=str(item.get("fecha", ""))
                )
                self.ventas.append(v)
            except (KeyError, ValueError):
                continue

    def _guardar_productos(self) -> bool:
        lista_dict = [
            {
                "codigo": p.codigo,
                "nombre": p.nombre,
                "categoria": p.categoria,
                "precio": p.precio,
                "stock": p.stock
            }
            for p in self.productos
        ]
        return self.archivo_servicio.guardar_datos_productos(lista_dict)

    def _guardar_ventas(self) -> bool:
        lista_dict = [
            {
                "usuario_id": v.usuario_id,
                "producto_codigo": v.producto_codigo,
                "cantidad": v.cantidad,
                "fecha": v.fecha
            }
            for v in self.ventas
        ]
        return self.archivo_servicio.guardar_datos_ventas(lista_dict)

    def validar_acceso(self, usuario_id_str: str, clave_acceso: str) -> bool:
        if not usuario_id_str.strip() or not clave_acceso.strip():
            return False
        try:
            user_id = int(usuario_id_str.strip())
            clave = clave_acceso.strip()
            usuario = next((u for u in self.usuarios if u.identificacion == user_id), None)
            return usuario is not None and usuario.clave == clave
        except ValueError:
            return False

    # --- Operaciones CRUD de Productos ---
    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        codigo_clean = codigo.strip()
        return next((p for p in self.productos if p.codigo == codigo_clean), None)

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Tuple[bool, str]:
        if self.buscar_producto(codigo):
            return False, f"Ya existe un producto registrado con el código '{codigo}'."
        try:
            nuevo_p = Producto(codigo, nombre, categoria, precio, stock)
            self.productos.append(nuevo_p)
            if not self._guardar_productos():
                self.productos.remove(nuevo_p)
                return False, "No se pudo guardar el producto. Revise la carpeta datos."
            return True, "Producto registrado correctamente."
        except ValueError as e:
            return False, str(e)

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Tuple[bool, str]:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False, f"No existe ningún producto con el código '{codigo}'."
        try:
            # Validar todos los campos antes de cambiar el producto existente.
            actualizado = Producto(codigo, nombre, categoria, precio, stock)
            indice = self.productos.index(producto)
            self.productos[indice] = actualizado
            if not self._guardar_productos():
                self.productos[indice] = producto
                return False, "No se pudo guardar la actualización."
            return True, "Producto actualizado correctamente."
        except ValueError as e:
            return False, str(e)

    def eliminar_producto(self, codigo: str) -> Tuple[bool, str]:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False, f"No se encontró un producto con el código '{codigo}'."
        indice = self.productos.index(producto)
        self.productos.remove(producto)
        if not self._guardar_productos():
            self.productos.insert(indice, producto)
            return False, "No se pudo guardar la eliminación."
        return True, "Producto eliminado correctamente."

    # --- Operación de Registro de Ventas ---
    def registrar_venta(self, usuario_id: int, producto_codigo: str, cantidad: int) -> Tuple[bool, str]:
        usuario = next((u for u in self.usuarios if u.identificacion == usuario_id), None)
        if not usuario:
            return False, f"El usuario con ID '{usuario_id}' no está registrado."

        producto = self.buscar_producto(producto_codigo)
        if not producto:
            return False, f"El producto con código '{producto_codigo}' no existe."

        # La validación pertenece al servicio, no al callback de la ventana.
        if isinstance(cantidad, str):
            try:
                cantidad = int(cantidad)
            except ValueError:
                return False, "La cantidad debe ser un número entero válido."
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            return False, "La cantidad solicitada debe ser mayor a cero."

        if producto.stock < cantidad:
            return False, f"Stock insuficiente. Stock disponible: {producto.stock} unidades."

        # Reducir stock y registrar la transacción
        producto.stock -= cantidad
        nueva_venta = Venta(usuario_id, producto_codigo, cantidad)
        self.ventas.append(nueva_venta)

        # Persistir ambas colecciones actualizadas
        if not self._guardar_productos():
            producto.stock += cantidad
            self.ventas.remove(nueva_venta)
            return False, "No se pudo guardar el stock. Revise la carpeta datos."
        if not self._guardar_ventas():
            producto.stock += cantidad
            self.ventas.remove(nueva_venta)
            if not self._guardar_productos():
                return False, "Falló el guardado. Revise productos.json y ventas.json antes de continuar."
            return False, "No se pudo guardar la venta. Se restauró el stock."

        return True, f"¡Venta registrada con éxito! Total: ${ (producto.precio * cantidad):.2f}"

    def listar_productos(self) -> List[Producto]:
        return self.productos

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def listar_ventas(self) -> List[Venta]:
        return self.ventas

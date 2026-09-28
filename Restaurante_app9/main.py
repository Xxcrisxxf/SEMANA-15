from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Tupla (tuple) para almacenar información constante/estable del sistema
OPCIONES_MENU = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir"
)

def mostrar_menu():
    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for opcion in OPCIONES_MENU:
        print(opcion)
        if opcion.startswith("5") or opcion.startswith("7") or opcion.startswith("8"):
            print("-" * 40)

def ejecutar_registrar_producto(restaurante: Restaurante):
    print("\n--- Registrar Producto ---")
    try:
        codigo = input("Código del producto: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.agregar_producto(producto):
            print("\nProducto registrado correctamente.")
        else:
            print(f"\nError: Ya existe un producto con el código '{codigo}'.")
    except ValueError as e:
        print(f"\nError de validación: {e}")

def ejecutar_buscar_producto(restaurante: Restaurante):
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto:
        print("\nProducto encontrado:")
        producto.mostrar_informacion()
    else:
        print(f"\nNo se encontró ningún producto con el código '{codigo}'.")

def ejecutar_actualizar_producto(restaurante: Restaurante):
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    if not restaurante.buscar_producto(codigo):
        print(f"\nError: No existe un producto registrado con el código '{codigo}'.")
        return
    
    try:
        nuevo_nombre = input("Nuevo nombre: ").strip()
        nueva_categoria = input("Nueva categoría: ").strip()
        nuevo_precio = float(input("Nuevo precio: "))
        
        if restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
            print("\nProducto actualizado correctamente.")
    except ValueError as e:
        print(f"\nError de validación: {e}")

def ejecutar_eliminar_producto(restaurante: Restaurante):
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("\nProducto eliminado correctamente.")
    else:
        print(f"\nError: No se encontró un producto con el código '{codigo}'.")

def ejecutar_listar_productos(restaurante: Restaurante):
    print("\n--- Lista de Productos ---")
    productos = restaurante.listar_productos()
    if productos:
        for p in productos:
            p.mostrar_informacion()
    else:
        print("No existen productos registrados.")

def ejecutar_registrar_usuario(restaurante: Restaurante):
    print("\n--- Registrar Usuario ---")
    try:
        identificacion = int(input("Identificación (ID): "))
        nombre = input("Nombre completo: ").strip()
        correo = input("Correo electrónico: ").strip()
        
        usuario = Usuario(identificacion, nombre, correo)
        if restaurante.agregar_usuario(usuario):
            print("\nUsuario registrado correctamente.")
        else:
            print(f"\nError: Ya existe un usuario registrado con el ID {identificacion}.")
    except ValueError as e:
        print(f"\nError de validación: {e}")

def ejecutar_listar_usuarios(restaurante: Restaurante):
    print("\n--- Lista de Usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if usuarios:
        for u in usuarios:
            u.mostrar_informacion()
    else:
        print("No existen usuarios registrados.")

def ejecutar_mostrar_categorias(restaurante: Restaurante):
    print("\n--- Categorías Registradas ---")
    categorias = restaurante.obtener_categorias_unicas()
    if categorias:
        for cat in categorias:
            print(f"- {cat}")
    else:
        print("No hay categorías disponibles.")

def main():
    restaurante = Restaurante()

    # Diccionario (dict) para mapear la opción seleccionada con su función correspondiente
    acciones = {
        "1": ejecutar_registrar_producto,
        "2": ejecutar_buscar_producto,
        "3": ejecutar_actualizar_producto,
        "4": ejecutar_eliminar_producto,
        "5": ejecutar_listar_productos,
        "6": ejecutar_registrar_usuario,
        "7": ejecutar_listar_usuarios,
        "8": ejecutar_mostrar_categorias
    }

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion in acciones:
            acciones[opcion](restaurante)
        elif opcion == "9":
            print("\nGracias por utilizar el Sistema de Restaurante.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
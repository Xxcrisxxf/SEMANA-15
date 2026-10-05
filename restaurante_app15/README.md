 nombre: Cristian Jair Bravo Chimborazo  
## Propósito

Continuar el proyecto de restaurante de las semanas anteriores y demostrar cómo una acción del usuario inicia una operación mediante un botón, `command=` y un callback. La operación de venta relaciona un usuario registrado con un producto y conserva el resultado en un archivo JSON.

## Evolución del proyecto

Se mantienen el inicio de sesión, la navegación por pestañas, la gestión de productos y la consulta de usuarios. La sección **Gestión de Ventas** permite seleccionar un usuario y un producto, ingresar una cantidad y registrar la operación. El proyecto conserva sus carpetas de datos, modelos, servicios, interfaz y recursos visuales.

Se ajustaron las dimensiones de la ventana, las tablas, el logo y los iconos para que los controles se presenten ordenados. Se conservan los botones Registrar, Consultar, Actualizar, Eliminar y Limpiar Campos de productos. La consulta de un producto se realiza escribiendo su código y presionando Consultar.

## Estructura
Repositorio GitHub
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   ├── usuarios.json
│   │   └── ventas.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── usuario.py
│   │   └── venta.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   ├── assets/              
│   └── main.py
└── README.md


## Gestión de ventas y manejo de eventos

En `MainView`, el botón **Registrar Venta** se configura así:

```python
command=self._callback_registrar_venta
```

Se pasa el método **sin paréntesis**, para ejecutarlo cuando el usuario presione el botón.

1. El usuario selecciona un responsable y un producto, e ingresa una cantidad.
2. El botón ejecuta `_callback_registrar_venta()`.
3. El callback obtiene las selecciones y llama a `RestauranteServicio.registrar_venta()`.
4. El servicio verifica que existan el usuario y el producto, que la cantidad sea un entero positivo y que haya stock suficiente.
5. El servicio crea un objeto `Venta`, descuenta las existencias y delega el guardado a `ArchivoServicio`.
6. El callback llama a `cargar_datos()` para actualizar las tablas y muestra el resultado mediante `messagebox`.

El callback coordina la interacción; las reglas de venta permanecen en el servicio. La interfaz no abre ni escribe archivos JSON. Esta actividad utiliza `command=`; no incorpora `bind()`, doble clic, `TreeviewSelect` ni búsquedas reactivas.

## Persistencia

`ventas.json` guarda la identificación del usuario, código del producto, cantidad y fecha de cada venta. `productos.json` conserva el stock actualizado. Al iniciar de nuevo, el servicio carga la información guardada y la interfaz vuelve a mostrar las ventas.

Se conservaron los datos y credenciales del archivo entregado. El registro original con código `P001` se mantiene tal como estaba, aunque ese código no figura en el catálogo actual. Las ventas nuevas solo admiten productos existentes con stock.

## Ejecución

Requisito: Python 3 con Tkinter. No se requieren paquetes adicionales de pip.

1. Abrir el proyecto en visual studio code.
2. Abrir una terminal y entrar en la carpeta `restaurante_app`.
3. Ejecutar:

```bash
python main.py
```

4. Ingresar con el ID y la contraseña registrados en `datos/usuarios.json`.
5. Abrir Gestión de Ventas, seleccionar usuario y producto, indicar la cantidad y presionar Registrar Venta.


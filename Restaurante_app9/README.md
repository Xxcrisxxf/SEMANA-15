Nombre : CRISTIAN JAIR BRAVO CHIMBORAZO
Descripción del sistema
Este proyecto representa la evolución del sistema de administración para un restaurante. Permite gestionar colecciones dinámicas de productos (registros, búsquedas, actualizaciones, eliminaciones y listados) y usuarios (registro y listado), manteniendo la persistencia en memoria organizada mediante estructuras de datos nativas de Python.
 La estructura de carpetas y archivos se distribuye de la siguiente manera:

Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── usuarios.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md
Responsabilidad de Componentes
modelos/producto.py: Define la entidad Producto con sus atributos (código, nombre, categoría, precio) y validaciones mediante @property y @setter.

modelos/usuario.py: Define la entidad Usuario con sus atributos (identificación, nombre, correo) y validaciones de datos.

servicios/restaurante.py: Actúa como la capa de servicios encargada de manipular las colecciones del sistema (listas de productos y usuarios), implementando búsquedas, eliminaciones, actualizaciones y control de duplicados.

main.py: Interfaz por consola encargada de capturar los datos ingresados por el usuario, coordinar el flujo de la aplicación invocando los métodos del servicio Restaurante y presentar los resultados.

Justificación del Uso de Estructuras de Datos

List :Administra colecciones dinámicas de objetos Producto y Usuario en Restaurante, permitiendo operaciones de inserción, recorrido y eliminación.
Tuple: Mantiene inmutable la estructura e información de las opciones del menú principal en main.py durante toda la ejecución del programa.
Dict : Mapea las claves ingresadas por el usuario en main.py directamente a la función que debe ejecutarse, reduciendo bloques condicionales extensos.
Set : Garantiza la extracción de un listado de categorías únicas sin elementos duplicados a partir de los productos registrados.

ejecutar desed la terminal con python main.py

Reflexión sobre la Selección de Estructuras de Datos
Elegir la estructura de datos adecuada es fundamental para optimizar el rendimiento, la legibilidad y la integridad del software. Las listas proveen flexibilidad para colecciones dinámicas que cambian constantemente; las tuplas garantizan seguridad al impedir modificaciones accidentales en datos constantes del sistema.
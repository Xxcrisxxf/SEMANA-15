class Usuario:
    def __init__(self, identificacion: int, nombre: str, correo: str, clave: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.clave = clave

    @property
    def identificacion(self) -> int:
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, nueva_id: int):
        if nueva_id <= 0:
            raise ValueError("La identificación debe ser un entero positivo.")
        self.__identificacion = nueva_id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre.strip()

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        if not nuevo_correo.strip():
            raise ValueError("El correo no puede estar vacío.")
        self.__correo = nuevo_correo.strip()

    @property
    def clave(self) -> str:
        return self.__clave

    @clave.setter
    def clave(self, nueva_clave: str):
        if not nueva_clave.strip():
            raise ValueError("La contraseña no puede estar vacía.")
        self.__clave = nueva_clave.strip()

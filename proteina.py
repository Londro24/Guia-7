"""Clase padre de otras clases"""

class Proteina():
    """Esta clase representa una proteina"""
    def __init__(self, nombre, descripcion, secuencia):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__secuencia = secuencia
    def get_nombre(self):
        """Devuelve el nombre de la proteina"""
        return self.__nombre
    def set_nombre(self, nombre):
        """Coloca otro nombre a una proteina"""
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El nombre debe ser un string, no se ha cambiado")
    def get_descripcion(self):
        """Devuelve la descripcion"""
        return self.__descripcion
    def set_descripcion(self, descripcion):
        """Coloca otra descripcion"""
        if isinstance(descripcion, str):
            self.__descripcion = descripcion
        else:
            print("La descripcion debe ser un string, no se ha cambiado")
    def get_secuencia(self):
        """Devuelve la secuencia"""
        return self.__secuencia
    def set_secuencia(self, secuencia):
        """Coloca otra secuencia"""
        if isinstance(secuencia, str):
            self.__secuencia = secuencia
        else:
            print("La secuencia debe ser un string, no se ha cambiado")
    def motrar_datos(self):
        """Muestra los datos generales de una proteina"""
        print("La proteina tiene las siguientes caracteristicas:"
            f"\nNombre: {self.__nombre}\nDescripcion: {self.__descripcion}"
            f"\nSecuencia: {self.__secuencia}\n")

"""Importa la clase base de esta clase"""
from proteina import Proteina

class ProteinaEnzimatica(Proteina):
    """Esta clase representa una proteina enzimatica"""
    def __init__(self, nombre, descripcion, secuencia, substrato):
        super().__init__(nombre, descripcion, secuencia)
        self.__substrato = substrato
    def get_substrato(self):
        """Devuelve el substrato"""
        return self.__substrato
    def set_substrato(self, substrato):
        """Coloca otro substrato"""
        if isinstance(substrato, str):
            self.__substrato = substrato
        else:
            pass
    def mostrar_substrato(self):
        """Muestra el susbtrato"""
        print(f"El substrato que lleva la enzima es: {self.__substrato}\n")

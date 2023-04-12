"""Importa la clase base para esta clase"""
from proteina import Proteina

class ProteinaEstructural(Proteina):
    """Esta clase representa una proteina estructural"""
    def __init__(self, nombre, descripcion, secuencia, tipo):
        super().__init__(nombre, descripcion, secuencia)
        self.__tipo = tipo
    def get_tipo(self):
        """Devuelve el tipo de proteina que es"""
        return self.__tipo
    def set_tipo(self, tipo):
        """Coloca otro tipo de proteina"""
        if isinstance(tipo, str):
            if tipo.upper() == 'GLOBULAR':
                self.__tipo = tipo
            elif tipo.upper() == 'FIBROSA':
                self.__tipo = tipo
        else:
            pass
    def mostrar_tipo(self):
        """Muestra el tipo de proteina que es"""
        print(f"Tipo de proteina estrcutural: {self.__tipo}\n")

"""Se importan clases de la libreria, para poder usarlas en el programa."""
from random import randint
from proteina import Proteina

class ProteinaMutante(Proteina):
    """Clase que representa una proteina mutante."""
    def __init__(self, nombre, descripcion, secuencia):
        super().__init__(nombre, descripcion, secuencia)
        self.__aa_mutante = randint(1, 51)
    def mostrar_mutacion(self):
        """Muestra la mutacion de la proteina."""
        print(f"La proteina mutante tiene una mutacion en el aminoacido "
            f"{self.__aa_mutante}\n")

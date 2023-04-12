"""Se importa la clase para verificar que se trabaje con proteinas"""
from proteina import Proteina

class SecuenciaProteica():
    """Esta clase muestras las secuencias de las proteinas"""
    def __init__(self):
        self.__proteinas = []
    def add_proteinas(self, proteina):
        """Agrega proteinas a una lista"""
        if isinstance(proteina, Proteina):
            self.__proteinas.append(proteina)
        else:
            print("No era una proteina")
    def get_proteinas(self):
        """Devuelve la lista de proteinas"""
        return self.__proteinas
    def mostrar_secuencia(self):
        """Muestra las secuencias por proteina"""
        for i in enumerate(self.__proteinas):
            print(i)
            print(f"La secuencia de la proteina "
                f"{self.__proteinas[i[0]].get_nombre()} es: "
                f"{self.__proteinas[i[0]].get_secuencia()}\n")

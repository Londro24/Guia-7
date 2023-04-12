"""Se importa la clase para verificar que se trabaje con proteinas"""
from proteina import Proteina

class AnalizadorProteico():
    """El objeto analiza varias proteinas"""
    def __init__(self):
        self.__proteinas = []
    def add_proteinas(self, proteina):
        """Agrega las proteínas a la lista de proteínas"""
        if isinstance(proteina, Proteina):
            self.__proteinas.append(proteina)
        else:
            print("No era una proteina")
    def get_proteinas(self):
        """Retorna una lista de proteinas"""
        return self.__proteinas
    def mostrar_porcentaje(self):
        """muestra porcentaje de aa hidrofobicos de cada proteina"""
        for i in enumerate(self.__proteinas):
            num = 0
            for j in self.__proteinas[i[0]].get_secuencia():
                if j in ["A", "V", "I", "L", "M", "F"]:
                    num += 1
            porcentaje = num / len(self.__proteinas[i[0]].get_secuencia()) * 100
            print(f"El porcentaje de aa hidrofobicos de la proteina "
                f"{self.__proteinas[i[0]].get_nombre()} es: "
                f"{porcentaje}%\n")
    def calcular_peso_molecular(self):
        """Se calcula el peso molecular de cada proteina"""
        print("Calculando peso molecular...")

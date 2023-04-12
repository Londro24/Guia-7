"""Se importan librerias para el proyecto"""
from random import randint
from proteina import Proteina
from proteina_estructural import ProteinaEstructural
from proteina_enzimatica import ProteinaEnzimatica
from proteina_mutante import ProteinaMutante
from secuencia_proteica import SecuenciaProteica
from analizador_proteico import AnalizadorProteico
aa = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P",
    "S", "T", "W", "Y", "V"]

def main():
    """Se ejecuta el programa principal"""
    sec1 = ""
    sec2 = ""
    sec3 = ""
    sec4 = ""
    for i in range (0,4):
        num = randint(51,201)
        for _ in range (0,num):
            num2 = randint(0,19)
            if i == 0:
                sec1 = sec1 + aa[num2]
            elif i == 1:
                sec2 = sec2 + aa[num2]
            elif i == 2:
                sec3 = sec3 + aa[num2]
            else:
                sec4 = sec4 + aa[num2]
    proteina1 = Proteina("3U3G", "STRUCTURE OF LC11-RNASE H1 ISOLATED FROM "
                        "COMPOST BY METAGENOMIC APPROACH: INSIGHT INTO THE "
                        "STRUCTURAL BASES FOR UNUSUAL ENZYMATIC PROPERTIES OF "
                        "STO-RNASE H1", sec1)
    proteina2 = ProteinaEstructural("7K09", "PUROMYCIN N-ACETYLTRANSFERASE IN "
                                    "COMPLEX WITH ACETYL-COA", sec2, "Globular")
    proteina3 = ProteinaEnzimatica("1PPI", "THE ACTIVE CENTER OF A MAMMALIAN "
                                "ALPHA-AMYLASE. THE STRUCTURE OF THE COMPLEX"
                                " OF A PANCREATIC ALPHA-AMYLASE WITH A "
                                "CARBOHYDRATE INHIBITOR REFINED TO 2.2 "
                                "ANGSTROMS RESOLUTION", sec3, "Agua")
    proteina1.motrar_datos()
    proteina2.motrar_datos()
    proteina2.mostrar_tipo()
    proteina3.motrar_datos()
    proteina3.mostrar_substrato()
    lista_proteina = SecuenciaProteica()
    lista_proteina.add_proteinas(proteina1)
    lista_proteina.add_proteinas(proteina2)
    lista_proteina.add_proteinas(proteina3)
    lista_proteina.mostrar_secuencia()
    proteina4 = ProteinaMutante("3YR6", "Hace cosas de proteinas, pero es una "
                                "mutacion", sec4)
    proteina4.motrar_datos()
    proteina4.mostrar_mutacion()
    lista_proteina2 = AnalizadorProteico()
    lista_proteina2.add_proteinas(proteina1)
    lista_proteina2.add_proteinas(proteina2)
    lista_proteina2.add_proteinas(proteina3)
    lista_proteina2.add_proteinas(proteina4)
    lista_proteina2.mostrar_porcentaje()
    lista_proteina2.calcular_peso_molecular()


if "__main__" == __name__:
    main()

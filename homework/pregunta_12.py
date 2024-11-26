"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_letra = {}

    with open("C:/Users/juana/OneDrive/Documentos/Github/UNAL_2024_2/Fundamentos de Analitica/2024-2-LAB-01-python-basico-JDave13/files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 4:
                letra = columns[0]
                claves_valores = columns[4].split(",")
                suma = sum(int(valor.split(":")[1]) for valor in claves_valores)
                if letra in suma_letra:
                    suma_letra[letra] += suma
                else:
                    suma_letra[letra] = suma

    return suma_letra
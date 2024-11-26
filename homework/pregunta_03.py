"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    suma_por_letra = {}
    with open("C:/Users/juana/OneDrive/Documentos/Github/UNAL_2024_2/Fundamentos de Analitica/2024-2-LAB-01-python-basico-JDave13/files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 1:
                letra = columns[0]  
                valor = int(columns[1]) 
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor
                else:
                    suma_por_letra[letra] = valor
    resultado = sorted(suma_por_letra.items())
    return resultado


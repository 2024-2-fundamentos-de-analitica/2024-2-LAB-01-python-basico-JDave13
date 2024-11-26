"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    max_min_letra = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                if letra in max_min_letra:
                    max_min_letra[letra] = (max(max_min_letra[letra][0], valor), min(max_min_letra[letra][1], valor))
                else:
                    max_min_letra[letra] = (valor, valor)

    resultado = [(letra, valor[0], valor[1]) for letra, valor in sorted(max_min_letra.items())]

    return resultado
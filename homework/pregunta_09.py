"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    count_clave = {}

    with open("C:/Users/juana/OneDrive/Documentos/Github/UNAL_2024_2/Fundamentos de Analitica/2024-2-LAB-01-python-basico-JDave13/files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 4:
                claves_valores = columns[4].split(",")
                for item in claves_valores:
                    clave, _ = item.split(":")
                    if clave in count_clave:
                        count_clave[clave] += 1
                    else:
                        count_clave[clave] = 1

    return count_clave
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    min_max_clave = {}
    with open("C:/Users/juana/OneDrive/Documentos/Github/UNAL_2024_2/Fundamentos de Analitica/2024-2-LAB-01-python-basico-JDave13/files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 4:
                claves_valores = columns[4].split(",")
                for item in claves_valores:
                    clave, valor = item.split(":")
                    valor = int(valor)
                    if clave in min_max_clave:
                        min_max_clave[clave] = (min(min_max_clave[clave][0], valor), max(min_max_clave[clave][1], valor))
                    else:
                        min_max_clave[clave] = (valor, valor)

    resultado = [(clave, valor[0], valor[1]) for clave, valor in sorted(min_max_clave.items())]

    return resultado

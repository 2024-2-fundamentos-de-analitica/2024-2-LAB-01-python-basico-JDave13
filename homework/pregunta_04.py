"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    sum_months = {}

    with open("C:/Users/juana/OneDrive/Documentos/Github/UNAL_2024_2/Fundamentos de Analitica/2024-2-LAB-01-python-basico-JDave13/files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) > 2:
                fecha = columns[2]
                mes = fecha.split("-")[1]
                if mes in sum_months:
                    sum_months[mes] += 1
                else:
                    sum_months[mes] = 1

    resultado = sorted(sum_months.items())

    return resultado

print(pregunta_04())
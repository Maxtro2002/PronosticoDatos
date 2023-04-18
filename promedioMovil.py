import numpy as np
import matplotlib.pyplot as plt


def promedioMovil(data, tam_ventana):
    prediccion = []
    for t in range(tam_ventana, len(data)):
        ventana = data[t - tam_ventana:t]
        promedioMovil = sum(ventana) / tam_ventana

        prediccion.append(promedioMovil)

    return prediccion


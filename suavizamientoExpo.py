import numpy as np
import matplotlib.pyplot as plt


def suavizado(data, alpha):
    prediccion = [data[0]]

    for t in range(1, len(data)):
        level = alpha * data[t] + (1 - alpha) * prediccion[t - 1]

        prediccion.append(level)

    return prediccion

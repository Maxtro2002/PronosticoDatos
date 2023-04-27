import numpy as np
import matplotlib.pyplot as plt


def suavizado(data):
    alfa = 0.3

    # Calcular la serie suavizada
    suavizado = []
    for i in range(len(data)):
        if i == 0:
            suavizado.append(data[i])
        else:
            suavizado.append(alfa * data[i] + (1 - alfa) * suavizado[i - 1])
    return suavizado

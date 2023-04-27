import numpy as np
import matplotlib.pyplot as plt


def suavizadoConTendencia(data):
    alfa = 0.3
    beta = 0.4

    suavizado = []
    tendencia = []
    valor = []
    for i in range(len(data)):
        if i == 0:
            suavizado.append(data[i])
            tendencia.append(0)
            valor.append(suavizado[i] + tendencia[i])
        else:
            suavizado.append(alfa * data[i] + (1 - alfa) * (suavizado[i-1] + tendencia[i-1]))
            tendencia.append(beta * (suavizado[i] - suavizado[i-1]) + (1 - beta) * tendencia[i-1])
            valor.append(suavizado[i] + tendencia[i])
    return valor
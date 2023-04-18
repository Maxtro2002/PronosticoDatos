import numpy as np
import matplotlib.pyplot as plt

def proyeccionTend(data, periodos):
    n = len(data)
    x = np.arange(n)
    slope, intercept = np.polyfit(x, data, 1)

    projection = []
    for t in range(n, n+periodos):
        projection.append(slope*t + intercept)

    return projection



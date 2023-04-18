import numpy as np
import matplotlib.pyplot as plt

def minimosCuadrados(data, periodos):
    n = len(data)
    x = np.arange(n)
    X = np.vstack([x, np.ones(n)]).T

    m, b = np.linalg.lstsq(X, data, rcond=None)[0]

    projection = []
    for t in range(n, n+periodos):
        projection.append(m*t + b)

    return projection


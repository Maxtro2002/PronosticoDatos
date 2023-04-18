import numpy as np


def promedioMovil(x, v):
    return np.convolve(x, np.ones(v), 'valid') / v



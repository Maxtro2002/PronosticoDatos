import numpy as np
import matplotlib.pyplot as plt

from promedioMovil import promedioMovil

array = np.array([10, 12, 13, 16, 18, 17, 19, 20, 22, 23, 24, 26, 28, 30])
tam_ventana = 3

x = promedioMovil(array, tam_ventana)
y = array

plt.plot(x)
plt.title("Promedio movil")
plt.show()

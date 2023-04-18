import numpy as np
import matplotlib.pyplot as plt

from promedioMovil import promedioMovil
from suavizamientoExpo import suavizado
from proyeccionTendencia import proyeccionTend
from analisisMinimosCuadrados import minimosCuadrados

# ------------------------------------Promedio movil------------------------------------
data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

tam_ventana = 3

prediccion = promedioMovil(data, tam_ventana)

plt.plot(data, label='Datos')
plt.plot([None] * (tam_ventana - 1) + prediccion, label='Prediccion')
plt.legend()
plt.show()
# ----------------------------------------------------------------------------------------

# ------------------------------------Suavizado exponencial------------------------------------
data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

alpha = 0.3

prediccion = suavizado(data, alpha)

plt.plot(data, label='Datos')
plt.plot(prediccion, label='Prediccion')
plt.legend()
plt.show()

# ----------------------------------------------------------------------------------------

# ------------------------------------Proyeccion de tendencia------------------------------------
data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

periodos = 3

projection = proyeccionTend(data, periodos)

plt.plot(data, label='Datos')
plt.plot([None] * len(data) + projection, label='Proyeccion')
plt.legend()
plt.show()
# ----------------------------------------------------------------------------------------

# ------------------------------------Regrecion minimos cuadrados------------------------------------
data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

periodos = 3

projection = minimosCuadrados(data, periodos)

plt.plot(data, label='Datos')
plt.plot([None] * len(data) + projection, label='Proyeccion')
plt.legend()
plt.show()

# ----------------------------------------------------------------------------------------

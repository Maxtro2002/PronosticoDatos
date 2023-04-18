import numpy as np
import matplotlib.pyplot as plt

from promedioMovil import promedioMovil
from suavizamientoExpo import suavizado

#------------------------------------Promedio movil------------------------------------
data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

tam_ventana = 3

prediccion = promedioMovil(data, tam_ventana)

plt.plot(data, label='Data')
plt.plot([None] * (tam_ventana - 1) + prediccion, label='Prediccion')
plt.legend()
plt.show()
#----------------------------------------------------------------------------------------

#------------------------------------Suavizado exponencial------------------------------------
data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

alpha = 0.3

prediccion = suavizado(data, alpha)

plt.plot(data, label='Data')
plt.plot(prediccion, label='Prediccion')
plt.legend()
plt.show()


#----------------------------------------------------------------------------------------

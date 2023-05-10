import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from promedioMovil import promedioMovil
from suavizamientoExpo import suavizado
from suavizadoConTendencia import suavizadoConTendencia
from minimosCuadrados import minimosCuadrados
from error import calcular_error

"""
Metodos utilizados para analisis:
Promedio movil
Suavizado exponencial
Suavizado exponencial con tendencia
Minimos cuadrados
"""


array = pd.read_csv('ds_salaries.csv', header=0, delimiter=',')

print("\n------------------------DATASET------------------------\n")
data = array["salary_in_usd"].values
year = array["work_year"].values

coef = np.polyfit(year, data, 1)
poly1d_fn = np.poly1d(coef)

# ------------------------------------Promedio movil------------------------------------
tam_ventana = 3
prediccionM = promedioMovil(data, tam_ventana)
print("Promedio movil")
plt.plot(data, label='Datos')
plt.plot([None] * (tam_ventana - 1) + prediccionM, label='prediccionM')
plt.legend()
plt.show()
plt.plot(prediccionM, "o", color="blue")
plt.plot(year, poly1d_fn(year), color="red")
plt.show()
errorMovil = calcular_error(data, prediccionM)
print(f"El valor proyectado es {prediccionM[-1]}, y el error es de {errorMovil}")

# ------------------------------------Suavizado exponencial------------------------------------
prediccion = suavizado(data)
print("Suavizado exponencial")
plt.plot(data, label='Datos')
plt.plot(prediccion, label='Prediccion')
plt.legend()
plt.show()
plt.plot(prediccion, "o", color="blue")
plt.plot(year, poly1d_fn(year), color="red")
plt.show()
errorSuavizado = calcular_error(data, prediccion)
print(f"El valor proyectado es {prediccion[-1]}, y el error es de {errorSuavizado}")




# ------------------------------------Suavizado con tendencia------------------------------------
proyeccionST = suavizadoConTendencia(data)
print("Suavizado con tendencia")
plt.plot(data, label='Datos')
plt.plot([None] * len(data) + proyeccionST, label='Proyeccion')
plt.legend()
plt.show()
plt.plot(proyeccionST, "o", color="blue")
plt.plot(year, poly1d_fn(year), color="red")
plt.show()
errorSuavTend = calcular_error(data, proyeccionST)
print(f"El valor proyectado es {proyeccionST[-1]}, y el error es de {errorSuavTend}")




# ------------------------------------Minimos cuadrados------------------------------------
proyeccion = minimosCuadrados(data)
print("Minimos cuadrados")
plt.plot(data, label='Datos')
plt.plot([None] * len(data) + proyeccion, label='Proyeccion')
plt.legend()
plt.show()
plt.plot(proyeccion, "o", color="blue")
plt.plot(year, poly1d_fn(year), color="red")
plt.show()
errorMinimos = calcular_error(data, proyeccion)
print(f"El valor proyectado es {proyeccionST[-1]}, y el error es de {errorMinimos}")

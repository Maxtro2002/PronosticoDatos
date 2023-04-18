import numpy as np
import matplotlib.pyplot as plt
import csv

from promedioMovil import promedioMovil
from suavizamientoExpo import suavizado
from proyeccionTendencia import proyeccionTend
from analisisMinimosCuadrados import minimosCuadrados

with open('Mobile phone price.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("1. Promedio movil\n"
      "2. suavizamiento exponencial\n"
      "3. Proyeccion de tendencia\n"
      "4. Regrecion de minimos cuadrados\n"
      )

metodo = int(input("Ingrese el numero del metodo que desea usar:\n"))

invalido = True

data = np.array([10, 15, 13, 17, 20, 19, 22, 24, 23, 25])

tam_ventana = 3
alpha = 0.3
periodos = 3


while invalido:
    # ------------------------------------Promedio movil------------------------------------

    if metodo == 1:
        prediccion = promedioMovil(data, tam_ventana)

        plt.plot(data, label='Datos')
        plt.plot([None] * (tam_ventana - 1) + prediccion, label='Prediccion')
        plt.legend()
        plt.show()
        invalido = False

    elif metodo == 2:
        # ------------------------------------Suavizado exponencial------------------------------------
        prediccion = suavizado(data, alpha)

        plt.plot(data, label='Datos')
        plt.plot(prediccion, label='Prediccion')
        plt.legend()
        plt.show()
        invalido = False

    elif metodo == 3:
        # ------------------------------------Proyeccion de tendencia------------------------------------
        projection = proyeccionTend(data, periodos)

        plt.plot(data, label='Datos')
        plt.plot([None] * len(data) + projection, label='Proyeccion')
        plt.legend()
        plt.show()

    elif metodo == 4:
        # ------------------------------------Regrecion minimos cuadrados------------------------------------
        projection = minimosCuadrados(data, periodos)

        plt.plot(data, label='Datos')
        plt.plot([None] * len(data) + projection, label='Proyeccion')
        plt.legend()
        plt.show()


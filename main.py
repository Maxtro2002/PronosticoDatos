import matplotlib.pyplot as plt
import pandas as pd

from promedioMovil import promedioMovil
from suavizamientoExpo import suavizado
from suavizadoConTendencia import suavizadoConTendencia
from minimosCuadrados import minimosCuadrados

array = pd.read_csv('Mobile phone price.csv', header=0, delimiter=',')
print("\n------------------------DATASET------------------------\n")
print("\nQue datos deseas analizar:\n"
      "1. Storage\n"
      "2. RAM\n"
      "3. ScreenSize\n"
      "4. Battery\n"
      "5. Price\n")
datosDS = int(input("Ingrese el numero de los datos que desea usar:\n"))

invalidoDatos = True

while invalidoDatos:
    if datosDS == 1:
        data = array['Storage'].values
        invalidoDatos = False

    elif datosDS == 2:
        data = array['RAM'].values
        invalidoDatos = False

    elif datosDS == 3:
        data = array['ScreenSize'].values
        invalidoDatos = False

    elif datosDS == 4:
        data = array['Battery'].values
        invalidoDatos = False

    elif datosDS == 5:
        data = array['Price'].values
        invalidoDatos = False

    else:
        print("ERROR: Por favor seleccione una opcion validas")
        datosDS = int(input("Ingrese el numero de los datos que desea usar:\n"))

print("1. Promedio movil\n"
      "2. suavizamiento exponencial\n"
      "3. Suavizado con tendencia\n"
      "4. Minimos cuadrados\n"
      )

metodo = int(input("Ingrese el numero del metodo que desea usar:\n"))

invalidoMetodo = True

while invalidoMetodo:
    # ------------------------------------Promedio movil------------------------------------

    if metodo == 1:
        tam_ventana = int(input("ingrese el tamaño de ventana que desea utilizar:\n"))
        prediccion = promedioMovil(data, tam_ventana)

        plt.plot(data, label='Datos')
        plt.plot([None] * (tam_ventana - 1) + prediccion, label='Prediccion')
        plt.legend()
        plt.show()
        invalidoMetodo = False

    elif metodo == 2:
        # ------------------------------------Suavizado exponencial------------------------------------
        prediccion = suavizado(data)

        plt.plot(data, label='Datos')
        plt.plot(prediccion, label='Prediccion')
        plt.legend()
        plt.show()
        invalidoMetodo = False

    elif metodo == 3:
        # ------------------------------------Suavizado con tendencia------------------------------------
        proyeccion = suavizadoConTendencia(data)

        plt.plot(data, label='Datos')
        plt.plot([None] * len(data) + proyeccion, label='Proyeccion')
        plt.legend()
        plt.show()
        invalidoMetodo = False

    elif metodo == 4:
        # ------------------------------------Minimos cuadrados------------------------------------
        proyeccion = minimosCuadrados(data)

        plt.plot(data, label='Datos')
        plt.plot([None] * len(data) + proyeccion, label='Proyeccion')
        plt.legend()
        plt.show()
        invalidoMetodo = False

    else:
        print("ERROR: Por favor seleccione una opcion validas")
        metodo = int(input("Ingrese el numero del metodo que desea usar:\n"))


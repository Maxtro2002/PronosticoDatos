import matplotlib.pyplot as plt
import pandas as pd

from promedioMovil import promedioMovil
from suavizamientoExpo import suavizado
from suavizadoConTendencia import suavizadoConTendencia
from minimosCuadrados import minimosCuadrados

"""
Metodos utilizados para analisis:
Promedio movil
Suavizado exponencial
Suavizado exponencial con tendencia
Minimos cuadrados
"""


array = pd.read_csv('ds_salaries.csv', header=0, delimiter=',')
print(array["salary_in_usd"])
wait = input("")
repetir = True
while repetir:
    print("\n------------------------DATASET------------------------\n")
    data = array["salary_in_usd"].values

    # ------------------------------------Promedio movil------------------------------------
    tam_ventana = 3
    prediccionM = promedioMovil(data, tam_ventana)
    print("Promedio movil")
    plt.plot(data, label='Datos')
    plt.plot([None] * (tam_ventana - 1) + prediccionM, label='prediccionM')
    plt.legend()
    plt.show()
    plt.plot(prediccionM, 'o', color="blue", label='Tendencia')
    plt.show()

    # ------------------------------------Suavizado exponencial------------------------------------
    prediccion = suavizado(data)
    print("Suavizado exponencial")
    plt.plot(data, label='Datos')
    plt.plot(prediccion, label='Prediccion')
    plt.legend()
    plt.show()
    plt.plot(prediccion, 'o', color="blue", label='Tendencia')
    plt.show()



    # ------------------------------------Suavizado con tendencia------------------------------------
    proyeccion = suavizadoConTendencia(data)
    print("Suavizado con tendencia")
    plt.plot(data, label='Datos')
    plt.plot([None] * len(data) + proyeccion, label='Proyeccion')
    plt.legend()
    plt.show()
    plt.plot(proyeccion, 'o', color="blue", label='Tendencia')
    plt.show()


    # ------------------------------------Minimos cuadrados------------------------------------
    proyeccion = minimosCuadrados(data)
    print("Minimos cuadrados")
    plt.plot(data, label='Datos')
    plt.plot([None] * len(data) + proyeccion, label='Proyeccion')
    plt.legend()
    plt.show()
    plt.plot(proyeccion, 'o', color="blue", label='Tendencia')
    plt.show()



    reset = input("Desea analisar otro dato?\n"
                      "1. Si\n"
                      "2. No\n")
    if reset != "1":
        repetir = False

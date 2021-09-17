""" Escribir una función que reciba una serie de Pandas con las notas 
de los alumnos de un curso y devuelva un diagrama de cajas con las notas.
El diagrama debe tener el título “Distribución de notas”. """

import matplotlib.pyplot as plt
import pandas as pd

def diagrama_caja(serie):
    fig, ax = plt.subplots()
    ax.boxplot(serie)
    
    return ax

def diagrama_caja_notas(notas):
    '''Función que construye un diagrama de cajas con las notas de los alumnos de un curso.
    
    Parámetros:
        - notas: Es una serie de Pandas con las notas de los alumnos.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos los sectores con las verntas a partir de la serie
    notas.plot(kind = 'box', ax = ax)
    # Eliminamos las marcas del eje x 
    plt.xticks([])
    # 
    # Añadimos el título
    plt.title('Distribución de notas')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax
    
notas = [4, 8, 7.5, 6, 5.5, 5.2, 3.5, 7.7, 3.2, 9, 6.8]
s_notas = pd.Series(notas)
diagrama_caja(s_notas)  
diagrama_caja_notas(s_notas) 
plt.show()
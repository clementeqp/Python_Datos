"""Escribir una función que reciba una serie de Pandas con el número
de ventas de un producto por años y una cadena con el tipo de gráfico 
a generar (lineas, barras, sectores, areas) y devuelva un diagrama del 
tipo indicado con la evolución de las ventas por años y con el título 
“Evolución del número de ventas”."""

import matplotlib.pyplot as plt
import pandas as pd


def evolucion_ventas(serie, tipo):
    fig, ax = plt.subplots()
    serie.plot(kind=graficos[tipo], ax=ax)
    plt.title('Evolucion del numero de ventas')
    
    return ax

graficos = {'lineas':'line', 'barras':'bar', 'sectores':'pie', 'area':'area'}
s_ventas = pd.Series([1200, 840, 1325, 1280, 1500], index = [2000, 2001, 2002, 2003, 2004])

evolucion_ventas(s_ventas, 'lineas')

evolucion_ventas(s_ventas, 'area')

evolucion_ventas(s_ventas, 'barras')

evolucion_ventas(s_ventas, 'sectores')
plt.show()
   
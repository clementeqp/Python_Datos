"""Escribir una función que reciba una serie de Pandas con el número
de ventas de un producto durante los meses de un trimestre y un título
y cree un diagrama de sectores con las ventas en formato png con el titulo dado.
El diagrama debe guardarse en un fichero con formato png y el título dado."""

import matplotlib.pyplot as plt
import pandas as pd

def diagrama_sectores(serie, titulo):
    fig, ax = plt.subplots()
    serie.plot(kind = 'pie', ax = ax)
    plt.ylabel('')
    plt.title(titulo)
    plt.savefig(titulo + '.png')
    return ax

ventas = {'Enero':200, 'Febrero':240, 'Marzo':310}
titulo='Ventas trimestre'
s_ventas=pd.Series(ventas)
diagrama_sectores(s_ventas, titulo)
# plt.show()

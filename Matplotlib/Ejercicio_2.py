""" 
Escribir una función que reciba un diccionario con las notas de 
las asignaturas de un curso y una cadena con el nombre de un color 
y devuelva un diagrama de barras de las notas en el color dado. 
"""

import matplotlib.pyplot as plt

def diagrama_barras(notas, color):
    fig, ax = plt.subplots()
    #ax.bar(notas.keys(), notas.values(), color=f'tab:{color}')
    ax.bar(notas.keys(), notas.values(), color=color)
    
    return ax
    
notas = {'Programación':9, 'Mates':6.5, 'Economía':4, 'Historia': 8}

diagrama_barras(notas, 'green')

plt.show()
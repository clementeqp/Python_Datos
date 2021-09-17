

""" Escribir una función que reciba un diccionario con las notas de los alumnos 
en curso en un examen y devuelva una serie con la nota mínima, la máxima, 
media y la desviación típica. """


import pandas as pd


notas_alumnos = {
    'Juan': 8.5,
    'Maria': 9.8,
    'Teresa': 7.3,
    'Pedro':4,
    'Carmen': 8.5,
    'Luis': 5
}

def estadistica_notas(notas):
    notas=pd.Series(notas)
    print(notas)
    results=pd.Series([notas.min(), notas.max(),notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviacion tipica'])
    return results

print(estadistica_notas(notas_alumnos))
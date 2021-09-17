"""
Escribir una función que reciba una diccionario con las notas 
de los alumnos en curso en un examen y devuelva una serie con las 
notas de los alumnos aprobados ordenadas de mayor a menor.
"""

import pandas as pd

notas_alumnos = {
    'Juan': 8.5,
    'Maria': 9.8,
    'Teresa': 7.3,
    'Pedro':4,
    'Carmen': 6.5,
    'Luis': 4.5
}

def aprobar(notas):
    notas=pd.Series(notas)
    aprobados=notas[notas>=5]
    aprobados=aprobados.sort_values(ascending=False)
    return aprobados
"""
def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)
print(aprobados(notas_alumnos))
"""

print(aprobar(notas_alumnos))
    
    

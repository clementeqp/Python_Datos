"""
Escribir un programa que pregunte al usuario por las ventas de un rango de años
y muestre por pantalla una serie con los datos de las ventas indexada por los años, 
antes y después de aplicarles un descuento del 10%.
"""

import pandas as pd


anyo_inicio = int(input("Introduce el año de inicio: "))
anyo_final = int(input("Introduce el año fial: "))

ventas = {}
for i in range(anyo_inicio,anyo_final+1):
    ventas[i] = float(input('Introduce las ventas del año '+ str(i) + ' :'))

ventas = pd.Series(ventas)
print('ventas\n', ventas)
print('\n')
print('Ventas con 10% de descuento\n', ventas*0.9)

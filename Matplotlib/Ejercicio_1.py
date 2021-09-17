"""
Escribir un programa que pregunte al usuario por las ventas de un rango 
de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.

plot(x, y): Dibuja un polígono con los vértices dados por las coordenadas 
de la lista x en el eje X y las coordenadas de la lista y en el eje Y. 
"""


import matplotlib.pyplot as plt

ventas=[]
anios=[i for i in range(2010,2022)]
""" for i in anios:
    input(f'Introduzca las ventas del año {i}: ')
    ventas.append(i) """
    
ventas=[25000, 26000, 30000, 34000, 35000, 36000, 32000,38000,39000, 41000, 32500,42000]
grafica, ax = plt.subplots()
#ax.plot(anios, ventas)
# opciones
ax.plot(anios, ventas, color = 'tab:purple', marker = 'o',linestyle = 'dashed', label = 'Ventas')
ax.set_title(
    'Ventas por años de Capullin system', 
    loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'} 
    )
ax.legend(loc = 'lower right')
plt.show()

"""
Alternativa con un diccionario

# Preguntamos por el año inicial
inicio = int(input('Introduce el año inicial: '))
# Preguntamos por el año final
fin = int(input('Introduce el año final: '))
# Definimos un diccionario vacío para guardar las ventas de cada año
ventas = {}
# Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
# i toma como valores los años desde el año de inicio hasta el año final
for i in range(inicio, fin+1):
    # Preguntamos por las ventas del año i y las guardamos en el diccionario con la clave el año y el valor las ventas
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
# Definimos la figura y los ejes del gráfico con Matplotlib
fig, ax = plt.subplots()
# Dibujamos la línea con las ventas a partir del diccionario
ax.plot(ventas.keys(), ventas.values())
# Mostarmos el gráfico por pantalla
plt.show()
"""

"""
Escribir un programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

Mes	    Ventas	Gastos
Enero	30500	22000
Febrero	35600	23400
Marzo	28300	18100
Abril	33900	20700

"""

import pandas as pd

datos = {
    'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas':[30500, 35600, 28300, 33900],
    'Gastos':[22000, 23400, 18100, 20700]
    }
dataframe=pd.DataFrame(data=datos)
print(dataframe)

datos2 = [['Enero', 30500, 22000], ['Febrero', 35600, 23400], ['Marzo', 28300, 18100], ['Abril', 33900,20700]]
filas=[]
for i in range(len(datos2)):
    filas.append(datos2[i][0])
    
print(filas)
print(datos.get('Mes'))
    

dataframe2=pd.DataFrame(datos2, index=filas, columns=datos.keys())
print(dataframe2)
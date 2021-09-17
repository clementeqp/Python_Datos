"""Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv
y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la 
ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. 
 Escribir un programa con los siguientes requisitos:"""
 
# Generar un DataFrame con los datos de los cuatro ficheros.
import pandas as pd
import datetime as dt
import numpy as np

file16='./datos/emisiones-2016.csv'
file17='./datos/emisiones-2017.csv'
file18='./datos/emisiones-2018.csv'
file19='./datos/emisiones-2019.csv'

emi16=pd.read_csv(file16, sep=';')
#print(emi16)
emi17=pd.read_csv(file17, sep=';')
emi18=pd.read_csv(file18, sep=';')
emi19=pd.read_csv(file19, sep=';')

emisiones=pd.concat([emi16, emi17, emi18, emi19])
print(emisiones)

# Filtrar las columnas del DataFrame para quedarse con las columnas 
# ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
columnas=['ESTACION', 'MAGNITUD', 'ANO', 'MES']
columnas.extend([col for col in emisiones if col.startswith('D')])
# print(columnas)
#emisiones_limpio=emisiones.loc[:,columnas]
#print(emisiones_limpio)
emisiones=emisiones[columnas]
print(emisiones)


# Reestructurar el DataFrame para que los valores de los contaminantes de las 
# columnas de los días aparezcan en una única columna.
emisiones=emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='Dias', value_name='Valor') 
print(emisiones)

# Añadir una columna con la fecha a partir de la concatenación del año,
# el mes y el día (usar el módulo datetime).

#Eliminamos el caracter D de Dias
emisiones.Dias = emisiones.Dias.str.strip('D')
print(emisiones)
# concatenamos las columnas
emisiones['FECHA']=emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.Dias.apply(str)

# convertimos la columna a fechas
emisiones['FECHA']=pd.to_datetime(emisiones.FECHA, format= '%Y/%m/%d', infer_datetime_format=True, errors='coerce')

print(emisiones)


# Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy)
# y ordenar el DataFrame por estaciones, contaminantes y fecha.

emisiones=emisiones.drop(emisiones[np.isnat(emisiones.FECHA)].index)
print (emisiones)
emisiones=emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])
print (emisiones)

# Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
print('Estaciones:', emisiones.ESTACION.unique())
print('Contaminantes:', emisiones.MAGNITUD.unique())

# Crear una función que reciba una estación, un contaminante y un rango de fechas y 
# devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.

def evolucion(estacion, contaminante, desde, hasta):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante) & (emisiones.FECHA>=desde) & (emisiones.FECHA <= hasta)].sort_values('FECHA')[['Valor', 'FECHA']]

print(evolucion(56, 8 , dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d')))

# Mostrar un resumen descriptivo (mímino, máximo, media, etc) para cada contaminante.
print(emisiones.groupby('MAGNITUD').Valor.describe())


# Mostrar un resumen descriptivo para cada contaminente por distritos.
print(emisiones.groupby([ 'ESTACION','MAGNITUD']).Valor.describe())

# Crear una función que reciba una estación y un contaminante y devuelva un resumen 
# descriptivo de las emisiones del contaminante indicado en la estadión indicada.

def resumen(estacion, contaminante):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].Valor.describe().round(2)

# Resumen de Dióxido de Nitrógeno en Plaza Elíptica
print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\n', resumen(56, 8),'\n', sep='')
# Resumen de Dióxido de Nitrógeno en Plaza del Carmen
print('Resumen Dióxido de Nitrógeno en Plaza del Carmen:\n', resumen(35, 8))


# Crear una función que devuelva las emisiones medias mensuales de un contaminante 
# y un año dados para todos las estaciones.

def resumen_mensual(contaminante, ano):
    
    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == ano)].groupby(['ESTACION','MES']).Valor.mean().unstack('MES')

print(resumen_mensual(8, 2019))


# Crear un función que reciba una estación de medición y devuelva un DataFrame con 
# las medias mensuales de los distintos tipos de contaminantes

def resumen_contaminantes(estacion):
    return emisiones[(emisiones.ESTACION == estacion)].groupby(['MAGNITUD', 'MES']).Valor.mean().unstack('MES')

print(resumen_contaminantes(8))
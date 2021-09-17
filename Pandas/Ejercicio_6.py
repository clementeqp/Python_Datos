"""
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35
con las siguientes columnas: 
nombre (nombre de la empresa), 
Final (precio de la 
acción al cierre de bolsa), 
Máximo (precio máximo de la acción durante la jornada),
Mínimo (precio mínimo de la acción durante la jornada), 
volumen (Volumen al cierre de bolsa),
Efectivo (capitalización al cierre en miles de euros). 
Construir una función que construya un DataFrame a partir del fichero
con el formato anterior y devuelva otro DataFrame 
con el mínimo, el máximo y la media de dada columna.
"""
import pandas as pd
path_file= './datos/cotizacion.csv'

def cotizar(file):
    df =pd.read_csv(file, sep=';', header=0, index_col=0, decimal=',')
    print(df)
    return df.describe()

print(cotizar(path_file).loc[['min', 'max', 'mean']])
print(cotizar(path_file).loc[['min', 'max', 'mean'], ['Final', 'Efectivo']])

def resumen_cotizaciones(file):
    df =pd.read_csv(file, sep=';', header=0, index_col=0, decimal=',',thousands='.')
    #print(df)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])

print(resumen_cotizaciones(path_file))

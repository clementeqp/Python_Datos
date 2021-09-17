"""
El fichero titanic.csv contiene información sobre los pasajeros del Titanic.
Escribir un programa con los siguientes requisitos:

    1-Generar un DataFrame con los datos del fichero.
    2-Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, 
        los nombres de sus columnas y filas, los tipos de datos de las columnas,
        las 10 primeras filas y las 10 últimas filas
    3-Mostrar por pantalla los datos del pasajero con identificador 148.
    4-Mostrar por pantalla las filas pares del DataFrame.
    5-Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
    6-Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
    7-Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
    8-Eliminar del DataFrame los pasajeros con edad desconocida.
    9-Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
    10-Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
    11-Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.

"""

import pandas as pd
path_file= './datos/titanic.csv'

# 1
titanic =pd.read_csv(path_file, sep=',', index_col=0)
#print(df)

# 2
def resumen_df(df):
    #print(df.info())
    print('Dimensiones:', titanic.shape)
    print('Número de elemntos:', titanic.size)
    print('Nombres de columnas:', titanic.columns)
    print('Nombres de filas:', titanic.index)
    print('Tipos de datos:\n', titanic.dtypes)
    print('Primeras 10 filas:\n', titanic.head(10))
    print('Últimas 10 filas:\n', titanic.tail(10))

resumen_df(titanic) 
 
#3
print(f'Pasajero 148:\n{titanic.loc[148]}')

#4
print(titanic.iloc[range(1,titanic.shape[0],2)])

#5
print(titanic[titanic["Pclass"]==1].sort_values('Name'))
print(titanic[titanic["Pclass"]==1]['Name'].sort_values())

#6

print("Sobrevivió un " + str(((titanic[titanic['Survived']==1].count()['Survived']/titanic.shape[0])*100).round(2)) + " %")
print((titanic[titanic['Survived']==0].count()['Survived']/titanic.shape[0])*100)

print(titanic['Survived'].value_counts()/titanic['Survived'].count() * 100)
print(titanic['Survived'].value_counts(normalize=True) * 100)

#7
print((titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100))

# 8-Eliminar del DataFrame los pasajeros con edad desconocida.

print(titanic.dropna(subset=['Age']))

# 9-Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.

print(titanic.groupby(['Pclass', 'Sex'])['Age'].mean().unstack()['female'].round(2))

# 10-Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.

mayores_edad=titanic['Age']>=18

    
titanic['Mayor_edad']=mayores_edad
print(titanic)

# 11-Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print((titanic.groupby(['Pclass', 'Mayor_edad'])['Survived'].value_counts(normalize=True) * 100).round(2))
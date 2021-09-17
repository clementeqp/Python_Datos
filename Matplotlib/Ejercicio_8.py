"""El fichero titanic.csv contiene información sobre los pasajeros del Titanic. 
Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

Diagrama de sectores con los fallecidos y supervivientes.
Histograma con las edades.
Diagrama de barras con el número de personas en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase."""

import pandas as pd
import matplotlib.pyplot as plt

file = './datos/titanic.csv'

titanic=pd.read_csv(file)
#print(titanic)


# Diagrama de sectores con los fallecidos y supervivientes.
fig, ax = plt.subplots()
titanic.Survived.value_counts().plot(kind='pie', labels=['Fallecidos', 'Supervivientes'], title = 'Distribucion deSupervivientes')
plt.ylabel('')
#plt.show()


# Histograma con las edades.
fig, ax = plt.subplots()
titanic.Age.plot(kind='hist', title='Histograma Edades')
#plt.show()

# Diagrama de barras con el número de personas en cada clase.
fig, ax = plt.subplots()
titanic.Pclass.value_counts().plot(kind='bar', title='Personas por Clase', color='red')
#plt.show()

# Otra forma
fig, ax = plt.subplots()
titanic.groupby("Pclass").size().plot(kind = "bar", title = "Número de personas por clase")
#plt.show()

# Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.

titanic.groupby(['Pclass','Survived']).size().unstack().plot(kind='bar', title = "Número de personas fallecidas y supervivientes por clase")
#plt.show()

# Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase

titanic.groupby(['Pclass','Survived']).size().unstack().plot(kind='bar',stacked=True, title = "Número de personas fallecidas y supervivientes por clase")
plt.show()
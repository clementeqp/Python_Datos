"""Escribir una función que reciba un dataframe de Pandas 
con los ingresos y gastos de una empresa por meses y devuelva 
un diagrama de líneas con dos líneas, una para los ingresos y 
otra para los gastos. El diagrama debe tener una leyenda identificando 
la línea de los ingresos y la de los gastos, un título con el nombre 
“Evolución de ingresos y gastos” y el eje y debe empezar en 0."""


import matplotlib.pyplot as plt
import pandas as pd



def diagrama_lineas(df):
    fig, ax = plt.subplots()
    ax.set_ylim([0, max(df.Ingresos.max(), df.Gastos.max()) + 500]) 
    #df.Ingresos.plot(kind='line', ax = ax, label='Ingresos')
    #df.Gastos.plot(kind='line', ax=ax, label='Gastos')
    #df.Total.plot(kind='line', ax=ax, label='Total')
    df.plot(ax=ax)
    plt.title('Evolucion de ingresos y gastos')
    ax.legend(loc = 'lower right')
    
    return ax
    
    
datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr','May'], 'Ingresos':[4500, 5200, 4800, 5300, 6200], 'Gastos':[2300, 2450, 2000, 2200, 2550]}
df_datos=pd.DataFrame(datos, index=datos['Mes'], columns=['Ingresos', 'Gastos'])
df_datos['Total']=df_datos['Ingresos']-df_datos['Gastos']
print(df_datos)
diagrama_lineas(df_datos)
plt.show()
    
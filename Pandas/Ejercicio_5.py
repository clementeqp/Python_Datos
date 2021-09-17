""" 
Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, 
una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

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
df=pd.DataFrame(datos)

def  calculo_balance(df):
    df['Balance'] = df.Ventas - df.Gastos
    return df

print(calculo_balance(df))

def  calculo_balance_meses(df, meses):
    df['Balance'] = df.Ventas - df.Gastos
    return df[df.Mes.isin(meses)].Balance.sum()

print(calculo_balance_meses(df, ['Enero', 'Marzo']), "€ total beneficio.")

contabilidad = pd.DataFrame(datos)

def balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad.set_index('Mes').loc[meses].Balance.sum()
    #return contabilidad.set_index('Mes').loc[meses,'Balance'].sum()

print(balance(contabilidad, ['Enero','Marzo']))
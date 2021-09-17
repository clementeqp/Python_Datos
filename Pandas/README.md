## La librería Pandas ==> import pandas as pd

Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos.

    - Define nuevas estructuras de datos basadas en los arrays de la librería NumPy pero con nuevas funcionalidades.
    - Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL.
    - Permite acceder a los datos mediante índices o nombres para filas y columnas.
    - Ofrece métodos para reordenar, dividir y combinar conjuntos de datos.
    - Permite trabajar con series temporales.
    - Realiza todas estas operaciones de manera muy eficiente.

#### Tipos de datos de Pandas

    - Series: Estructura de una dimensión.
    - DataFrame: Estructura de dos dimensiones (tablas).
    - Panel: Estructura de tres dimensiones (cubos).

#### La clase de objetos Series

Son estructuras similares a los arrays de una dimensión. Son homogéneas, es decir, sus elementos tienen que ser del mismo tipo, y su tamaño es inmutable, es decir, no se puede cambiar, aunque si su contenido.

Dispone de un índice que asocia un nombre a cada elemento del la serie, a través de la cuál se accede al elemento.

    - Creación de una serie a partir de una lista
        Series(data=lista, index=indices, dtype=tipo) : Devuelve un objeto de tipo Series con los datos de la lista lista, las filas especificados en la lista indices y el tipo de datos indicado en tipo. Si no se pasa la lista de índices se utilizan como índices los enteros del 0 al n-1, donde n es el tamaño de la serie. Si no se pasa el tipo de dato se infiere.
        ```
        >>> import pandas as pd
        >>> s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
        >>> print(s)
        0     Matemáticas
        1        Historia
        2        Economía
        3    Programación
        4          Inglés
        dtype: string
        ```

    - Creación de una serie a partir de un diccionario
        Series(data=diccionario, index=indices): Devuelve un objeto de tipo Series con los valores del diccionario diccionario y las filas especificados en la lista indices. Si no se pasa la lista de índices se utilizan como índices las claves del diccionario.
        ```
        >>> import pandas as pd
        >>> s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
        >>> print(s)
        Matemáticas     6.0
        Economía        4.5
        Programación    8.5
        dtype: float64
        ```

    - Atributos de una serie
        Existen varias propiedades o métodos para ver las características de una serie.

        s.size : Devuelve el número de elementos de la serie s.

        s.index : Devuelve una lista con los nombres de las filas del DataFrame s.

        s.dtype : Devuelve el tipo de datos de los elementos de la serie s.

    -Acceso a los elementos de una serie
         El acceso a los elementos de un objeto del tipo Series puede ser a través de posiciones o través de índices (nombres).

        - Acceso por posición
        Se realiza de forma similar a como se accede a los elementos de un array.

        s[i] : Devuelve el elemento que ocupa la posición i+1 en la serie s.
        s[nombres]: Devuelve otra serie con los elementos con los nombres de la lista nombres en el índice.
        - Acceso por índice
        s[nombre] : Devuelve el elemento con el nombre nombre en el índice.
        s[nombres] : Devuelve otra serie con los elementos correspondientes a los nombres indicadas en la lista nombres en el índice.
    - Resumen descriptivo de una serie
        Las siguientes funciones permiten resumir varios aspectos de una serie:

        - s.count() : Devuelve el número de elementos que no son nulos ni NaN en la serie s.
        - s.sum() : Devuelve la suma de los datos de la serie s cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
        - s.cumsum() : Devuelve una serie con la suma acumulada de los datos de la serie s cuando los datos son de un tipo numérico.
        - s.value_counts() : Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie s.
        - s.min() : Devuelve el menor de los datos de la serie s.
        - s.max() : Devuelve el mayor de los datos de la serie s.
        - s.mean() : Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico.
        - s.std() : Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico.
        - s.describe(): Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles.

    - Aplicar operaciones a una serie

        Los operadores binarios (+, \*, /, etc.) pueden utilizarse con una serie, y devuelven otra serie con el resultado de aplicar la         operación a cada elemento de la serie.

    - Aplicar funciones a una serie
        También es posible aplicar una función a cada elemento de la serie mediante el siguiente método:

        s.apply(f) : Devuelve una serie con el resultado de aplicar la función f a cada uno de los elementos de la serie s.

    - Filtrado de una serie
        Para filtrar una serie y quedarse con los valores que cumplen una determinada condición se utiliza el siguiente método:

        s[condicion] : Devuelve una serie con los elementos de la serie s que se corresponden con el valor True de la lista booleana condicion. condicion debe ser una lista de valores booleanos de la misma longitud que la serie.

    - Ordenar una serie
        Para ordenar una serie se utilizan los siguientes métodos:

        - s.sort_values(ascending=booleano) : Devuelve la serie que resulta de ordenar los valores la serie s. Si argumento del parámetro ascending es True el orden es creciente y si es False decreciente.

        - df.sort_index(ascending=booleano) : Devuelve la serie que resulta de ordenar el índice de la serie s. Si el argumento del parámetro ascending es True el orden es creciente y si es False decreciente.

    - Eliminar los dados desconocidos en una serie
        Los datos desconocidos representan en Pandas por NaN y los nulos por None. Tanto unos como otros suelen ser un problema a la hora de realizar algunos análisis de datos, por lo que es habitual eliminarlos. Para eliminarlos de una serie se utiliza el siguiente método:

        s.dropna() : Elimina los datos desconocidos o nulos de la serie s.

#### La clase de objetos DataFrame

    Un objeto del tipo DataFrame define un conjunto de datos estructurado en forma de tabla donde cada columna es un objeto de tipo Series, es decir, todos los datos de una misma columna son del mismo tipo, y las filas son registros que pueden contender datos de distintos tipos.

    Un DataFrame contiene dos índices, uno para las filas y otro para las columnas, y se puede acceder a sus elementos mediante los nombres de las filas y las columnas.

    Ejemplo. El siguiente DataFrame contiene información sobre los alumnos de un curso. Cada fila corresponde a un alumno y cada columna a una variable.

    - Creación de un DataFrame a partir de un diccionario de listas
        Para crear un DataFrame a partir de un diccionario cuyas claves son los nombres de las columnas y los valores son listas con los datos de las columnas se utiliza el método:

        DataFrame(data=diccionario, index=filas, columns=columnas, dtype=tipos) : Devuelve un objeto del tipo DataFrame cuyas columnas son las listas contenidas en los valores del diccionario diccionario, los nombres de filas indicados en la lista filas, los nombres de columnas indicados en la lista columnas y los tipos indicados en la lista tipos. La lista filas tiene que tener el mismo tamaño que las listas del diccionario, mientras que las listas columnas y tipos tienen que tener el mismo tamaño que el diccionario. Si no se pasa la lista de filas se utilizan como nombres los enteros empezando en 0. Si no se pasa la lista de columnas se utilizan como nombres las claves del diccionario. Si no se pasa la lista de tipos, se infiere.
        Los valores asociados a las claves del diccionario deben ser listas del mismo tamaño.

        ```
        >>> import pandas as pd
        >>> datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
        ... 'edad':[18, 22, 20, 21],
        ... 'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
        ... 'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
        ... }
        >>> df = pd.DataFrame(datos)
        >>> print(df)
            nombre  edad         grado             correo
        0    María    18      Economía    maria@gmail.com
        1     Luis    22      Medicina      luis@yahoo.es
        2   Carmen    20  Arquitectura   carmen@gmail.com
        3  Antonio    21      Economía  antonio@gmail.com
        ```

    - Creación de un DataFrame a partir de una lista de listas
        Para crear un DataFrame a partir de una lista de listas con los datos de las columnas se utiliza el siguiente método:

        DataFrame(data=listas, index=filas, columns=columnas, dtype=tipos) : Devuelve un objeto del tipo DataFrame cuyas columnas son los valores de las listas de la lista listas, los nombres de filas indicados en la lista filas, los nombres de columnas indicados en la lista columnas y los tipos indicados en la lista tipos. La lista filas, tiene que tener el mismo tamaño que la lista listas mientras que las listas columnas y tipos tienen que tener el mismo tamaño que las listas anidadas en listas. Si no se pasa la lista de filas o de columnas se utilizan enteros empezando en 0. Si no se pasa la lista de tipos, se infiere.
        Si las listas anidadas en listas no tienen el mismo tamaño, las listas menores se rellenan con valores NaN.

    - Creación de un DataFrame a partir de una lista de diccionarios
        Para crear un DataFrame a partir de una lista de diccionarios con los datos de las filas, se utiliza el siguiente método:

        DataFrame(data=diccionarios, index=filas, columns=columnas, dtype=tipos) : Devuelve un objeto del tipo DataFrame cuyas filas contienen los valores de los diccionarios de la lista diccionarios, los nombres de filas indicados en la lista filas, los nombres de columnas indicados en la lista columnas y los tipos indicados en la lista tipos. La lista filas tiene que tener el mismo tamaño que la lista lista. Si no se pasa la lista de filas se utilizan enteros empezando en 0. Si no se pasa la lista de columnas se utilizan las claves de los diccionarios. Si no se pasa la lista de tipos, se infiere.
        Si los diccionarios no tienen las mismas claves, las claves que no aparecen en el diccionario se rellenan con valores NaN.

    - Creación de un DataFrame a partir de un array
        Para crear un DataFrame a partir de un array de NumPy se utiliza el siguiente método:

        DataFrame(data=array, index=filas, columns=columnas, dtype=tipo) : Devuelde un objeto del tipo DataFrame cuyas filas y columnas son las del array array, los nombres de filas indicados en la lista filas, los nombres de columnas indicados en la lista columnas y el tipo indicado en tipo. La lista filas tiene que tener el mismo tamaño que el número de filas del array y la lista columnas el mismo tamaño que el número de columnas del array. Si no se pasa la lista de filas se utilizan enteros empezando en 0. Si no se pasa la lista de columnas se utilizan las claves de los diccionarios. Si no se pasa la lista de tipos, se infiere.
        ```
        >>> import pandas as pd
        >>> df = pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c'])
        >>> print(df)
                a         b         c
        0 -1.408238  0.644706  1.077434
        1 -0.279264 -0.249229  1.019137
        2 -0.805470 -0.629498  0.935066
        3  0.236936 -0.431673 -0.177379
        ```
    - Creación de un DataFrame a partir de un fichero CSV o Excel
        Dependiendo del tipo de fichero, existen distintas funciones para importar un DataFrame desde un fichero.

        read_csv(fichero.csv, sep=separador, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal) : Devuelve un objeto del tipo DataFrame con los datos del fichero CSV fichero.csv usando como separador de los datos la cadena separador. Como nombres de columnas se utiliza los valores de la fila n y como nombres de filas los valores de la columna m. Si no se indica m se utilizan como nombres de filas los enteros empezando en 0. Los valores incluídos en la lista no-validos se convierten en NaN. Para los datos numéricos se utiliza como separador de decimales el carácter indicado en separador-decimal.

        read_excel(fichero.xlsx, sheet_name=hoja, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal) : Devuelve un objeto del tipo DataFrame con los datos de la hoja de cálculo hoja del fichero Excel fichero.xlsx. Como nombres de columnas se utiliza los valores de la fila n y como nombres de filas los valores de la columna m. Si no se indica m se utilizan como nombres de filas los enteros empezando en 0. Los valores incluídos en la lista no-validos se convierten en NaN. Para los datos numéricos se utiliza como separador de decimales el carácter indicado en separador-decimal.

        ```

        >>> import pandas as pd
        >>> # Importación del fichero datos-colesteroles.csv
        >>> df = pd.read_csv(
        'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
        >>> print(df.head())
                                    nombre  edad sexo    peso    altura  colesterol
        0       José Luis Martínez Izquierdo    18    H    85.0    1.79         182.0
        1                     Rosa Díaz Díaz    32    M    65.0    1.73         232.0
        2              Javier García Sánchez    24    H     NaN    1.81         191.0
        3                Carmen López Pinzón    35    M    65.0    1.70         200.0
        4               Marisa López Collado    46    M    51.0    1.58         148.0
        ```
    - Exportación de ficheros
        También existen funciones para exportar un DataFrame a un fichero con diferentes formatos.

        - df.to_csv(fichero.csv, sep=separador, columns=booleano, index=booleano) : Exporta el DataFrame df al fichero fichero.csv en formato CSV usando como separador de los datos la cadena separador. Si se pasa True al parámetro columns se exporta también la fila con los nombres de columnas y si se pasa True al parámetro index se exporta también la columna con los nombres de las filas.

        - df.to_excel(fichero.xlsx, sheet_name = hoja, columns=booleano, index=booleano) : Exporta el DataFrame df a la hoja de cálculo hoja del fichero fichero.xlsx en formato Excel. Si se pasa True al parámetro columns se exporta también la fila con los nombres de columnas y si se pasa True al parámetro index se exporta también la columna con los nombres de las filas.

    - Atributos de un DataFrame
        Existen varias propiedades o métodos para ver las características de un DataFrame.

        - df.info() : Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y memoria usado) sobre el DataFrame df.

        - df.shape : Devuelve una tupla con el número de filas y columnas del DataFrame df.

        - df.size : Devuelve el número de elementos del DataFrame.

        - df.columns : Devuelve una lista con los nombres de las columnas del DataFrame df.

        - df.index : Devuelve una lista con los nombres de las filas del DataFrame df.

        - df.dtypes : Devuelve una serie con los tipos de datos de las columnas del DataFrame df.

        - df.head(n) : Devuelve las n primeras filas del DataFrame df.

        - df.tail(n) : Devuelve las n últimas filas del DataFrame df.

    - Renombrar los nombres de las filas y columnas
        Para cambiar el nombre de las filas y las columnas de un DataFrame se utiliza el siguiente método:

        df.rename(columns=columnas, index=filas): Devuelve el DataFrame que resulta de renombrar las columnas indicadas en las claves del diccionario columnas con sus valores y las filas indicadas en las claves del diccionario filas con sus valores en el DataFrame df.

    - Reindexar un DataFrame
        Para reordenar los índices de las filas y las columnas de un DataFrame, así como añadir o eliminar índices, se utiliza el siguiente método:

        df.reindex(index=filas, columns=columnas, fill_value=relleno) : Devuelve el DataFrame que resulta de tomar del DataFrame df las filas con nombres en la lista filas y las columnas con nombres en la lista columnas. Si alguno de los nombres indicados en filas o columnas no existía en el DataFrame df, se crean filan o columnas nuevas rellenas con el valor relleno.
    - Accesos mediante posiciones
        - df.iloc[i, j] : Devuelve el elemento que se encuentra en la fila i y la columna j del DataFrame df. Pueden indicarse secuencias de índices para obtener partes del DataFrame.

        - df.iloc[filas, columnas] : Devuelve un DataFrame con los elementos de las filas de la lista filas y de las columnas de la lista columnas.

        - df.iloc[i] : Devuelve una serie con los elementos de la fila i del DataFrame df.

    - Acceso a los elementos mediante nombres
        - df.loc[fila, columna] : Devuelve el elemento que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame df.
        - df.loc[filas, columnas] : Devuelve un DataFrame con los elemento que se encuentra en las filas con los nombres de la lista filas y las columnas con los nombres de la lista columnas del DataFrame df.

        - df[columna] : Devuelve una serie con los elementos de la columna de nombre columna del DataFrame df.

        - df.columna : Devuelve una serie con los elementos de la columna de nombre columna del DataFrame df. Es similar al método anterior pero solo funciona cuando el nombre de la columna no tiene espacios en blanco.

    - Operaciones con las columnas de un DataFrame
        Añadir columnas a un DataFrame
        El procedimiento para añadir una nueva columna a un DataFrame es similar al de añadir un nuevo par aun diccionario, pero pasando los valores de la columna en una lista o serie.

        - d[nombre] = lista: Añade al DataFrame df una nueva columna con el nombre nombre y los valores de la lista lista. La lista debe tener el mismo tamaño que el número de filas de df.

        - d[nombre] = serie: Añade al DataFrame df una nueva columna con el nombre nombre y los valores de la serie serie. Si el tamaño de la serie es menor que el número de filas de df se rellena con valores NaN mientras que si es mayor se recorta.
    
    - Operaciones sobre columnas
        Puesto que los datos de una misma columna de un DataFrame son del mismo tipo, es fácil aplicar la misma operación a todos los elementos de la columna.
        ```
        >>> import pandas as pd
        >>> df = pd.read_csv(
        'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
        >>> print(df['altura']*100)
        0     179
        1     173
        2     181
        ...

        >>> print(df['sexo']=='M')
        0     False
        1      True
        2     False
        ```

    -Aplicar funciones a columnas
        Para aplicar funciones a todos los elementos de una columna se utiliza el siguiente método:

        df[columna].apply(f) : Devuelve una serie con los valores que resulta de aplicar la función f a los elementos de la columna con nombre columna del DataFrame df.

    - Convertir una columna al tipo datetime
        A menudo una columna contiene cadenas que representan fechas. Para convertir estas cadenas al tipo datetime se utiliza el siguiente método:

        to_datetime(columna, formato): Devuelve la serie que resulta de convertir las cadenas de la columna con el nombre columna en fechas del tipo datetime con el formado especificado en formato.
    - Resumen descriptivo de un DataFrame
        Al igual que para las series, los siguientes métodos permiten resumir la información de un DataFrame por columnas:

        - df.count() : Devuelve una serie número de elementos que no son nulos ni NaN en cada columna del DataFrame df.
        - df.sum() : Devuelve una serie con la suma de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
        - df.cumsum() : Devuelve un DataFrame con la suma acumulada de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
        - df.min() : Devuelve una serie con los menores de los datos de las columnas del DataFrame df.
        - df.max() : Devuelve una serie con los mayores de los datos de las columnas del DataFrame df.
        - df.mean() : Devuelve una serie con las media de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
        - df.std() : Devuelve una serie con las desviaciones típicas de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
        - df.describe(include = tipo) : Devuelve un DataFrame con un resumen estadístico de las columnas del DataFrame df del tipo tipo. Para los datos numéricos (number) se calcula la media, la desviación típica, el mínimo, el máximo y los cuartiles de las columnas numéricas. Para los datos no numéricos (object) se calcula el número de valores, el número de valores distintos, la moda y su frecuencia. Si no se indica el tipo solo se consideran las columnas numéricas.

    - Eliminar columnas de un DataFrame
        Para eliminar columnas de un DataFrame se utilizan los siguientes métodos:

        - del df[nombre] : Elimina la columna con nombre nombre del DataFrame df.

        - df.pop(nombre) : Elimina la columna con nombre nombre del DataFrame df y la devuelve como una serie.

    - Operaciones con las filas de un DataFrame
        Añadir una fila a un DataFrame
        Para añadir una fila a un DataFrame se utiliza el siguiente método:

        - df.append(serie, ignore_index=True) : Devuelve el DataFrame que resulta de añadir una fila al DataFrame df con los valores de la serie serie. Los nombres del índice de la serie deben corresponderse con los nombres de las columnas de df. Si no se pasa el parámetro ignore_index entonces debe pasarse el parámetro name a la serie, donde su argumento será el nombre de la nueva fila.

    - Eliminar filas de un DataFrame
        Para eliminar filas de un DataFrame se utilizan el siguiente método:

        df.drop(filas) : Devuelve el DataFrame que resulta de eliminar las filas con los nombres indicados en la lista filas del DataFrame df.

    - Filtrado de las filas de un DataFrame
        Una operación bastante común con un DataFrame es obtener las filas que cumplen una determinada condición.

        - df[condicion] : Devuelve un DataFrame con las filas del DataFrame df que se corresponden con el valor True de la lista booleana condicion. condicion debe ser una lista de valores booleanos de la misma longitud que el número de filas del DataFrame.

    - Ordenar un DataFrame
        Para ordenar un DataFrame de acuerdo a los valores de una determinada columna se utilizan los siguientes métodos:

        - df.sort_values(columna, ascending=booleano) : Devuelve el DataFrame que resulta de ordenar las filas del DataFrame df según los valores del la columna con nombre columna. Si argumento del parámetro ascending es True el orden es creciente y si es False decreciente.

        - df.sort_index(ascending=booleano) : Devuelve el DataFrame que resulta de ordenar las filas del DataFrame df según los nombres de las filas. Si el argumento del parámetro ascending es True el orden es creciente y si es False decreciente.

    - Eliminar las filas con dados desconocidos en un DataFrame
        Para eliminar las filas de un DataFrame que contienen datos desconocidos NaN o nulos None se utiliza el siguiente método:

        - s.dropna(subset=columnas) : Devuelve el DataFrame que resulta de eliminar las filas que contienen algún dato desconocido o nulo en las columnas de la lista columna del DataFrame df. Si no se pasa un argumento al parámetro subset se aplica a todas las columnas del DataFrame.

    -Agrupación de un DataFrame
        En muchas aplicaciones es útil agrupar los datos de un DataFrame de acuerdo a los valores de una o varias columnas (categorías), como por ejemplo el sexo o el país.

        - Dividir un DataFrame en grupos
            Para dividir un DataFrame en grupos se utiliza el siguiente método:

            - df.groupby(columnas).groups : Devuelve un diccionario con cuyas claves son las tuplas que resultan de todas las combinaciones de los valores de las columnas con nombres en la lista columnas, y valores las listas de los nombres de las filas que contienen esos valores en las correspondientes columnas del DataFrame df.

            - df.groupby(columnas).get_group(valores) : Devuelve un DataFrame con las filas del DataFrame df que cumplen que las columnas de la lista columnas presentan los valores de la tupla valores. La lista columnas y la tupla valores deben tener el mismo tamaño.

    - Aplicar una función de agregación por grupos
        Una vez dividido el DataFame en grupos, es posible aplicar funciones de agregación a cada grupo mediante el siguiente método:

        - df.groupby(columnas).agg(funciones) : Devuelve un DataFrame con el resultado de aplicar las funciones de agregación de la lista funciones a cada uno de los DataFrames que resultan de dividir el DataFrame según las columnas de la lista columnas.
        Una función de agregación toma como argumento una lista y devuelve una único valor. Algunas de las funciones de agregación más comunes son:

        - np.min : Devuelve el mínimo de una lista de valores.
        - np.max : Devuelve el máximo de una lista de valores.
        - np.count_nonzero : Devuelve el número de valores no nulos de una lista de valores.
        - np.sum : Devuelve la suma de una lista de valores.
        - np.mean : Devuelve la media de una lista de valores.
        - np.std : Devuelve la desviación típica de una lista de valores.
    
    - Reestructurar un DataFrame
        A menudo la disposición de los datos en un DataFrame no es la adecuada para su tratamiento y es necesario reestructurar el DataFrame. Los datos que contiene un DataFrame pueden organizarse en dos formatos: ancho y largo.

        - Convertir un DataFrame a formato largo
            Para convertir un DataFrame de formato ancho a formato largo (columnas a filas) se utiliza el siguiente método:

            - df.melt(id_vars=id-columnas, value_vars=columnas, var_name=nombre-columnas, var_value=nombre-valores) : Devuelve el DataFrame que resulta de convertir el DataFrame df de formato ancho a formato largo. Todas las columnas de lista columnas se reestructuran en dos nuevas columnas con nombres nombre-columnas y nombre-valores que contienen los nombres de las columnas originales y sus valores, respectivamente. Las columnas en la lista id-columnas se mantienen sin reestructurar. Si no se pasa la lista columnas entonces se reestructuran todas las columnas excepto las columnas de la lista id-columnas.

        - Convertir un DataFrame a formato ancho
            Para convertir un DataFrame de formato largo a formato ancho (filas a columnas) se utiliza el siguiente método:

            - df.pivot(index=filas, columns=columna, values=valores) : Devuelve el DataFrame que resulta de convertir el DataFrame df de formato largo a formato ancho. Se crean tantas columnas nuevas como valores distintos haya en la columna columna. Los nombres de estas nuevas columnas son los valores de la columna columna mientras que sus valores se toman de la columna valores. Los nombres del índice del nuevo DataFrame se toman de los valores de la columna filas.
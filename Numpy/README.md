
## NUMPY ==> import numpy as np
-NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.
-Incorpora una nueva clase de objetos llamados arrays que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.
    -Un array es una estructura de datos de un mismo tipo organizada en forma de tabla o cuadrícula de distintas dimensiones.


- np.array(lista) : Crea un array a partir de la lista o tupla lista y devuelve una referencia a él.
    - Para una lista de valores se crea un array de una dimensión, también conocido como vector.
    - Para una lista de listas de valores se crea un array de dos dimensiones, también conocido como matriz.
    - Para una lista de listas de listas de valores se crea un array de tres dimensiones, también conocido como cubo.
    - Y así sucesivamente. No hay límite en el número de dimensiones del array más allá de la memoria disponible en el sistema.

##### Los elementos de la lista o tupla deben ser del mismo tipo.

-Ejemplos:
```
>>> # Array de una dimensión
>>> a1 = np.array([1, 2, 3])
>>> print(a1)
[1 2 3]
>>> # Array de dos dimensiones
>>> a2 = np.array([[1, 2, 3], [4, 5, 6]])
>>> print(a2)
[[1 2 3]
 [4 5 6]]
>>> # Array de tres dimensiones
>>> a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
>>> print(a3)
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

### Generacion de arrays especiales
- np.empty(dimensiones) : Crea y devuelve una referencia a un array vacío con las dimensiones especificadas en la tupla dimensiones.

= np.zeros(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos ceros.

- np.ones(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos unos.

- np.full(dimensiones, valor) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos valor.

- np.identity(n) : Crea y devuelve una referencia a la matriz identidad de dimensión n.

- np.arange(inicio, fin, salto) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia desde inicio hasta fin tomando valores cada salto.

- np.linspace(inicio, fin, n) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.

- np.random.random(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son aleatorios.

```
>>> print(np.zeros(3,2))
[[0. 0. 0.]
 [0. 0. 0.]]
>>> print(np.idendity(3))
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
>>> print(np.arange(1, 10, 2))
[1 3 5 7 9]
>>> print(np.linspace(0, 10, 5))
[ 0.   2.5  5.   7.5 10. ]
```

### Atributos de un arrays
- a.ndi : Devuelve el número de dimensiones del array a.

- a.shape : Devuelve una tupla con las dimensiones del array a.

- a.size : Devuelve el número de elementos del array a.

- a.dtype: Devuelve el tipo de datos de los elementos del array a.

### Acceso a elementos
- a[i, j] = a[i][j] ===>  Acceso al elemento de la fila i columna j.
- a[:, 0:2]         ===>  Todas las filas y columnas desde la 0 a la 1.

#### Filtrado
- a[condicion] : Devuelve una lista con los elementos del array a que cumplen la condición condicion.

## Operaciones
- Los operadores mamemáticos +, -, *, /, %, ** se utilizan para la realizar suma, resta, producto, cociente, resto y potencia a nivel de elemento.
- a.dot(b) : Devuelve el array resultado del producto matricial de los arrays a y b siempre y cuando sus dimensiones sean compatibles.
- a.T : Devuelve el array resultado de trasponer el array a.

```
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[1, 1], [2, 2], [3, 3]])
>>> print(a.dot(b))
[[14 14]
 [32 32]]
>>> print(a.T)
[[1 4]
 [2 5]
 [3 6]]
 ```
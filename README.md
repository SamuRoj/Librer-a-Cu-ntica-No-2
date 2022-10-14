# Teoría cuántica básica, observables y medidas

Librería realizada en Python que contiene operaciones entre vectores y matrices para determinar la solución a un problema cuántico, como la probabilidad de un estado de un vector, l transición de un vector a otro, entre otras.

## Para Empezar

### Prerequisitos

Lenguaje de programación Python, Idle o ejecución del programa desde terminal.

### Instalación y Ejecución

Descarga de los archivos LibQuantum2, LibQuantum.py, Matrix_Lib.py, Complex_Lib.py y Tests.py en un mismo directorio, además es necesario tener instalada la librería numpy, para la ejecución de una de las funciones que se encuentra dentro.

## Ejecución de Pruebas

### Archivo Tests.py

Dentro de este archivo se encuentran varias pruebas que se realizaron para verificar el programa, al ejecutarse Tests.py se observará el resultado de la operación y la validez de las pruebas junto con un formato de impresión de una matriz o vector dependiendo cual sea el caso.

```
Probabilidad de una posición particular.
0.69231
0.30769

Ran 1 test in 0.007s

OK
```

Si se quieren realizar más pruebas con otros valores se puede agregar la siguiente línea a la función `test_something` que se encuentra en el archivo Tests.py y se debe ejecutar nuevamente para observar los resultados.

```
Para realizar pruebas se debe escribir la siguiente línea:

self.assertAlmostEqual(Lib3.<Nombre de la función a usar>(Parámetros), <Resultado con el que se compara para verificar si la respuesta es válida>)

Se reemplazan los valores que se encuetran entre <>
```

### Archivo LibQuantum2.py

Contiene las funciones que permiten realizar las pruebas dependiendo del tipo de experimento que se quiera simular, entre ellos está el juego de las canicas, la doble rendija, múltiple rendija clásica, entre otros. Algunas de las funciones que se encuentran dentro de este archivo son:

```
Vectors(matrix)                     'Se encarga de dar un formato a los eigenvectores que retorna la función Eigenvectors.'            

Probability(vector, state)          'Dado un vector y una posición determina la probabilidad de que una partícula se encuentre en la posición solicitada.'

Transition(vector1, vector2)        'Dado dos vectores determina la probabilidad de que el vector 1 transite al vector 2.'

Mean(matrix, vector)                'Determina el valor esperado de una matriz y la matriz final luego de aplicar este.'

Variance(matrix, vector)            'Determina la varianza dados una matriz y un vector.'

Eigenvalues(matrix)                 'Determina los valores propios de una matriz.' 

Eigenvectors(matrix)                'Determina los vectores propios de una matriz.'

ProbabilityVector(state, vector)    'Determina la probabilidad de transitar de un estado inicial a un eigenvector.'

Dynamic(arrays, initial)            'Recibe un arreglo de matrices complejas y un estado inicial, determina si cada una de las matrices es unitaria y de ser así determina el estado final del sistema en el orden en que se dieron las matrices.s'
```

## Solución de los ejercicios propuestos

### Ejercicio 4.5.2



### Ejercicio 4.5.3
Este ejercicio propone un estado de ejemplo phi y se debe concluir si el estado que se da es separable o de lo contrario es entrelazado.

![Image Text]()

En la imagen anterior se expresan dos estados como se observa en la imagen, se propusieron los estados tsi y tsi prima, se realizó su producto tensor y se dió valores a cada una de las constantes c0, c1, c0 prima y c1 prima. Se puede ver que en este caso el estado final se puede expresar en términos de las constantes 0 y 1, para obtener el estado phi que se solicitaba por lo que se concluye que el estado es separable y no entrelazado.

## Realizado con

* [Pycharm] (https://www.jetbrains.com/pycharm/) The Python IDE for Professional Developers

## Autor

* **Samuel Rojas** [SamuRoj](https://github.com/SamuRoj)
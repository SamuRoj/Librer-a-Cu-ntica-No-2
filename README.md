# Programa simulación de lo clásico a lo cuántico

Librería realizada en Python que contiene operaciones entre vectores y matrices para determinar la solución a un problema cuántico, como la probabilidad de un estado de un vector, l transición de un vector a otro, entre otras operaciones.

## Para Empezar

### Prerequisitos

Lenguaje de programación Python, Idle o ejecución del programa desde terminal.

### Instalación y Ejecución

Descarga de los archivos LibQuantum.py, Matrix_Lib.py, Complex_Lib.py y Tests.py en un mismo directorio, además es necesario tener instalada la librería matplotlib.pyplot, para la ejecución de una de las funciones que se encuentra dentro.

## Ejecución de Pruebas

### Archivo Tests.py

Dentro de este archivo se encuentran varias pruebas que se realizaron para verificar el programa, al ejecutarse Tests.py se observará el resultado de la operación y la validez de las pruebas junto con un formato de impresión de una matriz o vector dependiendo cual sea el caso.

```
Juego de las canicas con las entradas de las matrices como fracciones

0.41666666665+0.0i  0.25+0.0i  0.33333333335+0.0i

Ran 1 test in 0.007s

OK
```

Si se quieren realizar más pruebas con otros valores se puede agregar la siguiente línea a la función `test_something` que se encuentra en el archivo Tests.py y se debe ejecutar nuevamente para observar los resultados.

```
Para realizar pruebas se debe escribir la siguiente línea:

self.assertAlmostEqual(Lib3.<Nombre de la función a usar>(Parámetros), <Resultado con el que se compara para verificar si la respuesta es válida>)

Se reemplazan los valores que se encuetran entre <>
```

### Archivo LibQuantum.py

Contiene las funciones que permiten realizar las pruebas dependiendo del tipo de experimento que se quiera simular, entre ellos está el juego de las canicas, la doble rendija, múltiple rendija clásica, entre otros. Algunas de las funciones que se encuentran dentro de este archivo son:

```
RoundDecimal(matrix)                    'Recibe una matriz y redondea cada uno de sus valores con 5 dígitos de precisión.'

MarblesGame(matrix, vector, clicks)     'Recibe una matriz, un vector y un entero llamado clicks que permite consultar el estado en que se encuentra el juego de las canicas, retorna el estado final.'

DecimalSlits(matrix, vector, clicks)    'Recibe una matriz, un vector y los clicks, se usa cuando las entradas de la matriz sean decimales o fracciones, retorna la matriz con valores redondeados.'

MultipleSlits(matrix, vector, slits, target, clicks)    'Permite ingresar la cantidad de rendijas, objetivos y clicks para simular diferentes experimentos, retorna el estado final de acuerdo a los datos que se ingresaron.'

MultipleSlitsQuantum(matrix, vector, slits, target, clicks)     'Recibe 5 parámetros y funciona de forma similar a la función MultipleSlits, solo que permite el trabajo con números complejos y la observación de fenómenos diferentes.'

Interference(vector, quantum)           'Recibe un vector que nazca de la acción de una matriz de números enteros y otro vector a partir de la acción de un matriz de números complejos, los compara y determina si ha sucedido lo que se conoce como el fenómeno de interferencia.'

BarGraph(vector)                        'Recibe un vector y realiza un gráfico de barras de acuerdo al estado del vector.'
```

## Realizado con

* [Pycharm] (https://www.jetbrains.com/pycharm/) The Python IDE for Professional Developers

## Autor

* **Samuel Rojas** [SamuRoj](https://github.com/SamuRoj)
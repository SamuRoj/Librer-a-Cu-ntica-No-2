import Matrix_Lib as Ml
import Complex_Lib as Cl
import matplotlib.pyplot as plt


def RoundDecimal(matrix):
    result = list(Ml.To_List(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(2):
                result[i][j][k] = round(result[i][j][k], 5)
    return result


# Juego de las canicas
def Clicks(matrix, vector, clicks):
    result = matrix
    for _ in range(clicks-1):
        result = Ml.Matrix_Product(result, matrix)
    return Ml.Matrix_Action(result, vector)


# Rendijas con fracciones
def DecimalSlits(matrix, vector, clicks):
    result = matrix
    for _ in range(clicks-1):
        result = Ml.Matrix_Product(result, matrix)
    result = RoundDecimal(list(Ml.To_List(result)))
    return Ml.Matrix_Action(result, vector)


# Múltiples Rendijas Clásico
def MultipleSlits(matrix, vector, slits, target, clicks):
    result = [[0 for _ in range(slits+target+1)] for _ in range(slits+target+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j]
    for _ in range(clicks-1):
        result = Ml.Matrix_Product(result, matrix)
    result = RoundDecimal(result)
    return Ml.Matrix_Action(result, vector)


# Múltiples rendijas cuántico
def MultipleSlitsQuantum(matrix, vector, slits, target, clicks):
    result = [[0 for _ in range(slits + target + 1)] for _ in range(slits + target + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j]
    for _ in range(clicks - 1):
        result = Ml.Matrix_Product(result, matrix)
    result = list(Ml.To_List(result))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j][0], result[i][j][1] = (Cl.Module(result[i][j]))**2, 0
    result = Ml.Matrix_Action(result, vector)
    result = list(map(list, result))
    for i in range(len(result)):
        result[i][0], result[i][1] = round(result[i][0], 5), round(result[i][1], 5)
    return tuple(map(tuple, result))


def Interference(vector, quantum):
    for i in range(len(vector)):
        if vector[i][0] != quantum[i][0]:
            return "Hay interferencia."
    return "No hay interferencia."


def BarGraph(vector):
    vector = list(map(list, vector))
    for i in range(len(vector)):
        vector[i] = vector[i][0]
    fig, axis = plt.subplots()
    axis.bar(range(len(vector)), vector, 0.5)
    axis.set_title("Probabilidades de vector de estados.")
    axis.set_ylabel("Probabilidad")
    axis.set_xlabel("Posición del vector")
    plt.show()


# Variables a usar para las pruebas
m1 = (((0, 0), (0, 0), (0, 0),  (0, 0), (0, 0), (0, 0)), ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
      ((0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (1, 0)), ((0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)), \
      ((0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)), ((1, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)))
v1 = ((0, 0), (0, 0), (27, 0), (0, 0), (0, 0), (0, 0))
m2 = (((0, 0), (1/6, 0), (5/6, 0)), ((1/3, 0), (1/2, 0), (1/6, 0)), ((2/3, 0), (1/3, 0), (0, 0)))
v2 = ((1/2, 0), (0, 0), (1/2, 0))
m3 = (((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (1/3, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (1/3, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (1/3, 0), (1/3, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)),\
        ((0, 0), (0, 0), (1/3, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)),\
        ((0, 0), (0, 0), (1/3, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)))
v3 = ((1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
m4 = (((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((1/(2**(1/2)), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((1/(2**(1/2)), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (-1/(6**(1/2)), 1/(6**(1/2))), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (-1/(6**(1/2)), -1/(6**(1/2))), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (1/(6**(1/2)), -1/(6**(1/2))), (-1/(6**(1/2)), 1/(6**(1/2))), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)),\
        ((0, 0), (0, 0), (-1/(6**(1/2)), -1/(6**(1/2))), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)),\
        ((0, 0), (0, 0), (1/(6**(1/2)), -1/(6**(1/2))), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)))
        
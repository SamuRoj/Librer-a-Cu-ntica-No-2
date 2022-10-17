import Complex_Lib as Cl

def RoundDecimal(matrix):
    result = list(To_List(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(2):
                result[i][j][k] = round(result[i][j][k], 0)
    return result

def To_List(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(list(map(list, matrix[i])))
    return result


def To_Tuple(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(tuple(map(tuple, matrix[i])))
    return tuple(result)

# Adición de vectores complejos
def Vector_Add(v1,v2):
    result = []
    for i in range(len(v1)):
        result.append(Cl.Complex_Sum(v1[i], v2[i]))
    return tuple(result)


# Inverso aditivo de un vector complejo
def Vector_Inverse(vector):
    vector = list(map(list, vector))
    for i in range(len(vector)):
        for j in range(2):
            vector[i][j] = (-1)*vector[i][j]
    return tuple(map(tuple, vector))


# Multiplicación de un escalar por un vector complejo
def Scalar_Product_Vector(num, vector):
    vector = list(map(list, vector))
    for i in range(len(vector)):
        vector[i] = Cl.Complex_Prod(num, vector[i])
    return tuple(map(tuple, vector))


# Adición de matrices
def Matrix_Add(m1, m2):
    result = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = Cl.Complex_Sum(m1[i][j], m2[i][j])
    return tuple(map(tuple, result))


# Inversa aditiva de matriz compleja
def Matrix_Inverse(matrix):
    matrix = To_List(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(2):
                matrix[i][j][k] = -1 * matrix[i][j][k]
    matrix = To_Tuple(matrix)
    return tuple(matrix)


# Multiplicación de un escalar por una matriz compleja
def Scalar_Product_Matrix(num, matrix):
    matrix = To_List(matrix)
    for i in range(len(matrix)):
        matrix[i] = Scalar_Product_Vector(num, matrix[i])
    matrix = To_Tuple(matrix)
    return tuple(matrix)


# Transpuesta de una matriz cuadrada o vector
def Transposed(element):
    if type(element[0][0]) == tuple:
        result = [[[0] for _ in range(len(element))] for _ in range(len(element[0]))]
        for i in range(len(element)):
            for j in range(len(element[0])):
                result[j][i] = element[i][j]
        result = To_Tuple(result)
    else:
        result = [[0] for _ in range(len(element))]
        for i in range(len(element)):
            result[i][0] = element[i]
        result = To_Tuple(result)
    return tuple(result)


# Conjugada de una matriz o vector
def Conjugate(element):
    if type(element[0][0]) == tuple or type(element[0][0]) == list:
        element = To_List(element)
        for i in range(len(element)):
            for j in range(len(element[0])):
                element[i][j] = Cl.Conjugate(element[i][j])
        return tuple(To_Tuple(element))
    else:
        element = list(map(list, element))
        for i in range(len(element)):
            element[i] = Cl.Conjugate(element[i])
        return tuple(element)


# Adjunta o daga de una matriz o vector
def Adjoint(element):
    if type(element[0][0]) == tuple:
        element = To_List(element)
    else:
        element = list(map(list, element))
    element = To_Tuple(Transposed(Conjugate(element)))
    return tuple(element)


# Producto de dos matrices
def Matrix_Product(m1, m2):
    m1, m2, result = To_List(m1), To_List(m2), [[[0] for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for k in range(len(m1)):
            total = [0, 0]
            for j in range(len(m2[0])):
                total = Cl.Complex_Sum(Cl.Complex_Prod(m1[i][j], m2[j][k]), total)
            result[i][k] = total
    result = To_Tuple(result)
    return tuple(result)


# Acción de una matriz sobre un vector
def Matrix_Action(matrix, vector):
    matrix, vector, result = To_List(matrix), list(map(list, vector)), [[0] for _ in range(len(vector))]
    for i in range(len(matrix)):
        for _ in range(len(matrix)):
            total = [0, 0]
            for j in range(len(vector)):
                total = Cl.Complex_Sum(Cl.Complex_Prod(matrix[i][j], vector[j]), total)
            result[i] = total
    return tuple(map(tuple, result))


# Producto Interno de un vector
def Dot_Product(v1, v2):
    v1, v2 = To_List(Adjoint(v1)), list(map(list, v2))
    for j in range(1):
        total = [0, 0]
        for i in range(len(v1)):
            total = Cl.Complex_Sum(Cl.Complex_Prod(v1[i][j], v2[i]), total)
    return tuple(total)


# Norma de un vector
def Magnitude(vector):
    aux, vector = To_List(Adjoint(vector)), list(map(list, vector))
    for j in range(1):
        total = [0, 0]
        for i in range(len(aux)):
            total = Cl.Complex_Sum(Cl.Complex_Prod(aux[i][j], vector[i]), total)
    return total[0]**(1/2)


# Distancia entre dos vectores
def Distance(v1, v2):
    return round(Magnitude(Vector_Add(v1, Vector_Inverse(v2))), 5)


# Determinar si una matriz dada es hermitiana
def Hermitian(matrix):
    aux = Adjoint(matrix)
    flag = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != aux[i][j]:
                flag = False
    if flag:
        return True
    return False


# Determinar si una matriz dada es unitaria
def Unitary(matrix):
    flag = True
    result = RoundDecimal(Matrix_Product(matrix, Adjoint(matrix)))
    identity = [[[1, 0] if i == j else [0, 0] for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] != identity[i][j]:
                flag = False
    if flag:
        return True
    return False


# Producto tensor entre dos matrices o vectores
def Tensor_Product(m1, m2):
    size, n, n2 = len(m1)*len(m2), len(m2), len(m2[0])
    m1, m2, result = To_List(m1), To_List(m2), [[[0] for _ in range(size)] for _ in range(size)]
    for j in range(size):
        for k in range(size):
            result[j][k] = Cl.Complex_Prod(m1[j // n][k // n2], m2[j % n][k % n2])
    result = To_Tuple(result)
    return tuple(result)


def print_vector(vector):
    print("  ".join(list(map(Cl.Print_Complex, vector))))


def print_matrix(matrix):
    for i in matrix:
        print("     ".join(list(map(Cl.Print_Complex, i))))
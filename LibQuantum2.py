import Complex_Lib as Cl
import Matrix_Lib as Ml
import LibQuantum as Ql
import numpy as np

def Vectors(matrix):
    result = [[] for _ in range(len(matrix))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i].append((matrix[j][i].real, matrix[j][i].imag))
    result = Ml.To_Tuple(result)
    return tuple(result)

def Probability(vector, state):
    # Normalización del vector
    magnitude = (Ml.Magnitude(vector))**2
    # Probabilidad del estado dado
    state = (Cl.Module(vector[state]))**2
    return round(state/magnitude, 5)

def Transition(vector1, vector2):
    # Producto Interno
    result = Ml.Dot_Product(vector2, vector1)
    magnitude = (Ml.Magnitude(vector1))*(Ml.Magnitude(vector2))
    result = list(result)
    # División de producto interno entre la multiplicación de la magnitud de los dos vectores
    for i in range(len(result)):
        result[i] = round(result[i]/magnitude, 5)
    return tuple(result)

def Mean(matrix, vector):
    identity = [[(1, 0) if i == j else (0, 0) for i in range(len(matrix[0]))] for j in range(len(matrix))]
    if Ml.Hermitian(matrix):
        mean = list(Ml.Dot_Product(Ml.Matrix_Action(matrix, vector), vector))
        result = Ml.Scalar_Product_Matrix(mean, identity)
        return tuple(result)
    return False

def Variance(matrix, vector):
    if Ml.Hermitian(matrix):
        hermitop = Ml.Matrix_Add(matrix, Ml.Matrix_Inverse(Mean(matrix, vector)))
        result = Ml.Matrix_Product(hermitop, hermitop)
        variance = Ml.Dot_Product(Ml.Matrix_Action(result, vector), vector)
        return tuple(variance)
    return False

def Eigenvalues(matrix):
    values, vectors = np.linalg.eigh(matrix)
    values = np.round(values, 5)
    return values

def Eigenvectors(matrix):
    values, vectors = np.linalg.eigh(matrix)
    vectors = np.round(vectors, 5)
    return vectors

def ProbabilityVector(state, vector):
    result = Transition(state, vector)
    result = Cl.Module((result)) ** 2
    return round(result, 5)



# Declaración de variables
v1 = ((0, 3), (-2, 0))
v2 = ((3, -4), (7, 2))
v3 = ((2, 5), (3, -2))
v4 = ((3, 2), (4, 4), (3, 0), (0, 8))
v5 = ((1, 0), (0, -1))
v6 = ((0, 1), (1, 0))
tsi = ((2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1))
phi = ((-1, -4), (2, -3), (-7, 6), (-1, 1), (-5, -3), (5, 0), (5, 8), (4, -4), (8, -7), (2, -7))
alpha = (((2**(1/2)/2), 0), ((-2**(1/2)/2), 0))
omega = (((3, 0), (1, 2)), ((1, -2), (-1, 0)))

print("Solución a ejercicios propuestos")
print()
print("Ejercicio 4.3.1")
spin = ((1,0), (0,0))
matrix = ((0+0j, 1+0j), (1+0j, 0+0j))
vectors = Vectors(Eigenvectors(matrix))
print(f"""Los estados a los que se puede transitar son:""")
for i in vectors:
    Ml.print_vector(i)
print()
print("Ejercicio 4.3.2")
print("Las probabilidades de transitar a algún eigenvector son:")
for i in vectors:
    print(ProbabilityVector(spin, i))
print()
print("Ejercicio 4.4.1")
u1 = (((0,0), (1,0)), ((1,0), (0,0)))
u2 = (((2**(1/2)/2,0), (2**(1/2)/2,0)), ((2**(1/2)/2,0), (-2**(1/2)/2,0)))
print(Ml.Unitary(u1))
print(Ml.Unitary(u2))
result = Ml.Matrix_Product(u1, u2)
print(Ml.Unitary(result))
print("Al ser todos los resultados True, se confirma que las matrices dadas y su producto son unitarias.")
print()
print("Ejericicio 4.4.2")
billiard = (((0,0), (1/2**(1/2),0), (1/2**(1/2),0), (0,0)),\
            ((0, 1/2**(1/2)), (0,0), (0,0), (1/2**(1/2), 0)),\
            ((1/2**(1/2), 0), (0,0), (0,0), (0, 1/2**(1/2))),\
            ((0,0), (1/2**(1/2),0), (-1/2**(1/2),0), (0,0)))
position = ((1,0), (0,0), (0,0), (0,0))
print(Probability(Ql.Clicks(billiard, position, 3), 3))
print("La probabilidad de que se encuentre en la posición 3 es de 0%")
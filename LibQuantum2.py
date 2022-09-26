import Complex_Lib as Cl
import Matrix_Lib as Ml

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


# Declaración de variables
v1 = ((0, 3), (-2, 0))
v2 = ((3, -4), (7, 2))
v3 = ((2, 5), (3, -2))
v4 = ((3, 2), (4, 4), (3, 0), (0, 8))
v5 = ((1, 0), (0, -1))
v6 = ((0, 1), (1, 0))
tsi = ((2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1))
phi = ((-1, -4), (2, -3), (-7, 6), (-1, 1), (-5, -3), (5, 0), (5, 8), (4, -4), (8, -7), (2, -7))
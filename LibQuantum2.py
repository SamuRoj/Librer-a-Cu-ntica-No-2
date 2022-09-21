import Complex_Lib as Cl
import Matrix_Lib as Ml

def Probability(vector, state):
    magnitude = (Ml.Magnitude(vector))**2
    state = (Cl.Module(vector[state]))**2
    return round(state/magnitude, 5)

def Transition(vector1, vector2):
    vector2 = Ml.Adjoint(vector2)
    result = Ml.Dot_Product(vector2, vector1)
    return result


# Declaración de variables
v1 = ((0, 3), (-2, 0))
v2 = ((0, 1), (-1, 0))
v3 = ((1, 0), (0, -1))
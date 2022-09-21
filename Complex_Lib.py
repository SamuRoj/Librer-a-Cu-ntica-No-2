import math

#Complex Sum
def Complex_Sum(num1, num2):
    real = num1[0] + num2[0]
    imaginary = num1[1] + num2[1]
    return (real, imaginary)

#Complex Product
def Complex_Prod(num1, num2):
    real = (num1[0]*num2[0]) - (num1[1]*num2[1])
    imaginary = (num1[0]*num2[1]) + (num1[1]*num2[0])
    return (real, imaginary)

#Complex Substraction
def Complex_Subs(num1, num2):
    real = num1[0] - num2[0]
    imaginary = num1[1] - num2[1]
    return (real, imaginary)

#Complex Division
def Complex_Div(num1, num2):
    module = (num2[0]**2) + (num2[1]**2)
    real = ((num1[0]*num2[0]) + (num1[1]*num2[1]))/module
    imaginary = ((num1[1]*num2[0]) - (num1[0]*num2[1]))/module
    return (real, imaginary)

#Module
def Module(num):
    return ((num[0]**2) + (num[1]**2))**(1/2)

#Conjugate
def Conjugate(num):
    return (num[0], -num[1])

#Conversion to Polar
def To_Polar(num):
    phase = Phase_Complex(num)
    module = Module(num)
    return (module, phase)

#Conversion to Cartesian
def To_Cartesian(num):
    a = num[0]*math.cos(num[1])
    b = num[0]*math.sin(num[1])
    return (round(a,7),round(b,7))

#Phase of a complex number
def Phase_Complex(num):
    if (num[0] >= 0 and num[1] >= 0) or (num[0] < 0 and num[1] >= 0):
        return math.atan2(num[1],num[0])
    elif (num[0] >= 0 and num[1] < 0) or (num[0] < 0 and num[1] < 0):
        return 2*math.pi + math.atan2(num[1],num[0])

#Printing the result with a new format
def Print_Complex(num):
    if num[1] >= 0:
        return (f'{num[0]}+{num[1]}i')
    else:
        return (f'{num[0]}{num[1]}i')

def Print_Polar(num):
    print(f"({num[0]}e^({num[1]}i)")
import LibQuantum2 as Lib
import Complex_Lib as Cl
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("Probabilidad de una posición particular.")
        print(Lib.Probability(Lib.v1, 0))
        self.assertAlmostEqual(Lib.Probability(Lib.v1, 0), 0.69231)
        print(Lib.Probability(Lib.v1, 1))
        self.assertAlmostEqual(Lib.Probability(Lib.v1, 1), 0.30769)
        print("Ejemplo Número 2")
        print(Lib.Probability(Lib.v2, 0))
        self.assertAlmostEqual(Lib.Probability(Lib.v2, 0), 0.32051)
        print(Lib.Probability(Lib.v2, 1))
        self.assertAlmostEqual(Lib.Probability(Lib.v2, 1), 0.67949)
        print("Ejemplo Número 3")
        print(Lib.Probability(Lib.v3, 0))
        self.assertAlmostEqual(Lib.Probability(Lib.v3, 0), 0.69048)
        print(Lib.Probability(Lib.v3, 1))
        self.assertAlmostEqual(Lib.Probability(Lib.v3, 1), 0.30952)
        print("Ejemplo Número 4")
        print(Lib.Probability(Lib.v4, 0))
        self.assertAlmostEqual(Lib.Probability(Lib.v4, 0), 0.11017)
        print(Lib.Probability(Lib.v4, 1))
        self.assertAlmostEqual(Lib.Probability(Lib.v4, 1), 0.27119)
        print(Lib.Probability(Lib.v4, 2))
        self.assertAlmostEqual(Lib.Probability(Lib.v4, 2), 0.07627)
        print(Lib.Probability(Lib.v4, 3))
        self.assertAlmostEqual(Lib.Probability(Lib.v4, 3), 0.54237)
        print("Transición de un vector a otro")
        print(Cl.Print_Complex(Lib.Transition(Lib.v5, Lib.v6)))
        self.assertAlmostEqual(Lib.Transition(Lib.v5, Lib.v6), (0, -1))
        print("Ejemplo Número 2")
        print(Cl.Print_Complex(Lib.Transition(Lib.tsi, Lib.phi)))
        self.assertAlmostEqual(Lib.Transition(Lib.tsi, Lib.phi), (-0.02056, -0.13019))

if  __name__ == '__main__':
    print(unittest.main())
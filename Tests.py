import LibQuantum2 as Lib
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("Probabilidad de una posición particular.")
        print(Lib.Probability(Lib.v1, 0))
        self.assertAlmostEqual(Lib.Probability(Lib.v1, 0), 0.69231)
        print("Probabilidad de transitar de un vector a otro.")
        print(Lib.Transition(Lib.v3, Lib.v2))
        self.assertAlmostEqual(Lib.Transition(Lib.v3, Lib.v2), 0)
        

if  __name__ == '__main__':
    print(unittest.main())
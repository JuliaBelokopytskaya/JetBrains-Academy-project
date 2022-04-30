from lab3 import *
import unittest


class FunTestCase(unittest.TestCase):
    """Tests for BMI calculation method"""

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after [" + self.shortDescription() + "]")

    def test_geometricMean(self):
        """Geometric mean test"""
        print("test id: " + self.id())
        self.assertEqual(geometric_mean(3,2,6), 12)

    def test_digitsNumbers(self):
        """Digits numbers test"""
        print("test id: " + self.id())
        a=digits_numbers(245)
        self.assertEqual(a,[5,4,2])

    def test_arithmeticMean(self):
        """Arithmetic test"""
        print("test id: " + self.id())
        self.assertEqual(arithmetic_mean(0,6,3), 3)

if __name__ == '__main__':
    unittest.main()

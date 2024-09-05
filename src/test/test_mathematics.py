from Maths.mathematics import summation, subtraction, multiplication
import unittest

class TestMathematics(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(summation(1,2),3)

    def test_subtraction(self):
        self.assertEqual(subtraction(1,2),-1)

    def test_multiplication(self):
        self.assertEqual(multiplication(1,2),2)

if __name__ == '__main__':
    unittest.main()

import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):

    def test_1(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)

    def test_2(self):
        with self.assertRaises(TypeError):
            factorial(3.14)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(None)

    def test_3(self):
        self.assertRaises(ValueError, factorial, -121)


    def test_4(self):
        with self.assertRaises(TypeError):
            factorial(1.99)


    def test_5(self):
        self.assertRaises(TypeError, factorial, "85")

    def test_6(self):
        for i in range(1, 15):
            self.assertGreater(factorial(i), 0)


    def test_7(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(12), 479001600)
        with self.assertRaises(ValueError):
            factorial(100)

if name == 'main':
    unittest.main()
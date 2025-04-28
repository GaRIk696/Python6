# Тестирование с unittest

import sys
import unittest

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
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_2(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_3(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_4(self):
        with self.assertRaises(ValueError):
            factorial(100000)
        with self.assertRaises(ValueError):
            factorial(sys.maxsize + 1)

    def test_5(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_6(self):
        self.assertIsInstance(factorial(4), int)

    def test_7(self):
        with self.assertRaises(TypeError):
            factorial(3.14)
        with self.assertRaises(TypeError):
            factorial(3.0)
        with self.assertRaises(TypeError):
            factorial("орпопрооп")
        with self.assertRaises(TypeError):
            factorial("6")


if __name__ == '__main__':
    unittest.main()

import simple_calc as s
import unittest


class Test_calc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(s.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(s.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(s.multiply(2, 2), 4)

    def test_division(self):
        self.assertEqual(s.divide(6, 3), 2)

    def test_add_params(self):
        test_cases = [(2, 2, 4), (5, 4, 9)]:
        for num1, num2, expected in test_cases
            with self.subTest(num1 = num1, num2 = num2, expected = expected)



if __name__ == '__main__':
    unittest.main()


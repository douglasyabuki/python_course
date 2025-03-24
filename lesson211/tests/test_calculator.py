try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from calculator import add


class TestCalculator(unittest.TestCase):
    def test_add_5_and_5_should_return_10(self):
        self.assertEqual(add(5, 5), 10)

    def test_add_minus5_and_5_should_return_0(self):
        self.assertEqual(add(-5, 5), 0)

    def test_add_various_inputs(self):
        x_y_outputs = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, expected = x_y_output
                self.assertEqual(add(x, y), expected)

    def test_add_x_not_int_or_float_should_raise_assertionerror(self):
        with self.assertRaises(AssertionError):
            add('11', 0)

    def test_add_y_not_int_or_float_should_raise_assertionerror(self):
        with self.assertRaises(AssertionError):
            add(11, '0')


if __name__ == '__main__':
    unittest.main(verbosity=2)

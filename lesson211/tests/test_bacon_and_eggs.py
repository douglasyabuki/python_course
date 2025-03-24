"""
TDD - Test Driven Development

Red
Step 1 -> Create the test and see it fail

Green
Step 2 -> Create the code and see the test pass

Refactor
Step 3 -> Improve the code
"""
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
from bacon_and_eggs import bacon_and_eggs


class TestBaconAndEggs(unittest.TestCase):
    def test_should_raise_assertion_error_if_input_is_not_int(self):
        with self.assertRaises(AssertionError):
            bacon_and_eggs('')

    def test_should_return_bacon_and_eggs_if_input_is_multiple_of_3_and_5(self):
        inputs = (15, 30, 45, 60)
        expected = 'Bacon and eggs'

        for i in inputs:
            with self.subTest(input=i, expected=expected):
                self.assertEqual(
                    bacon_and_eggs(i),
                    expected,
                    msg=f'"{i}" did not return "{expected}"'
                )

    def test_should_return_go_hungry_if_input_is_not_multiple_of_3_and_5(self):
        inputs = (1, 2, 4, 7, 8)
        expected = 'Go hungry'

        for i in inputs:
            with self.subTest(input=i, expected=expected):
                self.assertEqual(
                    bacon_and_eggs(i),
                    expected,
                    msg=f'"{i}" did not return "{expected}"'
                )

    def test_should_return_bacon_if_input_is_multiple_of_3_only(self):
        inputs = (3, 6, 9, 12, 18, 21)
        expected = 'Bacon'

        for i in inputs:
            with self.subTest(input=i, expected=expected):
                self.assertEqual(
                    bacon_and_eggs(i),
                    expected,
                    msg=f'"{i}" did not return "{expected}"'
                )

    def test_should_return_eggs_if_input_is_multiple_of_5_only(self):
        inputs = (5, 10, 20, 25, 35)
        expected = 'Eggs'

        for i in inputs:
            with self.subTest(input=i, expected=expected):
                self.assertEqual(
                    bacon_and_eggs(i),
                    expected,
                    msg=f'"{i}" did not return "{expected}"'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)

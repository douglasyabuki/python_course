"""
class Person
    __init__
        first_name str
        last_name str
        data_fetched bool (starts as False)

    API:
        fetch_all_data -> method
            OK
            404

            (data_fetched becomes True if data is fetched successfully)
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
from unittest.mock import patch
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('John', 'Doe')
        self.p2 = Person('Joe', 'Tho')

    def test_person_attr_first_name_has_correct_value(self):
        self.assertEqual(self.p1.first_name, 'John')
        self.assertEqual(self.p2.first_name, 'Joe')

    def test_person_attr_first_name_is_str(self):
        self.assertIsInstance(self.p1.first_name, str)
        self.assertIsInstance(self.p2.first_name, str)

    def test_person_attr_last_name_has_correct_value(self):
        self.assertEqual(self.p1.last_name, 'Doe')
        self.assertEqual(self.p2.last_name, 'Tho')

    def test_person_attr_last_name_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)
        self.assertIsInstance(self.p2.last_name, str)

    def test_person_attr_data_fetched_starts_false(self):
        self.assertFalse(self.p1.data_fetched)
        self.assertFalse(self.p2.data_fetched)

    def test_fetch_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.fetch_all_data(), 'CONNECTED')
            self.assertTrue(self.p1.data_fetched)

            self.assertEqual(self.p2.fetch_all_data(), 'CONNECTED')
            self.assertTrue(self.p2.data_fetched)

    def test_fetch_all_data_failure_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.fetch_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.data_fetched)

            self.assertEqual(self.p2.fetch_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.data_fetched)

    def test_fetch_all_data_success_then_failure_sequentially(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.fetch_all_data(), 'CONNECTED')
            self.assertTrue(self.p1.data_fetched)

            self.assertEqual(self.p2.fetch_all_data(), 'CONNECTED')
            self.assertTrue(self.p2.data_fetched)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.fetch_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.data_fetched)

            self.assertEqual(self.p2.fetch_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.data_fetched)


if __name__ == '__main__':
    unittest.main(verbosity=2)

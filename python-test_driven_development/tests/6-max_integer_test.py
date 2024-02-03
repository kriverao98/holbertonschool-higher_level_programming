# tests/6-max_integer_test.py

import unittest
from my_module import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        result = max_integer([1, 2, 3, 3, 2, 1])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()# tests/6-max_integer_test.py

import unittest
from my_module import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        result = max_integer([1, 2, 3, 3, 2, 1])
        self.assertEqual(result, 3)

    # BEGIN: Additional test cases
    def test_empty_string(self):
        result = max_integer("")
        self.assertIsNone(result)

    def test_max_at_beginning(self):
        result = max_integer([10, 5, 3, 2, 1])
        self.assertEqual(result, 10)

    def test_max_at_end(self):
        result = max_integer([1, 2, 3, 5, 10])
        self.assertEqual(result, 10)

    def test_max_in_middle(self):
        result = max_integer([1, 2, 10, 5, 3])
        self.assertEqual(result, 10)

    def test_all_same_numbers(self):
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)
    # END: Additional test cases

if __name__ == '__main__':
    unittest.main()

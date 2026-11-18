"""Тесты двоичного поиска"""
import unittest

from calc.arrays import binary_search, is_ordered


class SearchTests(unittest.TestCase):
    def test_found(self):
        values = [-76, -5, 24, 43, 81]
        for target in (-76, 24, 81):
            with self.subTest(target=target):
                index = binary_search(values, target)
                self.assertIsNotNone(index)
                self.assertEqual(values[index], target)

    def test_missing(self):
        self.assertIsNone(binary_search([-76, -5, 24, 43, 81], 0))

    def test_first_index(self):
        self.assertEqual(binary_search([-76, -5, 24, 43, 81], -76), 0)

    def test_duplicates(self):
        values = [-5, -5, 0, 0, 5]
        index = binary_search(values, -5)
        self.assertEqual(values[index], -5)

    def test_ordered_detection(self):
        self.assertTrue(is_ordered([-76, -5, 24, 43, 81]))
        self.assertFalse(is_ordered([3, 1, 2]))

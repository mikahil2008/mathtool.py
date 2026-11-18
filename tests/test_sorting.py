"""Тесты всех семи методов сортировки"""
import unittest

from calc import sorting


class SortingTests(unittest.TestCase):
    CASES = ([42], [5, 5, 5, 5], [3, 1, 3, 1, 2],
             [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 2, -1, 5])

    def test_methods(self):
        for method in sorting.METHODS:
            for case in self.CASES:
                for descending in (False, True):
                    with self.subTest(method=method, values=case,
                                      descending=descending):
                        values = case[:]
                        result = sorting.METHODS[method](values, descending)
                        self.assertIsNone(result)
                        expected = sorted(case, reverse=descending)
                        self.assertEqual(values, expected)

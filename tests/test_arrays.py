"""Тесты перемешивания Фишера-Йетса"""
import unittest

from calc.arrays import shuffle


class ShuffleTests(unittest.TestCase):
    def test_composition(self):
        original = [2, 2, -1, 5]
        values = original[:]
        result = shuffle(values, seed=1)
        self.assertIsNone(result)
        self.assertEqual(sorted(values), sorted(original))

    def test_reproducible(self):
        original = [3, 1, 4, 1, 5, -2]
        first, second = original[:], original[:]
        shuffle(first, seed=7)
        shuffle(second, seed=7)
        self.assertEqual(first, second)

    def test_edge_cases(self):
        for values in ([], [42], [5, 5, 5, 5], [2, 2, -1, 5]):
            with self.subTest(values=values):
                copy = values[:]
                shuffle(copy, seed=1)
                self.assertEqual(sorted(copy), sorted(values))
                self.assertEqual(len(copy), len(values))

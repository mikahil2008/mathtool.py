"""Тесты поиска порядковой статистики"""
import unittest

from calc.selection import statistic


class StatisticTests(unittest.TestCase):
    def test_sample_ranks(self):
        values = [12, 71, 35, 80, 61, 50, 87, 11, 20]
        for k, expected in ((1, 11), (4, 35), (9, 87)):
            with self.subTest(k=k):
                self.assertEqual(statistic(values[:], k, seed=1), expected)

    def test_duplicates(self):
        self.assertEqual(statistic([5, 2, 2, 9], 2, seed=1), 2)
        self.assertEqual(statistic([5, 2, 2, 9], 3, seed=1), 5)

    def test_all_ranks(self):
        original = [5, -1, 2, 2]
        expected = sorted(original)
        for k in range(1, len(original) + 1):
            with self.subTest(k=k):
                values = original[:]
                result = statistic(values, k, seed=1)
                self.assertEqual(result, expected[k - 1])
                self.assertEqual(sorted(values), expected)

    def test_single_and_equal(self):
        self.assertEqual(statistic([42], 1, seed=1), 42)
        self.assertEqual(statistic([7, 7, 7, 7], 3, seed=1), 7)

    def test_ordered_and_reverse(self):
        self.assertEqual(statistic([1, 2, 3, 4, 5], 3, seed=1), 3)
        self.assertEqual(statistic([5, 4, 3, 2, 1], 2, seed=1), 2)

    def test_different_seeds(self):
        original = [12, 71, 35, 80, 61, 50, 87, 11, 20]
        expected = sorted(original)
        for seed in (1, 7, 42):
            for k in (1, 4, 9):
                with self.subTest(seed=seed, k=k):
                    self.assertEqual(statistic(original[:], k, seed=seed),
                                     expected[k - 1])

    def test_bad_inputs(self):
        for k in (0, -1, 10, 1.5, True):
            with self.subTest(k=k):
                with self.assertRaises(ValueError):
                    statistic([1, 2, 3], k)
        with self.assertRaises(ValueError):
            statistic([], 1)

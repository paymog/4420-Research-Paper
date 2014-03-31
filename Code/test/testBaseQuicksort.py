from nose.tools import assert_true

__author__ = 'paymahnmoghadasian'

import unittest
from ..src.BaseQuicksort import BaseQuicksort

class testBaseQuicksort(unittest.TestCase):
    def setUp(self):
        self.qsort = BaseQuicksort(None)

    def test_lessThan(self):
        self.assertTrue(self.qsort.lessThan(1,2))
        self.assertEqual(self.qsort.numComparisons, 1)

        self.assertFalse(self.qsort.lessThan(2,1))
        self.assertEqual(self.qsort.numComparisons, 2)

    def test_lessThanEqual(self):
        self.assertTrue(self.qsort.lessThanEqual(1, 2))
        self.assertEqual(self.qsort.numComparisons, 1)

        self.assertTrue(self.qsort.lessThanEqual(1, 1))
        self.assertEqual(self.qsort.numComparisons, 2)

        self.assertFalse(self.qsort.lessThanEqual(2, 1))
        self.assertEqual(self.qsort.numComparisons, 3)

    def test_greaterThan(self):
        self.assertTrue(self.qsort.greaterThan(2, 1))
        self.assertEqual(self.qsort.numComparisons, 1)

        self.assertFalse(self.qsort.greaterThan(1, 2))
        self.assertEqual(self.qsort.numComparisons, 2)

    def test_greaterThanEqual(self):
        self.assertTrue(self.qsort.greaterThanEqual(2,1))
        self.assertEqual(self.qsort.numComparisons, 1)

        self.assertTrue(self.qsort.greaterThanEqual(2,2))
        self.assertEqual(self.qsort.numComparisons, 2)

        self.assertFalse(self.qsort.greaterThanEqual(2,3))
        self.assertEqual(self.qsort.numComparisons, 3)

    def test_equal(self):
        self.assertTrue(self.qsort.equal(1, 1))
        self.assertEqual(self.qsort.numComparisons, 1)

        self.assertFalse(self.qsort.equal(1,2))
        self.assertEqual(self.qsort.numComparisons, 2)

    def test_sort(self):
        self.assertRaises(NotImplementedError, self.qsort.sort)

    def test_insertionSort(self):
        self.assertInsertionSort([1])
        self.assertInsertionSort([2,1])
        self.assertInsertionSort([1,2])
        self.assertInsertionSort([1,1])
        self.assertInsertionSort([3,2,1])
        self.assertInsertionSort([3,2,3,1])
        self.assertInsertionSort(range(-5,5)[::-1])

    def assertInsertionSort(self, data):
        self.qsort.data = data
        sData = self.qsort._insertionSort(self.qsort.data, 0,len(data))
        self.assertEqual(sData, sorted(data))


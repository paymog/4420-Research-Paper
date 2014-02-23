__author__ = 'paymahnmoghadasian'

import unittest
from ..src.ClassicQuicksort import ClassicQuicksort, PivotSelectionMechanism

class testClassicQuicksort(unittest.TestCase):

    def assertPivot(self, expectedResult):
        self.assertEqual(self.qsort._ClassicQuicksort__selectPivot(0, len(self.qsort.data)), expectedResult)

    def test_selectPivot_First(self):
        self.qsort = ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.First)

        self.qsort.data = [1,2,3]
        self.assertPivot(1)
        self.assertEqual([1,2,3], self.qsort.data)

        self.qsort.data = [3,2,1]
        self.assertPivot(3)
        self.assertEqual([3,2,1], self.qsort.data)

        self.qsort.data = [2,3,1]
        self.assertPivot(2)
        self.assertEqual([2,3,1], self.qsort.data)

        self.qsort.data = [1]
        self.assertPivot(1)
        self.assertEqual([1], self.qsort.data)


    def test_selectPivot_Last(self):
        self.qsort = ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Last)

        self.qsort.data = [1,2,3]
        self.assertPivot(3)
        self.assertEqual([3,2,1], self.qsort.data)

        self.qsort.data = [3,2,1]
        self.assertPivot(1)
        self.assertEqual([1,2,3], self.qsort.data)

        self.qsort.data = [2,3,1]
        self.assertPivot(1)
        self.assertEqual([1,3,2], self.qsort.data)

        self.qsort.data = [1]
        self.assertPivot(1)
        self.assertEqual([1], self.qsort.data)


    def test_selectPivot_Mediam(self):
        self.qsort = ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Median)

        self.qsort.data = [1,2,3]
        self.assertPivot(2)
        self.assertEqual([2,1,3], self.qsort.data)

        self.qsort.data = [3,2,1]
        self.assertPivot(2)
        self.assertEqual([2,3,1], self.qsort.data)

        self.qsort.data = [2,3,1]
        self.assertPivot(2)
        self.assertEqual([2,3,1], self.qsort.data)

        self.qsort.data = [1]
        self.assertPivot(1)
        self.assertEqual([1], self.qsort.data)

        self.qsort.data = [2,1]
        self.assertPivot(1)
        self.assertEqual([1,2], self.qsort.data)

        self.qsort.data = [3,1,2,4]
        self.assertPivot(3)
        self.assertEqual([3,1,2,4], self.qsort.data)

        self.qsort.data = [2,1,3,4]
        self.assertPivot(3)
        self.assertEqual([3,1,2,4], self.qsort.data)

        self.qsort.data = [2,1,4,3]
        self.assertPivot(3)
        self.assertEqual([3,1,4,2], self.qsort.data)

        self.qsort.data = [1,1,2,2,2]
        self.assertPivot(2)
        self.assertEqual([2,1,1,2,2], self.qsort.data)



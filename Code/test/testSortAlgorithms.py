__author__ = 'paymahnmoghadasian'

import unittest
from itertools import permutations
from ..src.ClassicQuicksort import ClassicQuicksort, PivotSelectionMechanism as CPivot
from ..src.DualPivotQuicksort import DualPivotQuicksort, PivotSelectionMechanism as DPivot


class testSortAlgorithms(unittest.TestCase):

    def permutationTest(self, sortObject):
        for i in range(2,7):
            for perm in permutations(range(1,i)):
                sortObject.data = list(perm)
                sortObject.sort()
                self.assertEqual(range(1,i), sortObject.data, "Original Data %s" % str(perm))

    def rangeTest(self, sortObject):
        for i in range(1,100):
            data = range(i)
            sortObject.data = data[::-1]
            sortObject.sort()
            self.assertEqual(data, sortObject.data)

    def testAlgs(self):
        self.rangeTest(ClassicQuicksort(None))
        self.rangeTest(ClassicQuicksort(None, pivotSelection=CPivot.Last))
        self.rangeTest(ClassicQuicksort(None, pivotSelection=CPivot.Median))
        self.rangeTest(ClassicQuicksort(None, True))
        self.rangeTest(ClassicQuicksort(None, True, 5))
        self.rangeTest(ClassicQuicksort(None, True, pivotSelection=CPivot.Median))
        self.rangeTest(DualPivotQuicksort(None))

        self.permutationTest(ClassicQuicksort(None))
        self.permutationTest(ClassicQuicksort(None, pivotSelection=CPivot.Last))
        self.permutationTest(ClassicQuicksort(None, pivotSelection=CPivot.Median))
        self.permutationTest(ClassicQuicksort(None, True))
        self.permutationTest(ClassicQuicksort(None, True, 5))
        self.permutationTest(ClassicQuicksort(None, True, pivotSelection=CPivot.Median))
        self.permutationTest(DualPivotQuicksort(None))
        self.permutationTest(DualPivotQuicksort(None, pivotSelection=DPivot.Tertiles))





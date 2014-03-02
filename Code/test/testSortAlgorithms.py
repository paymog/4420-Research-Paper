__author__ = 'paymahnmoghadasian'

import unittest
from itertools import permutations
from ..src.ClassicQuicksort import ClassicQuicksort, PivotSelectionMechanism
from ..src.DualPivotQuicksort import DualPivotQuicksort


class testSortAlgorithms(unittest.TestCase):

    def permutationTest(self, sortObject):
        for i in range(3,7):
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
        self.rangeTest(ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Last))
        self.rangeTest(ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Median))
        self.rangeTest(ClassicQuicksort(None, True))
        self.rangeTest(ClassicQuicksort(None, True, 5))
        self.rangeTest(ClassicQuicksort(None, True, pivotSelection=PivotSelectionMechanism.Median))
        self.rangeTest(DualPivotQuicksort(None))

        self.permutationTest(ClassicQuicksort(None))
        self.permutationTest(ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Last))
        self.permutationTest(ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Median))
        self.permutationTest(ClassicQuicksort(None, True))
        self.permutationTest(ClassicQuicksort(None, True, 5))
        self.permutationTest(ClassicQuicksort(None, True, pivotSelection=PivotSelectionMechanism.Median))
        self.permutationTest(DualPivotQuicksort(None))


    def testDualPivotQuicksort(self):
        sort = DualPivotQuicksort(None)

        #other test cases
        sort.data = [1,2,1,1]
        sort.sort()
        self.assertEqual([1,1,1,2], sort.data)

        sort.data = [1,1,2,1]
        sort.sort()
        self.assertEqual([1,1,1,2], sort.data)

        sort.data = [2,1,2,2]
        sort.sort()
        self.assertEqual([1,2,2,2], sort.data)

        sort.data = [2,2,1,2]
        sort.sort()
        self.assertEqual([1,2,2,2], sort.data)

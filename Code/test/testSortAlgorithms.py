__author__ = 'paymahnmoghadasian'

import unittest
from ..src.ClassicQuicksort import ClassicQuicksort, PivotSelectionMechanism
from ..src.DualPivotQuicksort import DualPivotQuicksort


class testSortAlgorithms(unittest.TestCase):

    def runTest(self, sortObject):
        for i in range(1,100):
            data = range(i)
            sortObject.data = data[::-1]
            sortObject.sort()
            self.assertEqual(data, sortObject.data)

    def testAlgs(self):
        self.runTest(ClassicQuicksort(None))
        self.runTest(ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Last))
        self.runTest(ClassicQuicksort(None, pivotSelection=PivotSelectionMechanism.Median))
        self.runTest(ClassicQuicksort(None, True))
        self.runTest(ClassicQuicksort(None, True, 5))
        self.runTest(ClassicQuicksort(None, True, pivotSelection=PivotSelectionMechanism.Median))
        self.runTest(DualPivotQuicksort(None))


    def testDualPivotQuicksort(self):
        # these are tests that failed when the testAlgs method ran for the first time
        sort = DualPivotQuicksort([3,2,1,0])
        sort.sort()
        self.assertEqual([0,1,2,3], sort.data)

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

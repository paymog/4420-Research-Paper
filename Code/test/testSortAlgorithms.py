__author__ = 'paymahnmoghadasian'

import unittest
from ..src.ClassicQuicksort import ClassicQuicksort, PivotSelectionMechanism


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

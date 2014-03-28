__author__ = 'paymahnmoghadasian'

import unittest
from itertools import permutations
from ..src.ClassicQuicksort import ClassicQuicksort
from ..src.DualPivotQuicksort import DualPivotQuicksort
from ..src.YaroslavskiyQuicksort import YaroslavskiyQuicksort


class testSortAlgorithms(unittest.TestCase):

    def permutationTest(self, sortObject):
        for i in range(2,9):
            for perm in permutations(range(1,i)):
                sortObject.data = list(perm)
                sortObject.sort()
                self.assertEqual(range(1,i), sortObject.data, "Original Data %s" % str(perm))

    def rangeTest(self, sortObject):
        for i in range(2,100):
            data = range(i)
            sortObject.data = data[::-1]
            sortObject.sort()
            self.assertEqual(data, sortObject.data, "Original Data %s" % ",".join([str(a) for a in data[::-1]]))

    def runPermAndRange(self, sorter):
        self.rangeTest(sorter)
        self.permutationTest(sorter)

    def testAlgs(self):
        self.runPermAndRange(ClassicQuicksort(None))
        self.runPermAndRange(ClassicQuicksort(None, pivotSelection=2))
        self.runPermAndRange(ClassicQuicksort(None, pivotSelection=3))
        self.runPermAndRange(ClassicQuicksort(None, True))
        self.runPermAndRange(ClassicQuicksort(None, True, 5))
        self.runPermAndRange(ClassicQuicksort(None, True, pivotSelection=3))
        self.runPermAndRange(DualPivotQuicksort(None))
        self.runPermAndRange(YaroslavskiyQuicksort(None))
        self.runPermAndRange(DualPivotQuicksort(None, behaveOptimally=True))



